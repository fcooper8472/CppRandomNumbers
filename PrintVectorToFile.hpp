#ifndef CPPRANDOMNUMBERS_PRINTVECTORTOFILE_HPP
#define CPPRANDOMNUMBERS_PRINTVECTORTOFILE_HPP

#include <cmath>
#include <filesystem>
#include <fstream>
#include <string>
#include <vector>


class ProbabilityDensityFunction {
public:
    virtual double Pdf(double x) = 0;

    virtual double LogPdf(double x) = 0;
};


void PrintVectorToFile(const std::string &fname, const std::vector<double> &vec) {

    const auto output_dir = std::filesystem::path("/tmp") / "CppRandomNumbers" / "RandomSamples";
    std::filesystem::create_directories(output_dir);

    std::ofstream f;
    f.open(output_dir / fname);

    for (const auto &x : vec) {
        f << x << "\n";
    }

    f.close();
}

bool ApproxEqual(const double a, const double b, const double epsilon = 1e-12) {
    return std::fabs(a - b) < epsilon;
}

void PrintPdfToFile(ProbabilityDensityFunction* pPdf, const std::string &fname, const double lower, const double upper) {

    const std::size_t n = 100;
    const double delta = (upper - lower) / n;

    std::vector<double> x_vals;
    x_vals.reserve(n);
    for (std::size_t i = 0; i < n; ++i) {
        x_vals.push_back(lower + i * delta);
    }

    std::vector<double> pdf_vals;
    pdf_vals.reserve(n);
    for (double& x : x_vals) {
        pdf_vals.push_back(pPdf->Pdf(x));
    }

    std::vector<double> log_vals;
    log_vals.reserve(n);
    for (double& x : x_vals) {
        log_vals.push_back(pPdf->LogPdf(x));
    }

    const auto output_dir = std::filesystem::path("/tmp") / "CppRandomNumbers" / "Pdf";
    std::filesystem::create_directories(output_dir);

    std::ofstream f;
    f.open(output_dir / fname);

    for (std::size_t i = 0; i < n; ++i) {
        f << x_vals[i] << ',' << pdf_vals[i] << log_vals[i] << '\n';
    }

    f.close();
}

#endif //CPPRANDOMNUMBERS_PRINTVECTORTOFILE_HPP
