#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <random>

int main() {
    // Seed a Mersenne twister with a 'true' random seed from random_device
    std::random_device rd{};
    std::mt19937 gen{rd()};

    // Params
    const std::size_t n = 100'000;
    const double mu = 1.2;
    const double sigma = 2.3;

    // Create Cauchy distribution which we then modify when sampling from it.
    std::cauchy_distribution<double> dis(mu, sigma);

    // Create and fill the vector
    std::vector<double> vec(n);
    for (double &x : vec) {
        do {
            x = dis(gen);
        }
        while (x < 0.0);
    }

    PrintVectorToFile("HalfCauchy_mu=1.2_sigma=2.3", vec);  // This is just for testing and can be removed

    return 0;
}