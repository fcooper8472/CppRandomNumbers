import os
import subprocess

import matplotlib.pyplot as plt
import numpy as np


import scipy.stats


# Output directory
output_dir = os.path.join('/tmp', 'CppRandomNumbers', 'RandomSamples')

script_dir = os.path.realpath(os.path.dirname(__file__))
build_dir = os.path.join(script_dir, 'Debug')

print('\n### Cleaning output directory')
for file in os.listdir(output_dir):
    subprocess.call(['rm', file], cwd=output_dir)

print('\n### Making build directory')
subprocess.call(['mkdir', '-p', build_dir])

print('\n### Running CMake')
subprocess.call(['cmake', '..'], cwd=build_dir)

print('\n### Building all')
subprocess.call(['cmake', '--build', '.'], cwd=build_dir)

exes_and_outputs = {
    'rand_normal': "Normal_mean=1.23_std=2.34",
}

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

###########################
# Normal dist
###########################
print('  normal')
raw_output = exes_and_outputs['rand_normal']

output_file = os.path.join(output_dir, raw_output)
graph_name = os.path.join(output_dir, '{}.svg'.format(raw_output))

cpp_mean = 1.23
cpp_std = 2.34

x = np.linspace(cpp_mean - 3 * cpp_std, cpp_mean + 3 * cpp_std, num=100)
y = scipy.stats.norm.pdf(x, cpp_mean, cpp_std)

data = np.loadtxt(output_file)

plt.hist(data, bins=25, density=True)
plt.plot(x, y)
plt.title(raw_output.replace('_', ' '))
plt.savefig(graph_name)
plt.close()


# Verify all outputs have a graph
print('\n### Verifying all graphs exist')
for val in exes_and_outputs.values():
    output_file = os.path.join(output_dir, '{}.svg'.format(val))
    assert(os.path.isfile(output_file))

print('\n### Done.')
