from setuptools import setup, find_packages

setup(
    name='Micropiper',
    version='1.0.0',
    description='Forget pip, use Micropiper. A quick and easy solution for using functions from Python packages. The Micropiper ecosystem is different, and for a library to be downloadable with it, it must consist of just one file, called main.py. An internet connection is required.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/simplyYan/Micropiper',
    author='simplyYan',
    author_email='yan.dev.hireme@email.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
