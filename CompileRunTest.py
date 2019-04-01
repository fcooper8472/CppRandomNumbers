import os
import subprocess

import matplotlib.pyplot as plt
import numpy as np

import scipy.stats

# Define directories
output_dir = os.path.join('/tmp', 'CppRandomNumbers', 'RandomSamples')
script_dir = os.path.realpath(os.path.dirname(__file__))
build_dir = os.path.join(script_dir, 'Debug')

# Define the C++ targets and associated data files
exes_and_outputs = {
    'rand_normal': "Normal_mean=1.23_std=2.34",
    'rand_uniform': "Uniform_a=1.23_b=2.34",
    'rand_beta': "Beta_alpha=1.23_beta=2.34",
    'rand_gamma': "Gamma_alpha=4_beta=0.5",
    'rand_cauchy': "Cauchy_mu=8.9_sigma=2.3",
    'rand_exponential': "Exponential_rate=2.3",
    'rand_half_cauchy': "HalfCauchy_mu=1.2_sigma=2.3",
    'rand_student_t': "StudentT_df=4_mu=9.7_sigma=3.3",
}


def main():

    print('\n### Cleaning output directory')
    if os.path.isdir(output_dir):
        for file in os.listdir(output_dir):
            subprocess.call(['rm', file], cwd=output_dir)

    print('\n### Making build directory')
    subprocess.call(['mkdir', '-p', build_dir])

    print('\n### Running CMake')
    subprocess.call(['cmake', '..'], cwd=build_dir)

    print('\n### Building all')
    subprocess.call(['cmake', '--build', '.'], cwd=build_dir)

    print('\n### Running executables...')
    for executable in exes_and_outputs.keys():
        print('  {}'.format(executable))
        subprocess.call(['./{}'.format(executable)], cwd=build_dir)

    # Verify all outputs exist
    print('\n### Verifying all outputs exist')
    for val in exes_and_outputs.values():
        output_file = os.path.join(output_dir, val)
        assert(os.path.isfile(output_file))

    print('\n### Creating graphs for...')

    print('  normal')
    plot_normal()

    print('  uniform')
    plot_uniform()

    print('  beta')
    plot_beta()

    print('  gamma')
    plot_gamma()

    print('  cauchy')
    plot_cauchy()

    print('  exponential')
    plot_exponential()

    print('  half cauchy')
    plot_half_cauchy()

    print('  student t')
    plot_student_t()

    # Verify all outputs have a graph
    print('\n### Verifying all graphs exist')
    for val in exes_and_outputs.values():
        output_file = os.path.join(output_dir, '{}.svg'.format(val))
        assert(os.path.isfile(output_file))

    print('\n### Done.')


def plot_normal():
    """
    Plot the data from the C++ script against the scipy pdf, for the normal distribution
    """
    raw_output = exes_and_outputs['rand_normal']

    output_file = os.path.join(output_dir, raw_output)
    graph_name = os.path.join(output_dir, '{}.svg'.format(raw_output))

    cpp_mean = 1.23
    cpp_std = 2.34

    data = np.loadtxt(output_file)
    lower = np.quantile(data, 0.005)
    upper = np.quantile(data, 0.995)
    data = np.clip(data, lower, upper)

    x = np.linspace(lower, upper, num=100)
    y = scipy.stats.norm.pdf(x, cpp_mean, cpp_std)

    plt.hist(data, bins=25, density=True)
    plt.plot(x, y)
    plt.title(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def plot_uniform():
    """
    Plot the data from the C++ script against the scipy pdf, for the uniform distribution
    """
    raw_output = exes_and_outputs['rand_uniform']

    output_file = os.path.join(output_dir, raw_output)
    graph_name = os.path.join(output_dir, '{}.svg'.format(raw_output))

    cpp_a = 1.23
    cpp_b = 2.34

    data = np.loadtxt(output_file)
    lower = 1.23
    upper = 2.34

    scipy_loc = cpp_a
    scipy_scale = cpp_b - cpp_a

    x = np.linspace(lower, upper, num=100)
    y = scipy.stats.uniform.pdf(x, loc=scipy_loc, scale=scipy_scale)

    plt.hist(data, bins=25, density=True)
    plt.plot(x, y)
    plt.title(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def plot_beta():
    """
    Plot the data from the C++ script against the scipy pdf, for the beta distribution
    """
    raw_output = exes_and_outputs['rand_beta']

    output_file = os.path.join(output_dir, raw_output)
    graph_name = os.path.join(output_dir, '{}.svg'.format(raw_output))

    cpp_alpha = 1.23
    cpp_beta = 2.34

    data = np.loadtxt(output_file)
    lower = 0.0
    upper = 1.0

    x = np.linspace(lower, upper, num=100)
    y = scipy.stats.beta.pdf(x, a=cpp_alpha, b=cpp_beta)

    plt.hist(data, bins=25, density=True)
    plt.plot(x, y)
    plt.title(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def plot_gamma():
    """
    Plot the data from the C++ script against the scipy pdf, for the gamma distribution
    """
    raw_output = exes_and_outputs['rand_gamma']

    output_file = os.path.join(output_dir, raw_output)
    graph_name = os.path.join(output_dir, '{}.svg'.format(raw_output))

    cpp_alpha = 4.0
    cpp_beta = 0.5

    data = np.loadtxt(output_file)
    lower = 0.0
    upper = np.quantile(data, 0.99)
    data = np.clip(data, lower, upper)

    x = np.linspace(lower, upper, num=100)
    y = scipy.stats.gamma.pdf(x, a=cpp_alpha, scale=1 / cpp_beta)

    plt.hist(data, bins=25, density=True)
    plt.plot(x, y)
    plt.title(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def plot_cauchy():
    """
    Plot the data from the C++ script against the scipy pdf, for the cauchy distribution
    """
    raw_output = exes_and_outputs['rand_cauchy']

    output_file = os.path.join(output_dir, raw_output)
    graph_name = os.path.join(output_dir, '{}.svg'.format(raw_output))

    cpp_mu = 8.9
    cpp_sigma = 2.3

    data = np.loadtxt(output_file)
    lower = np.quantile(data, 0.05)
    upper = np.quantile(data, 0.95)
    data = np.clip(data, lower, upper)

    x = np.linspace(lower, upper, num=100)
    y = scipy.stats.cauchy.pdf(x, loc=cpp_mu, scale=cpp_sigma)

    plt.hist(data, bins=25, density=True)
    plt.plot(x, y)
    plt.title(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def plot_exponential():
    """
    Plot the data from the C++ script against the scipy pdf, for the exponential distribution
    """
    raw_output = exes_and_outputs['rand_exponential']

    output_file = os.path.join(output_dir, raw_output)
    graph_name = os.path.join(output_dir, '{}.svg'.format(raw_output))

    cpp_rate = 2.34

    data = np.loadtxt(output_file)
    lower = 0.0
    upper = np.quantile(data, 0.99)
    data = np.clip(data, lower, upper)

    x = np.linspace(lower, upper, num=100)
    y = scipy.stats.expon.pdf(x, scale=1. / cpp_rate)

    plt.hist(data, bins=25, density=True)
    plt.plot(x, y)
    plt.title(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def plot_half_cauchy():
    """
    Plot the data from the C++ script against the scipy pdf, for the half cauchy distribution
    """
    raw_output = exes_and_outputs['rand_half_cauchy']

    output_file = os.path.join(output_dir, raw_output)
    graph_name = os.path.join(output_dir, '{}.svg'.format(raw_output))

    cpp_mu = 1.2
    cpp_sigma = 2.3

    data = np.loadtxt(output_file)
    lower = 0.0
    upper = np.quantile(data, 0.9)
    data = np.clip(data, lower, upper)

    import math
    scale_fac = 1.0 / (0.5 + 0.31830988618379067154 * math.atan(cpp_mu / cpp_sigma))

    x = np.linspace(lower, upper, num=100)
    y = scipy.stats.halfcauchy.pdf(x, loc=cpp_mu, scale=cpp_sigma)
    z = scale_fac / (math.pi * cpp_sigma * (1. + ((x - cpp_mu)/cpp_sigma) ** 2))

    plt.hist(data, bins=25, density=True)
    plt.plot(x, y)
    plt.plot(x, z, 'g')
    plt.title(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def plot_student_t():
    """
    Plot the data from the C++ script against the scipy pdf, for the student t distribution
    """
    raw_output = exes_and_outputs['rand_student_t']

    output_file = os.path.join(output_dir, raw_output)
    graph_name = os.path.join(output_dir, '{}.svg'.format(raw_output))

    cpp_df = 4
    cpp_mu = 9.7
    cpp_sigma = 3.3

    data = np.loadtxt(output_file)
    lower = np.quantile(data, 0.005)
    upper = np.quantile(data, 0.995)
    data = np.clip(data, lower, upper)

    x = np.linspace(lower, upper, num=100)
    y = scipy.stats.t.pdf(x, df=cpp_df, loc=cpp_mu, scale=cpp_sigma)

    plt.hist(data, bins=25, density=True)
    plt.plot(x, y)
    plt.title(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


if __name__ == '__main__':
    main()
