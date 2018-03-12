import sys

from setuptools import setup, find_packages

v = sys.version_info
if v[:2] < (3, 0):
    error = "ERROR: ims_lti_py requires Python version 3.0 or above."
    print(error, file=sys.stderr)
    sys.exit(1)

setup_args = dict(
    name='ltiecsdockerspawner',
    version='0.1',
    packages=['ltiecsdockerspawner'],
    url='https://github.com/xaviaracil/ltiecsdockerspawner',
    license='MIT License',
    author='Xavi Aracil',
    author_email='xaracil@uoc.edu',
    description='LTI based ECSDockerSpawner for Jupyter'
)

if 'bdist_wheel' in sys.argv:
    import setuptools

# setuptools requirements
if 'setuptools' in sys.modules:
    setup_args['install_requires'] = install_requires = []
    with open('requirements.txt') as f:
        for line in f.readlines():
            req = line.strip()
            if not req or req.startswith(('-e', '#')):
                continue
            install_requires.append(req)


def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()