@echo off

:: -------- <custom vars> ----
set "env=enaml_video_app"
set "yaml=env_win.yml"
:: -------- </custom vars> ----


:: <miniconda path confirmation>
set "miniconda_dir=%UserProfile%\Miniconda3"
If not exist "%miniconda_dir%\Scripts\conda.exe" goto no
:ask
echo:
echo Is Miniconda/Anaconda installed to "%miniconda_dir%"? (yes/no)
set INPUT=
set /P INPUT=Type 'y' or 'n': %=%
if /I "%INPUT%"=="y" goto yes
if /I "%INPUT%"=="n" goto no
echo Please type 'y' or 'n' only
goto ask
:no
echo:
echo Please type the path to Miniconda/Anaconda folder.
echo (you can drag'n'drop or paste it right here)
set /P miniconda_dir=Type the path (or 'x' to exit): %=%
set "_conda=%miniconda_dir%\Scripts\conda.exe"
if exist "%_conda%" goto ask
if "%miniconda_dir%" == "x" goto exit
echo "%_conda%" was not found!
goto no
:yes
:: </miniconda path confirmation>


:: <main>
set "this_script_dir=%~dp0"
cd /d %this_script_dir%

set PYTHONNOUSERSITE=1

set "_prefix=%miniconda_dir%\envs\%env%"

set "_conda=%miniconda_dir%\Scripts\conda.exe"
set "_activate=%miniconda_dir%\Scripts\activate.bat"
set "_deactivate=%miniconda_dir%\Scripts\deactivate.bat"
set "_pip=%_prefix%\Scripts\pip.exe"
set "_root_python=%miniconda_dir%\python.exe"

"%_conda%" env remove --name %env%
"%_root_python%" ".\_clear_global_channels.py" "%_conda%"
"%_conda%" env create --file %yaml%
:: Do not specify custom -p/--prefix path as
:: this might make shortcut creation fail.
:: If you need so specify custom prefix
:: first add %miniconda_dir%\Scripts to the PATH
:: and change %_prefix% accordingly.
call "%_activate%" %env%
:: </main>


:: -------- <custom commands after activate> ----
:: inverse order of channels:
"%_conda%" config --env --add channels conda-forge
"%_conda%" config --env --add channels defaults
"%_conda%" remove --force --yes pyqtgraph
"%_pip%" install git+https://github.com/pyqtgraph/pyqtgraph.git
"%_conda%" remove --force --yes qt pyqt sip
"%_pip%" install pyside2
:: -------- </custom commands after activate> ----


call "%_deactivate%"
pause
:exit
