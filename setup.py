# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='django-issue-synchronisation',
    version=__import__('issues').__version__,
    description='Issue synchronisation for django applications',
    long_description="""Synchronizes different issue trackers into a django based application.""",
    author='Henning Kage',
    author_email='henning.kage@gmail.com',
    url='https://github.com/hkage/django-issue-synchronisation',
    license='GPLv3',
    packages=find_packages(exclude=('tests', 'example')),
    data_files=[('issues/fixtures', ['issues/fixtures/issues.json'])],
    tests_require=[
        'django>=1.3,<1.6',
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Bug Tracking'
    ],
)
