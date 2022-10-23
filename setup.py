from setuptools import setup,find_packages

setup(
    name = 'lv-bgt-downloader',
    version = '0.1.0',
    description = 'A Python package to download and parse StuF-Geo XML from Dutch BGT Download API version 1.0',
    url = 'https://github.com/octo-willy/lv-bgt-downloader',
    author = 'octo-willy',
    author_email='octowilly@email.com',
    license = 'BSD 2-clause',
    packages = find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers'
    ]

)
