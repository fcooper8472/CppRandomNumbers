#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <cassert>
#include <cmath>
#include <limits>

class GammaDistributionPdf : public ProbabilityDensityFunction {
private:
    // Params
    double mAlpha;
    double mBeta;

    // Cached constants for Pdf & LogPdf
    double mPrefactor;
    double mLogPrefactor;
    double mAm1;

public:
    explicit GammaDistributionPdf(double alpha = 1.0, double beta = 1.0)
            :
            mAlpha(alpha),
            mBeta(beta) {

        // Both params must be positive
        assert(mAlpha > 0.0);
        assert(mBeta > 0.0);

        // Constants for Beta function evaluations
        mPrefactor = std::pow(mBeta, mAlpha) / std::tgamma(mAlpha);
        mLogPrefactor = mAlpha * std::log(mBeta) - std::lgamma(mAlpha);

        // Other useful constants
        mAm1 = mAlpha - 1.0;
    }

    double Pdf(const double x) override {
        if (x > 0.0) {
            return mPrefactor * std::pow(x, mAm1) * std::exp(-x * mBeta);
        } else {
            return 0.0;
        }
    }

    double LogPdf(const double x) override {
        if (x > 0.0) {
            return mLogPrefactor + mAm1 * std::log(x) - mBeta * x;
        } else {
            return -std::numeric_limits<double>::infinity();
        }
    }
};

int main() {

    const double alpha = 2.6;
    const double beta = 0.8;
    GammaDistributionPdf pdf{alpha, beta};

    // Regular PDF
    assert(ApproxEqual(pdf.Pdf(-1.0), 0.0));
    assert(ApproxEqual(pdf.Pdf(3.0), 0.20601517762879468));

    // Log PDF
    assert(std::isinf(pdf.LogPdf(-1.0)));
    assert(ApproxEqual(pdf.LogPdf(3.0), -1.5798054350969495));

    const double pdf_lower = 0.01;
    const double pdf_upper = 10.0;
    PrintPdfToFile(&pdf, "Gamma_alpha=2.6_beta=0.8", pdf_lower, pdf_upper);

    return 0;
}