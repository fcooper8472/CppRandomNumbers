#include "../PrintVectorToFile.hpp"  // This is just for testing and can be removed

#include <random>

int main() {
    // Seed a Mersenne twister with a random number from a random_device
    std::random_device rd{};
    std::mt19937 gen{rd()};

    // Params
    const std::size_t n = 1000;
    const double mean = 1.23;
    const double std_dev = 2.34;

    // Create distribution
    std::normal_distribution<double> dist{mean, std_dev};

    // Create and fill the vector
    std::vector<double> vec(n);
    for (double &x : vec) {
        x = dist(gen);
    }

    PrintVectorToFile("Normal_1.23_2.34", vec);  // This is just for testing and can be removed

    return 0;
}