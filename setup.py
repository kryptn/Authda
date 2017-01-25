from setuptools import setup

package_json = {
  "name": "authda",
  "version": "1.0.0",
  "description": "idk a slack auth written for romeo using aws lambda ideally",
  "main": "Authda/invite.jsx",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/kryptn/authda.git"
  },
  "author": "kryptn",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/kryptn/authda/issues"
  },
  "homepage": "https://github.com/kryptn/authda#readme",
  "dependencies": {
    "babel-preset-react": "^6.22.0",
    "bootstrap": "^3.3.7",
    "react": "^15.4.2",
    "react-bootstrap": "^0.30.7",
    "react-dom": "^15.4.2",
    "whatwg-fetch": "^2.0.2",
  },
  "devDependencies": {
    "babel-core": "^6.22.1",
    "babel-loader": "^6.2.10",
    "babel-preset-es2015": "^6.22.0",
    "css-loader": "^0.26.1",
    "file-loader": "^0.9.0",
    "style-loader": "^0.13.1",
    "url-loader": "^0.5.7",
    "webpack": "^1.14.0"
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
                        'slacker',
                        'calmjs'])

