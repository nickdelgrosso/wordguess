from setuptools import setup

setup(
    name='wordguess',
    version='0.0.1'
    description='A Wordle terminal clone in Python',
    packages=['wordguess'],
    package_data={'wordlists': ['data/words.txt']},
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'wordguess = wordguess.main:main',
        ],  
    },
)