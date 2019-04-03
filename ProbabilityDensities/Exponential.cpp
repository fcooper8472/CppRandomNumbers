#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <cassert>
#include <cmath>
#include <limits>

class ExponentialDistributionPdf : public ProbabilityDensityFunction {
private:
    // Params
    double mRate;

    // Cached constant for LogPdf
    double mLogRate;

public:
    explicit ExponentialDistributionPdf(double rate = 1.0)
            : mRate(rate) {

        // Rate must be positive
        assert(mRate > 0.0);

        mLogRate = std::log(mRate);
    }

    double Pdf(const double x) override {
        if (x >= 0.0) {
            return mRate * std::exp(-x * mRate);
        } else {
            return 0.0;
        }
    }

    double LogPdf(const double x) override {
        if (x >= 0.0) {
            return mLogRate - x * mRate;
        } else {
            return -std::numeric_limits<double>::infinity();
        }
    }
};

int main() {

    const double rate = 0.4;
    ExponentialDistributionPdf pdf{rate};

    // Regular PDF
    assert(ApproxEqual(pdf.Pdf(-1.0), 0.0));
    assert(ApproxEqual(pdf.Pdf(3.0), 0.12047768476488085));

    // Log PDF
    assert(std::isinf(pdf.LogPdf(-1.0)));
    assert(ApproxEqual(pdf.LogPdf(3.0), -2.1162907318741553));

    const double pdf_lower = 0.0;
    const double pdf_upper = 10.0;
    PrintPdfToFile(&pdf, "Exponential_rate=0.4", pdf_lower, pdf_upper);

    return 0;
}