# CppRandomNumbers
Standalone examples for the [Distribution Zoo](https://ben18785.shinyapps.io/distribution-zoo/).

## Probability density functions

The directory `ProbabilityDensities` contains a single `cpp` file for each distribution.
In each file is a minimal class for the corresponding PDF, inheriting from a minimal abstract PDF defined in `Utilities.hpp`.
This minimal PDF defines functions `Pdf` and `LogPdf` that take and return a `double`.
Each file also contains a main function with minimal value-tests for each distribution.

## Random samples of size n

The directory `RandomSamples` contains a standalone `cpp` file with a single main function for each distribution.
Each file is a minimal example of generating a vector of `n` random samples from the corresponding distribution.

## Verifying the examples

The script `CompileRunTest.py` will compile and run each standalone executable and generate graphs to verify against the Python `scipy` statistical distributions.
