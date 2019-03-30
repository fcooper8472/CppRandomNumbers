#ifndef CPPRANDOMNUMBERS_PRINTVECTORTOFILE_HPP
#define CPPRANDOMNUMBERS_PRINTVECTORTOFILE_HPP

#include <filesystem>
#include <fstream>
#include <string>
#include <vector>


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

#endif //CPPRANDOMNUMBERS_PRINTVECTORTOFILE_HPP
