@echo off
set "this_script_dir=%~dp0"

:: <custom vars>
call "%this_script_dir%\env_pre.bat"
:: </custom vars>


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
cd /d %this_script_dir%

set PYTHONNOUSERSITE=1

set "_prefix=%miniconda_dir%\envs\%env%"

set "_conda=%miniconda_dir%\Scripts\conda.exe"
set "_activate=%miniconda_dir%\Scripts\activate.bat"
set "_deactivate=%miniconda_dir%\Scripts\deactivate.bat"
set "_pip=%_prefix%\Scripts\pip.exe"
set "_root_python=%miniconda_dir%\python.exe"
set "_python=%_prefix%\python.exe"

"%_conda%" env remove --name %env%
"%_root_python%" "%this_script_dir%\_clear_global_channels.py" "%_conda%"
"%_conda%" env create --file %yaml%
:: Do not specify custom -p/--prefix path as
:: this might make shortcut creation fail.
:: If you need so specify custom prefix
:: first add %miniconda_dir%\Scripts to the PATH
:: and change %_prefix% accordingly.
call "%_activate%" %env%
:: </main>


:: <custom commands after activate>
call "%this_script_dir%\env_post.bat"
:: </custom commands after activate>


call "%_deactivate%"
pause
:exit
