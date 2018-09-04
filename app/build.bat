set "script_dir=%~dp0"
cd /d "%script_dir%"

python setup.py sdist
:: sdist is a source distribution
:: it can be changed to binary wheel

start dist
