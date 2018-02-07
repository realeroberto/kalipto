from setuptools import setup

setup(name='kalipto',
      version='0.1',
      description='A steganographic chat over social media',
      url='https://github.com/robertoreale/kalipto',
      author='Roberto Reale',
      author_email='roberto.reale@linux.com',
      license='MIT',
      packages=['kalipto'],
      install_requires=['stegano','twitter','wget'],
      entry_points = {
          'console_scripts': ['kalipto=kalipto.cmdline:main'],
      },
      zip_safe=False)
