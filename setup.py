from setuptools import setup, find_packages

setup(
    name='food_service',
    version='0.0.3',
    packages=['food_service'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pytest',
        'flask_sqlalchemy',
        'flask_restful',
    ],
)
