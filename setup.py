#!/usr/bin/env python
from setuptools import find_packages, setup

from paypal import VERSION

sorl_thumbnail_version = 'sorl-thumbnail>=12.4.1,<12.5'
easy_thumbnails_version = 'easy-thumbnails==2.5'

setup(
    name='django-oscar-paypal',
    version=VERSION,
    url='https://github.com/django-oscar/django-oscar-paypal',
    description=(
        "Integration with PayPal Express, PayPal Payflow Pro and Adaptive "
        "Payments for django-oscar"),
    long_description=open('README.rst').read(),
    keywords="Payment, PayPal, Oscar",
    license=open('LICENSE').read(),
    platforms=['linux'],
    packages=find_packages(exclude=['sandbox*', 'tests*']),
    include_package_data=True,
    install_requires=[
        'django-oscar>=2.0,<2.1',
        'django>=1.11,<2.3',
        'requests>=1.0',
        'django-localflavor',
        sorl_thumbnail_version,
        easy_thumbnails_version,
    ],
    tests_require=[
        'django-webtest==1.9.4',
        'pytest-cov==2.6.1',
        'pytest-django==3.4.8',
        sorl_thumbnail_version,
        easy_thumbnails_version,
    ],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Other/Nonlisted Topic'],
)
