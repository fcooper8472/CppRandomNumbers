#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <random>

int main() {
    // Seed a Mersenne twister with a 'true' random seed from random_device
    std::random_device rd{};
    std::mt19937 gen{rd()};

    // Params
    const std::size_t n = 100'000;
    const double alpha = 4.0;
    const double beta = 0.5;

    // Create distribution.  Note C++ parameterisation different to distribution zoo, hence the 1/beta here.
    std::gamma_distribution<double> dis(alpha, 1.0 / beta);

    // Create and fill the vector
    std::vector<double> vec(n);
    for (double &x : vec) {
        x = dis(gen);
    }

    PrintVectorToFile("Gamma_alpha=4_beta=0.5", vec);  // This is just for testing and can be removed

    return 0;
}