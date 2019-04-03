#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <cassert>
#include <cmath>

class StudentTDistributionPdf : public ProbabilityDensityFunction {
private:
    // Params
    double mLocation;
    double mScale;
    double mDf;

    // Cached constants for Pdf & LogPdf
    double m1OnSigSq;
    double mDfScale;
    double mPrefactor;
    double mLogPrefactor;

public:
    explicit StudentTDistributionPdf(double location = 0.0, double scale = 1.0, double df = 1.0)
            : mLocation(location), mScale(scale), mDf(df) {

        // Scale and degrees of freedom must be positive
        assert(mScale > 0.0);
        assert(mDf > 0.0);

        // Constants for Beta function evaluations
        const double beta_factor = std::tgamma(0.5 * mDf + 0.5) / (std::tgamma(0.5 * mDf) * std::tgamma(0.5));
        const double log_beta_factor = std::lgamma(0.5 * mDf) + std::lgamma(0.5) - std::lgamma(0.5 * mDf + 0.5);

        // Pre-calculate useful constants
        m1OnSigSq = 1.0 / (mScale * mScale);
        mDfScale = 0.5 * (mDf + 1.0);
        mPrefactor = beta_factor / (std::sqrt(mDf) * mScale);
        mLogPrefactor = -(0.5 * std::log(mDf) + std::log(scale) + log_beta_factor);
    }

    double Pdf(const double x) override {
        return mPrefactor * std::pow(mDf / (mDf + m1OnSigSq * (x - mLocation) * (x - mLocation)), mDfScale);
    }

    double LogPdf(const double x) override {
        return mLogPrefactor - mDfScale * std::log1p(m1OnSigSq * (x - mLocation) * (x - mLocation) / mDf);
    }
};

int main() {

    const double location = 4.2;
    const double scale = 6.4;
    const double df = 3.5;
    StudentTDistributionPdf pdf{location, scale, df};

    // Regular PDF
    assert(ApproxEqual(pdf.Pdf(0.0), 0.04474060649238696));
    assert(ApproxEqual(pdf.Pdf(9.5), 0.03883745265139358));

    // Log PDF
    assert(ApproxEqual(pdf.LogPdf(0.0), -3.106873767080274));
    assert(ApproxEqual(pdf.LogPdf(9.5), -3.2483702234103236));

    const double pdf_lower = location - 3.0 * scale;
    const double pdf_upper = location + 3.0 * scale;
    PrintPdfToFile(&pdf, "StudentT_location=4.2_scale=6.4_df=3.5", pdf_lower, pdf_upper);

    return 0;
}