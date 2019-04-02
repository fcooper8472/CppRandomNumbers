#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <cassert>
#include <cmath>
#include <limits>

class BetaDistributionPdf : public ProbabilityDensityFunction {
private:
    // Params
    double mAlpha;
    double mBeta;

    // Cached constants for Pdf & LogPdf
    double m1OnBetaFn;
    double mLogBetaFn;
    double mAm1;
    double mBm1;

public:
    explicit BetaDistributionPdf(double alpha = 1.0, double beta = 1.0)
            :
            mAlpha(alpha),
            mBeta(beta) {

        // Both params must be positive
        assert(mAlpha > 0.0);
        assert(mBeta > 0.0);

        // Constants for Beta function evaluations
        m1OnBetaFn = std::tgamma(mAlpha + mBeta) / (std::tgamma(mAlpha) * std::tgamma(mBeta));
        mLogBetaFn = std::lgamma(mAlpha + mBeta) - (std::lgamma(mAlpha) + std::lgamma(mBeta));

        // Other useful constants
        mAm1 = mAlpha - 1.0;
        mBm1 = mBeta - 1.0;
    }

    double Pdf(const double x) override {
        if (x > 0.0 && x < 1.0) {
            return std::pow(x, mAm1) * std::pow(1.0 - x, mBm1) * m1OnBetaFn;
        } else {
            return 0.0;
        }
    }

    double LogPdf(const double x) override {
        if (x > 0.0 && x < 1.0) {
            return mAm1 * std::log(x) + mBm1 * std::log1p(-x) + mLogBetaFn;
        } else {
            return -std::numeric_limits<double>::infinity();
        }
    }
};

int main() {

    const double alpha = 2.6;
    const double beta = 4.9;
    BetaDistributionPdf pdf{alpha, beta};

    // Regular PDF
    assert(ApproxEqual(pdf.Pdf(-1.0), 0.0));
    assert(ApproxEqual(pdf.Pdf(0.5), 1.3994593448067123));
    assert(ApproxEqual(pdf.Pdf(2.0), 0.0));

    // Log PDF
    assert(std::isinf(pdf.LogPdf(-1.0)));
    assert(ApproxEqual(pdf.LogPdf(0.5), 0.3360859797527125));
    assert(std::isinf(pdf.LogPdf(2.0)));

    const double pdf_lower = 0.01;
    const double pdf_upper = 0.99;
    PrintPdfToFile(&pdf, "Beta_alpha=2.6_beta=4.9", pdf_lower, pdf_upper);

    return 0;
}