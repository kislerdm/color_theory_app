from setuptools import setup, find_packages

setup(
    name='color_theory_app_backend',
    version='1.0',
    description='Common layer of the color_theory_app backend',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://color-theory-app.dkisler.com',
    author='Dmitry Kisler',
    author_email='admin@dkisler.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.5.4'
    ])
