from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='pycli',
      version='0.1',
      description='The python commandline tool',
      long_description=readme(),
      keywords='python commandline',
      url='http://github.com/leonqli/pycli',
      author='Leon Li',
      author_email='leonqli@gmail.com',
      license='MIT',
      packages=['pycli'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['pycli=pycli.cli:main'],
      },
      include_package_data=True,
      zip_safe=False)
