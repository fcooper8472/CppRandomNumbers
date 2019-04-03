#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <cassert>
#include <cmath>

class HalfCauchyDistributionPdf : public ProbabilityDensityFunction {
private:
    // Params
    double mLocation;
    double mScale;

    // Cached constants for Pdf & LogPdf
    double m1OnSigSq;
    double mPrefactor;
    double mLogPrefactor;

public:
    explicit HalfCauchyDistributionPdf(double location = 0.0, double scale = 1.0)
            : mLocation(location), mScale(scale) {

        // Sig must be positive
        assert(mScale > 0.0);

        // Pre-calculate useful constants
        const double atan_bit = M_1_PI * std::atan(mLocation / mScale);
        m1OnSigSq = 1.0 / (mScale * mScale);
        mPrefactor = 1.0 / (M_PI * mScale * (0.5 + atan_bit));
        mLogPrefactor = -(std::log(0.5 * M_PI * mScale) + std::log1p(2.0 * atan_bit));
    }

    double Pdf(const double x) override {
        if (x >= 0.0) {
            return mPrefactor / (1.0 + m1OnSigSq * (x - mLocation) * (x - mLocation));
        } else {
            return 0.0;
        }
    }

    double LogPdf(const double x) override {
        if (x >= 0.0) {
            return mLogPrefactor - std::log1p(m1OnSigSq * (x - mLocation) * (x - mLocation));
        } else {
            return -std::numeric_limits<double>::infinity();
        }
    }
};

int main() {

    const double location = 0.0;
    const double scale = 3.5;
    HalfCauchyDistributionPdf pdf{location, scale};

    // Regular PDF
    assert(ApproxEqual(pdf.Pdf(-1.0), 0.0));
    assert(ApproxEqual(pdf.Pdf(1.2), 0.1627588899405796));

    // Log PDF
    assert(std::isinf(pdf.LogPdf(-1.0)));
    assert(ApproxEqual(pdf.LogPdf(1.2), -1.8154853760944443));

    const double pdf_lower = 0.0;
    const double pdf_upper = 5.0 * scale;
    PrintPdfToFile(&pdf, "HalfCauchy_mu=0.0_sig=3.5", pdf_lower, pdf_upper);

    return 0;
}