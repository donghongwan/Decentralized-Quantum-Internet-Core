from setuptools import setup, find_packages

setup(
    name='decentralized-quantum-internet-core',
    version='1.0.0',
    author='KOSASIH',
    author_email='kosasihg88@gmail.com',
    description='A project for a decentralized quantum internet core.',
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests',
        'numpy',
        'cryptography',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
