#include "../PrintVectorToFile.hpp"  // This is just for testing and can be removed

#include <cassert>
#include <cmath>

class NormalDistributionPdf : public ProbabilityDensityFunction {
private:
    // Params
    double mMean;
    double mStdDev;

    // Cached constants for Pdf & LogPdf
    double m2SigSq;
    double mPrefactor;
    double mLogPrefactor;

public:
    explicit NormalDistributionPdf(double mean = 0.0, double std_dev = 1.0)
            :
            mMean(mean),
            mStdDev(std_dev) {
        m2SigSq = 2.0 * mStdDev * mStdDev;
        mPrefactor = 1.0 / std::sqrt(M_PI * m2SigSq);
        mLogPrefactor = -0.5 * std::log(M_PI * m2SigSq);
    }

    double Pdf(const double x) override {
        return mPrefactor * exp(-(x - mMean) * (x - mMean) / m2SigSq);
    }

    double LogPdf(const double x) override {
        return mLogPrefactor - (x - mMean) * (x - mMean) / m2SigSq;
    }
};

int main() {

    const double mean = 8.9;
    const double std_dev = 2.3;
    NormalDistributionPdf pdf{mean, std_dev};

    // Regular PDF
    assert(ApproxEqual(pdf.Pdf(5.0), 0.04119387068037555));
    assert(ApproxEqual(pdf.Pdf(9.6), 0.16560307708677963));

    // Log PDF
    assert(ApproxEqual(pdf.LogPdf(5.0), -3.189465803587792));
    assert(ApproxEqual(pdf.LogPdf(9.6), -1.7981614557617047));

    const double pdf_lower = mean - 3.0 * std_dev;
    const double pdf_upper = mean + 3.0 * std_dev;
    PrintPdfToFile(&pdf, "Normal_mean=8.9_std=2.3", pdf_lower, pdf_upper);

    return 0;
}