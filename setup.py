import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    INSTALL_REQUIRES = [l.split('#')[0].strip() for l in fh if not l.strip().startswith('#')]

setuptools.setup(
    name="GetOldTweets3_nd",
    version="0.0.11",
    author="",
    author_email="",
    license='MIT',
    description="Get old tweets from Twitter without debug",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucafirefox/GetOldTweets3_nd",
    keywords="twitter tweets",
    packages=setuptools.find_packages(),
    scripts=['bin/GetOldTweets3_nd'],
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
    ],
    python_requires='>=3.4',
    install_requires=INSTALL_REQUIRES
)
