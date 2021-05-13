from setuptools import setup

setup(
    name='covidpy',
    version='0.1.0',
    description='Detailed Regular Information about World\'s Covid19 Data',
    url='https://github.com/shuds13/pyexample',
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
