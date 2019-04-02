#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <random>

int main() {
    // Seed a Mersenne twister with a 'true' random seed from random_device
    std::random_device rd{};
    std::mt19937 gen{rd()};

    // Params
    const std::size_t n = 100'000;
    const double mu = 8.9;
    const double sigma = 2.3;

    // Create distribution.
    std::cauchy_distribution<double> dis(mu, sigma);

    // Create and fill the vector
    std::vector<double> vec(n);
    for (double &x : vec) {
        x = dis(gen);
    }

    PrintVectorToFile("Cauchy_mu=8.9_sigma=2.3", vec);  // This is just for testing and can be removed

    return 0;
}