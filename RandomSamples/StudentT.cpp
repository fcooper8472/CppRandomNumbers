#include "../PrintVectorToFile.hpp"  // This is just for testing and can be removed

#include <random>

int main() {
    // Seed a Mersenne twister with a 'true' random seed from random_device
    std::random_device rd{};
    std::mt19937 gen{rd()};

    // Params
    const std::size_t n = 100'000;
    const std::size_t df = 4;
    const double mu = 9.7;
    const double sigma = 3.3;

    // Create distribution.
    std::student_t_distribution<double> dis(df);

    // Create and fill the vector
    std::vector<double> vec(n);
    for (double &x : vec) {
        x = dis(gen) * sigma + mu;
    }

    PrintVectorToFile("StudentT_df=4_mu=9.7_sigma=3.3", vec);  // This is just for testing and can be removed

    return 0;
}