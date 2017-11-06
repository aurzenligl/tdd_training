from setuptools import setup, find_packages

setup(
    name='sokoban',
    version='0.0.1',
    packages=find_packages(),
    install_requires = ['pygame'],
    entry_points = {
        'console_scripts': [
            'sokoban = sokoban.__main__:main'
        ],
    },
)
