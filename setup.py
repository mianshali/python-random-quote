from setuptools import setup, find_packages

setup(
    name='randomquote',
    version='0.1',
    description='Get a random quote',
    url='https://github.com/mianshali/python3-random.git',
    author='mian ali',
    author_email='mianshali5@gmail.com',
    license='MIT',
    install_requires=['requests'],
    packages=find_packages(),
    entry_points=dict(
         console_scripts=['rq=src.main:display_quote']
    )
)
