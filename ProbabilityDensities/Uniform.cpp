#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <cassert>
#include <cmath>
#include <limits>

class UniformDistributionPdf : public ProbabilityDensityFunction {
private:
    // Params
    double mA;
    double mB;

    // Cached constants for Pdf & LogPdf
    double mHeight;
    double mLogHeight;

public:
    explicit UniformDistributionPdf(double a = 0.0, double b = 1.0)
            :
            mA(a),
            mB(b) {
        assert(mA < mB);
        mHeight = 1.0 / (mB - mA);
        mLogHeight = -std::log(mB - mA);
    }

    double Pdf(const double x) override {
        return x >= mA && x <= mB ? mHeight : 0.0;
    }

    double LogPdf(const double x) override {
        return x >= mA && x <= mB ? mLogHeight : -std::numeric_limits<double>::infinity();
    }
};

int main() {

    const double a = 1.2;
    const double b = 2.8;
    UniformDistributionPdf pdf{a, b};

    // Regular PDF
    assert(ApproxEqual(pdf.Pdf(0.0), 0.0));
    assert(ApproxEqual(pdf.Pdf(2.0), 0.625));
    assert(ApproxEqual(pdf.Pdf(4.0), 0.0));

    // Log PDF
    assert(std::isinf(pdf.LogPdf(0.0)));
    assert(ApproxEqual(pdf.LogPdf(2.0), -0.47000362924573563));
    assert(std::isinf(pdf.LogPdf(4.0)));

    const double pdf_lower = a;
    const double pdf_upper = b;
    PrintPdfToFile(&pdf, "Uniform_a=1.2_b=2.8", pdf_lower, pdf_upper);

    return 0;
}