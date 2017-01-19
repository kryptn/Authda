from setuptools import setup

package_json = {
    'dependencies': {
        'react': '~15.0.0',
    }
}


setup(name='Authda',
      packages=['Authda'],
      include_package_data=True,
      test_suite='Authda.tests',
      package_json=package_json,
      install_requires=['flask',
                        'flask-sqlalchemy',
                        'flask-testing',
                        'flask-wtf',
                        'slacker',
                        'calmjs'])

