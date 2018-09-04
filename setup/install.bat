@echo off
set "miniconda_dir=%UserProfile%\Miniconda3"


:: Begin Miniconda path confirmation
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
set "conda=%miniconda_dir%\Scripts\conda.exe"
if exist "%conda%" goto ask
if "%miniconda_dir%" == "x" goto exit
echo "%conda%" was not found!
goto no
:yes
:: End Miniconda path confirmation


set "this_script_dir=%~dp0"
cd /d %this_script_dir%

set PYTHONNOUSERSITE=1
"%miniconda_dir%\Scripts\conda.exe" env create --file env_win.yaml


pause
:exit
:: Do not specify custom -p/--prefix path
:: this might make shortcut creation fail.
:: If you need so specify custim prefix
:: first add %miniconda_dir%\Scripts to the PATH.
