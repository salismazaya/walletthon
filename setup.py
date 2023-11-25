from setuptools import setup, find_packages

setup(
    name='walletthon',
    version='0.0.1',
    author='Salis Mazaya',
    author_email='salismazaya@gmail.com',
    description='Unofficial library for managing your @wallet account',
    url='https://github.com/salismazaya/walletthon',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=[
        'requests',
        'telethon',
    ],
    python_requires='>=3.10',
)
