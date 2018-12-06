@echo off
:: inverse order of channels:
%run% conda config --env --add channels conda-forge
%run% conda config --env --add channels defaults

%run% conda remove --force --yes pyqtgraph
%run% pip install git+https://github.com/pyqtgraph/pyqtgraph.git
%run% conda remove --force --yes qt pyqt sip
%run% pip install pyside2

:: %run% python -m ipykernel install --user --name %env%
