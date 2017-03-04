"""
author: Rahul Mohandas
"""
import setuptools

setuptools.setup(
    name="smv",
    version="0.1",
    packages=setuptools.find_packages(exclude=["tests"]),
    author="Rahul Mohandas",
    author_email="rahul@rahulmohandas.com",
    description="It's like scp but for moving",
    license="MIT",
    test_suite="tests"
)
