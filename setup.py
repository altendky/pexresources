import setuptools


setuptools.setup(
    name="pexresources",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pexresources = pexresources.cli:cli',
        ],
    },
    install_requires=[
        'click',
        'importlib_resources',
    ],
    extras_require={
        'dev': [
            'pex',
        ],
    },
)
