from setuptools import setup

setup(name='Authda',
      packages=['Authda'],
      include_package_data=True,
      test_suite='Authda.tests',
      install_requires=['flask',
                        'flask-sqlalchemy',
                        'flask-testing',
                        'slacker'])

