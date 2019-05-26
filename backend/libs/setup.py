import os
import setuptools


PATH = os.path.dirname(os.path.abspath(__file__))

setuptools.setup(
    name='color_theory_app_backend_libs',
    version='1.0',
    description='Utils function color_theory_app',
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://www.dkisler.com',
    author='Dmitry Kisler',
    author_email='admin@dkisler.com',
    license='MIT',
    packages=['color_theory_app_backend_libs'],
    package_dir={'color_theory_app_backend_libs':
                 os.path.join(PATH, 'color_theory_app_backend_libs')},
    install_requires=[
        'argparse',
        'logging'
    ],
    include_package_data=False,
    zip_safe=False)
