#include "../Utilities.hpp"  // This is just for testing and can be removed

#include <random>

int main() {
    // Seed a Mersenne twister with a 'true' random seed from random_device
    std::random_device rd{};
    std::mt19937 gen{rd()};

    // Params
    const std::size_t n = 100'000;
    const double a = 1.23;
    const double b = 2.34;

    // Create distribution. Note support is [a, b) not [a, b].  Use std::nextafter(b, b + 1.0) if you care.
    std::uniform_real_distribution<double> dist{a, b};

    // Create and fill the vector
    std::vector<double> vec(n);
    for (double &x : vec) {
        x = dist(gen);
    }

    PrintVectorToFile("Uniform_a=1.23_b=2.34", vec);  // This is just for testing and can be removed

    return 0;
}