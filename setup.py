from setuptools import find_packages, setup

requirements = [
    "numpy",
    "scipy",
    "scikit-learn",
    "pandas",
]

setup(
    name='joint_mds',
    version='0.0.0',
    packages=find_packages(),
    install_requires=requirements,
    description="",
    author="",
    author_email='',
    license="MIT license",
)