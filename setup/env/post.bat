@echo off
:: inverse order of channels:
%run% conda config --env --add channels conda-forge
%run% conda config --env --add channels defaults

%run% conda install ".\enaml-video-app-0.1.0-py_0.tar.bz2"
%run% conda remove --force --yes pyqtgraph
%run% conda install --copy --yes pyqtgraph
%run% pip install --ignore-installed git+https://github.com/pyqtgraph/pyqtgraph.git
%run% pip install --ignore-installed pyside2

:: %run% python -m ipykernel install --user --name %env%

%run% enaml-video-app-ready
