import os
import subprocess

import matplotlib.pyplot as plt
import numpy as np

import scipy.stats

# Define directories
output_sample_dir = os.path.join('/tmp', 'CppRandomNumbers', 'RandomSamples')
output_pdf_dir = os.path.join('/tmp', 'CppRandomNumbers', 'Pdf')
script_dir = os.path.realpath(os.path.dirname(__file__))
build_dir = os.path.join(script_dir, 'Debug')

# Define the C++ targets and associated data files
pdf_exes_and_outputs = {
    'pdf_normal': "Normal_mean=8.9_std=2.3",
    'pdf_uniform': "Uniform_a=1.2_b=2.8",
    'pdf_beta': "Beta_alpha=2.6_beta=4.9",
    'pdf_gamma': "Gamma_alpha=2.6_beta=0.8",
}

sample_exes_and_outputs = {
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

    print('\n### Cleaning output directories')
    if os.path.isdir(output_sample_dir):
        for file in os.listdir(output_sample_dir):
            subprocess.call(['rm', file], cwd=output_sample_dir)

    if os.path.isdir(output_pdf_dir):
        for file in os.listdir(output_pdf_dir):
            subprocess.call(['rm', file], cwd=output_pdf_dir)

    print('\n### Making build directory')
    subprocess.call(['mkdir', '-p', build_dir])

    print('\n### Running CMake')
    subprocess.call(['cmake', '..'], cwd=build_dir)

    print('\n### Building all')
    subprocess.call(['cmake', '--build', '.'], cwd=build_dir)

    ####################################################################################################################
    # PDF executables
    ####################################################################################################################
    print('\n### Running pdf executables...')
    for executable in pdf_exes_and_outputs.keys():
        print('  {}'.format(executable))
        subprocess.call(['./{}'.format(executable)], cwd=build_dir)

    # Verify all outputs exist
    print('\n### Verifying all pdf outputs exist')
    for val in pdf_exes_and_outputs.values():
        output_file = os.path.join(output_pdf_dir, val)
        assert(os.path.isfile(output_file))

    print('\n### Creating pdf graphs for...')
    pdf_plot_normal()
    pdf_plot_uniform()
    pdf_plot_beta()
    pdf_plot_gamma()
    # pdf_plot_cauchy()
    # pdf_plot_exponential()
    # pdf_plot_half_cauchy()
    # pdf_plot_student_t()

    # Verify all sample outputs have a graph
    print('\n### Verifying all graphs exist')
    for val in sample_exes_and_outputs.values():
        # output_file = os.path.join(output_sample_dir, '{}.svg'.format(val))
        # assert(os.path.isfile(output_file))
        pass

    ####################################################################################################################

    ####################################################################################################################
    # Sample executables
    ####################################################################################################################
    print('\n### Running sample executables...')
    for executable in sample_exes_and_outputs.keys():
        print('  {}'.format(executable))
        subprocess.call(['./{}'.format(executable)], cwd=build_dir)

    # Verify all outputs exist
    print('\n### Verifying all sample outputs exist')
    for val in sample_exes_and_outputs.values():
        output_file = os.path.join(output_sample_dir, val)
        assert(os.path.isfile(output_file))

    print('\n### Creating sample graphs for...')
    sample_plot_normal()
    sample_plot_uniform()
    sample_plot_beta()
    sample_plot_gamma()
    sample_plot_cauchy()
    sample_plot_exponential()
    sample_plot_half_cauchy()
    sample_plot_student_t()

    # Verify all sample outputs have a graph
    print('\n### Verifying all graphs exist')
    for val in sample_exes_and_outputs.values():
        output_file = os.path.join(output_sample_dir, '{}.svg'.format(val))
        assert(os.path.isfile(output_file))

    ####################################################################################################################

    print('\n### Done.')


def pdf_plot_normal():
    """
    Plot the data from the C++ script against the scipy pdf, for the normal distribution
    """
    print('  normal')

    raw_output = pdf_exes_and_outputs['pdf_normal']

    output_file = os.path.join(output_pdf_dir, raw_output)
    graph_name = os.path.join(output_pdf_dir, '{}.svg'.format(raw_output))

    cpp_mean = 8.9
    cpp_std = 2.3

    data = np.loadtxt(output_file, delimiter=',')
    x = data[:, 0]
    pdf = data[:, 1]
    log = data[:, 2]

    scipy_pdf = scipy.stats.norm.pdf(x, loc=cpp_mean, scale=cpp_std)
    scipy_log = scipy.stats.norm.logpdf(x, loc=cpp_mean, scale=cpp_std)

    plt.figure(figsize=(14, 6))
    plt.subplot(121)
    plt.plot(x, scipy_pdf, 'orange')
    plt.plot(x, pdf, 'g:', linewidth=5)
    plt.title('pdf')
    plt.gca().set_facecolor('0.85')

    plt.subplot(122)
    plt.plot(x, scipy_log, 'orange')
    plt.plot(x, log, 'g:', linewidth=5)
    plt.title('log pdf')
    plt.gca().set_facecolor('0.85')

    plt.gcf().suptitle(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def pdf_plot_uniform():
    """
    Plot the data from the C++ script against the scipy pdf, for the uniform distribution
    """
    print('  uniform')

    raw_output = pdf_exes_and_outputs['pdf_uniform']

    output_file = os.path.join(output_pdf_dir, raw_output)
    graph_name = os.path.join(output_pdf_dir, '{}.svg'.format(raw_output))

    cpp_a = 1.2
    cpp_b = 2.8

    data = np.loadtxt(output_file, delimiter=',')
    x = data[:, 0]
    pdf = data[:, 1]
    log = data[:, 2]

    scipy_pdf = scipy.stats.uniform.pdf(x, loc=cpp_a, scale=cpp_b - cpp_a)
    scipy_log = scipy.stats.uniform.logpdf(x, loc=cpp_a, scale=cpp_b - cpp_a)

    mean = np.mean(log)

    plt.figure(figsize=(14, 6))
    plt.subplot(121)
    plt.plot(x, scipy_pdf, 'orange')
    plt.plot(x, pdf, 'g:', linewidth=5)
    plt.title('pdf')
    plt.gca().set_facecolor('0.85')

    plt.subplot(122)
    plt.plot(x, scipy_log, 'orange')
    plt.plot(x, log, 'g:', linewidth=5)
    plt.title('log pdf')
    plt.gca().set_facecolor('0.85')
    plt.gca().set_ylim(mean - 0.1 * mean, mean + 0.1 * mean)

    plt.gcf().suptitle(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def pdf_plot_beta():
    """
    Plot the data from the C++ script against the scipy pdf, for the beta distribution
    """
    print('  beta')

    raw_output = pdf_exes_and_outputs['pdf_beta']

    output_file = os.path.join(output_pdf_dir, raw_output)
    graph_name = os.path.join(output_pdf_dir, '{}.svg'.format(raw_output))

    cpp_alpha = 2.6
    cpp_beta = 4.9

    data = np.loadtxt(output_file, delimiter=',')
    x = data[:, 0]
    pdf = data[:, 1]
    log = data[:, 2]

    scipy_pdf = scipy.stats.beta.pdf(x, a=cpp_alpha, b=cpp_beta)
    scipy_log = scipy.stats.beta.logpdf(x, a=cpp_alpha, b=cpp_beta)

    plt.figure(figsize=(14, 6))
    plt.subplot(121)
    plt.plot(x, scipy_pdf, 'orange')
    plt.plot(x, pdf, 'g:', linewidth=5)
    plt.title('pdf')
    plt.gca().set_facecolor('0.85')

    plt.subplot(122)
    plt.plot(x, scipy_log, 'orange')
    plt.plot(x, log, 'g:', linewidth=5)
    plt.title('log pdf')
    plt.gca().set_facecolor('0.85')

    plt.gcf().suptitle(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def pdf_plot_gamma():
    """
    Plot the data from the C++ script against the scipy pdf, for the gamma distribution
    """
    print('  gamma')

    raw_output = pdf_exes_and_outputs['pdf_gamma']

    output_file = os.path.join(output_pdf_dir, raw_output)
    graph_name = os.path.join(output_pdf_dir, '{}.svg'.format(raw_output))

    cpp_alpha = 2.6
    cpp_beta = 0.8

    data = np.loadtxt(output_file, delimiter=',')
    x = data[:, 0]
    pdf = data[:, 1]
    log = data[:, 2]

    scipy_pdf = scipy.stats.gamma.pdf(x, a=cpp_alpha, scale=1 / cpp_beta)
    scipy_log = scipy.stats.gamma.logpdf(x, a=cpp_alpha, scale=1 / cpp_beta)

    plt.figure(figsize=(14, 6))
    plt.subplot(121)
    plt.plot(x, scipy_pdf, 'orange')
    plt.plot(x, pdf, 'g:', linewidth=5)
    plt.title('pdf')
    plt.gca().set_facecolor('0.85')

    plt.subplot(122)
    plt.plot(x, scipy_log, 'orange')
    plt.plot(x, log, 'g:', linewidth=5)
    plt.title('log pdf')
    plt.gca().set_facecolor('0.85')

    plt.gcf().suptitle(raw_output.replace('_', ' '))
    plt.savefig(graph_name)
    plt.close()


def sample_plot_normal():
    """
    Plot the data from the C++ script against the scipy pdf, for the normal distribution
    """
    print('  normal')

    raw_output = sample_exes_and_outputs['rand_normal']

    output_file = os.path.join(output_sample_dir, raw_output)
    graph_name = os.path.join(output_sample_dir, '{}.svg'.format(raw_output))

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


def sample_plot_uniform():
    """
    Plot the data from the C++ script against the scipy pdf, for the uniform distribution
    """
    print('  uniform')
    raw_output = sample_exes_and_outputs['rand_uniform']

    output_file = os.path.join(output_sample_dir, raw_output)
    graph_name = os.path.join(output_sample_dir, '{}.svg'.format(raw_output))

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


def sample_plot_beta():
    """
    Plot the data from the C++ script against the scipy pdf, for the beta distribution
    """
    print('  beta')
    raw_output = sample_exes_and_outputs['rand_beta']

    output_file = os.path.join(output_sample_dir, raw_output)
    graph_name = os.path.join(output_sample_dir, '{}.svg'.format(raw_output))

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


def sample_plot_gamma():
    """
    Plot the data from the C++ script against the scipy pdf, for the gamma distribution
    """
    print('  gamma')
    raw_output = sample_exes_and_outputs['rand_gamma']

    output_file = os.path.join(output_sample_dir, raw_output)
    graph_name = os.path.join(output_sample_dir, '{}.svg'.format(raw_output))

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


def sample_plot_cauchy():
    """
    Plot the data from the C++ script against the scipy pdf, for the cauchy distribution
    """
    print('  cauchy')
    raw_output = sample_exes_and_outputs['rand_cauchy']

    output_file = os.path.join(output_sample_dir, raw_output)
    graph_name = os.path.join(output_sample_dir, '{}.svg'.format(raw_output))

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


def sample_plot_exponential():
    """
    Plot the data from the C++ script against the scipy pdf, for the exponential distribution
    """
    print('  exponential')
    raw_output = sample_exes_and_outputs['rand_exponential']

    output_file = os.path.join(output_sample_dir, raw_output)
    graph_name = os.path.join(output_sample_dir, '{}.svg'.format(raw_output))

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


def sample_plot_half_cauchy():
    """
    Plot the data from the C++ script against the scipy pdf, for the half cauchy distribution
    """
    print('  half cauchy')
    raw_output = sample_exes_and_outputs['rand_half_cauchy']

    output_file = os.path.join(output_sample_dir, raw_output)
    graph_name = os.path.join(output_sample_dir, '{}.svg'.format(raw_output))

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


def sample_plot_student_t():
    """
    Plot the data from the C++ script against the scipy pdf, for the student t distribution
    """
    print('  student t')
    raw_output = sample_exes_and_outputs['rand_student_t']

    output_file = os.path.join(output_sample_dir, raw_output)
    graph_name = os.path.join(output_sample_dir, '{}.svg'.format(raw_output))

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
