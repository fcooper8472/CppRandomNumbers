#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <cassert>
#include <cmath>

class CauchyDistributionPdf : public ProbabilityDensityFunction {
private:
    // Params
    double mMu;
    double mSig;

    // Cached constants for Pdf & LogPdf
    double m1OnSigSq;
    double mPrefactor;
    double mLogPrefactor;

public:
    explicit CauchyDistributionPdf(double mu = 0.0, double sig = 1.0)
            : mMu(mu), mSig(sig) {

        // Sig must be positive
        assert(mSig > 0.0);

        // Pre-calculate useful constants
        m1OnSigSq = 1.0 / (mSig * mSig);
        mPrefactor = 1.0 / (M_PI * mSig);
        mLogPrefactor = -std::log(M_PI * mSig);
    }

    double Pdf(const double x) override {
        return mPrefactor / (1.0 + m1OnSigSq * (x - mMu) * (x - mMu));
    }

    double LogPdf(const double x) override {
        return mLogPrefactor - std::log1p(m1OnSigSq * (x - mMu) * (x - mMu));
    }
};

int main() {

    const double mu = 7.4;
    const double sig = 3.5;
    CauchyDistributionPdf pdf{mu, sig};

    // Regular PDF
    assert(ApproxEqual(pdf.Pdf(5.0), 0.06185922274532301));
    assert(ApproxEqual(pdf.Pdf(9.6), 0.06518926867426962));

    // Log PDF
    assert(ApproxEqual(pdf.LogPdf(5.0), -2.782894076541897));
    assert(ApproxEqual(pdf.LogPdf(9.6), -2.7304604144815317));

    const double pdf_lower = mu - 3.0 * sig;
    const double pdf_upper = mu + 3.0 * sig;
    PrintPdfToFile(&pdf, "Cauchy_mu=7.4_sig=3.5", pdf_lower, pdf_upper);

    return 0;
}