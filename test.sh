tf='.venv_test'

virtualenv $tf -p python
$tf/bin/pip install -e .
$tf/bin/python setup.py test

rm -rf $tf
