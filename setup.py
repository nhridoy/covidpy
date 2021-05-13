import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='covidpy',
    version='0.1.3',
    description='Detailed Regular Information about World\'s Covid19 Data',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/hridoyboss12/covidpy',
    author='Nahidujjaman Hridoy',
    author_email='nahidujjamanhridoy@gmail.com',
    license='BSD 2-clause',
    packages=['covidpy'],
    install_requires=['bs4',
                      'requests',
                      'pandas'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
