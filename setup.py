import setuptools
import sys

VERSION = '2.0.0'
INSTALL_REQUIRES = [
    'datastore >= 0.3.6',
    'smhasher >= 0.150',  # Version used by datastore won't compile in Xenial.
    'blinker >= 1.2',
    'WebOb >= 0.9',
    'Mako >= 0.9',
    'bottle >= 0.12.8',
]
EXTRAS_REQUIRE = {}

# https://hynek.me/articles/conditional-python-dependencies/
# Add a conditional dependency on the ipaddress library for validating IP
# addresses; only needed for Python < 3.3.
if int(setuptools.__version__.split('.', 1)[0]) < 18:
    assert 'bdist_wheel' not in sys.argv
    if sys.version_info[0:2] < (3, 3):
        INSTALL_REQUIRES.append('ipaddress')
else:
    EXTRAS_REQUIRE[":python_version<'3.3'"] = ['ipaddress']

setuptools.setup(
    name='switchboard',
    version=VERSION,
    description="Feature flipper for Pyramid, Pylons, or TurboGears apps.",
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='switches feature flipper pyramid pylons turbogears',
    author='Kyle Adams',
    author_email='kadams54@users.noreply.github.com',
    url='https://github.com/switchboardpy/switchboard/',
    download_url='https://github.com/switchboardpy/switchboard/releases',
    license='Apache License',
    packages=setuptools.find_packages(exclude=['ez_setup']),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    zip_safe=False,
    tests_require=[
        'nose',
        'mock',
        'paste', 'selenium >= 3.0',
        'splinter',
    ],
    test_suite='nose.collector',
)
