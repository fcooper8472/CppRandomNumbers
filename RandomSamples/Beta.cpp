#include "../PrintVectorToFile.hpp"  // This is just for testing and can be removed

#include <random>

int main() {
    // Seed a Mersenne twister with a 'true' random seed from random_device
    std::random_device rd{};
    std::mt19937 gen{rd()};

    // Params
    const std::size_t n = 100'000;
    const double alpha = 1.23;
    const double beta = 2.34;

    // No beta distribution in the standard library, so construct samples using two Gammas
    std::gamma_distribution<double> dis_alpha(alpha, 1.0);
    std::gamma_distribution<double> dis_beta(beta, 1.0);

    // Create and fill the vector
    std::vector<double> vec(n);
    for (double &x : vec) {
        const double alpha_sample = dis_alpha(gen);
        x = alpha_sample / (alpha_sample + dis_beta(gen));
    }

    PrintVectorToFile("Beta_alpha=1.23_beta=2.34", vec);  // This is just for testing and can be removed

    return 0;
}