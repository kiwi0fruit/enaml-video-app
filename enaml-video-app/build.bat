@cd /d "%~dp0"
@python -c "import pathlib; print(pathlib.Path.cwd().as_uri())" | call .\setvar cwd_url

:: create pip source package:
:: (sdist is a source distribution but
::  it can be changed to a binary wheel):
python setup.py sdist

:: create conda source package:
:: (it's 'noarch' at the moment but
::  it can be changed to a compiled binary):
conda build . --output-folder dist
