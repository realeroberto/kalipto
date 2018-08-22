from setuptools import setup

setup(name='kalipto',
      version='0.1.1',
      description='A steganographic chat over social media',
      url='https://github.com/reale/kalipto',
      author='Roberto Reale',
      author_email='rober.reale@gmail.com',
      license='MIT',
      packages=['kalipto'],
      install_requires=['stegano','twitter','wget'],
      entry_points = {
          'console_scripts': ['kalipto=kalipto.cmdline:main'],
      },
      zip_safe=False)
