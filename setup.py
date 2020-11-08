from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='torrent-crawler',
    description='Library to search any torrents',
    version='1.0.0',
    url='https://github.com/Alxspb/torrent-crawler',
    download_url='https://github.com/Alxspb/torrent-crawler/releases',
    author='Alxspb',
    author_email='alxspb@list.ru',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    keywords=['pip', 'torrent', 'crawler'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'search-torrent=torrent_crawler.search:main',
        ],
    },
    install_requires=[
        'bs4',
        'requests',
        'html5lib'
    ]
)
