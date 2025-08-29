from setuptools import setup, find_packages

with open('artifacts/requirements.txt') as f:
    install_requires = f.read().splitlines()

with open('artifacts/README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vgs-symbolic-utilities',
    version='1.0.0',
    author='Aaron Slusher / VGS Research Team',
    description='Educational demonstration utilities for symbolic AI system diagnostics.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(where='artifacts', include=['artifacts.utilities*']),
    package_dir={'artifacts': '.'},
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7',
)
