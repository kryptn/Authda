tf='.env'
rm -rf $tf
virtualenv $tf -p python

$tf/bin/pip install calmjs
$tf/bin/pip install -e .
$tf/bin/python setup.py npm --init -w
$tf/bin/python setup.py npm --install
webpack
