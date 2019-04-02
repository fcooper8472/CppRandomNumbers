#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <random>

int main() {
    // Seed a Mersenne twister with a 'true' random seed from random_device
    std::random_device rd{};
    std::mt19937 gen{rd()};

    // Params
    const std::size_t n = 100'000;
    const double rate = 2.3;

    // Create distribution
    std::exponential_distribution<double> dist{rate};

    // Create and fill the vector
    std::vector<double> vec(n);
    for (double &x : vec) {
        x = dist(gen);
    }

    PrintVectorToFile("Exponential_rate=2.3", vec);  // This is just for testing and can be removed

    return 0;
}