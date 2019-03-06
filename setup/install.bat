@echo off
set "here=%~dp0"
set run=call "%here%\setup\path-run.bat"
set call=call "%here%\setup\path-call.bat"

:: <custom vars>
call "%here%\env\pre.bat"
:: </custom vars>


:: <miniconda path confirmation>
set "prefix=%UserProfile%\Miniconda3"
If not exist "%prefix%\Scripts\conda.exe" goto no
:ask
echo:
echo Is Miniconda/Anaconda installed to "%prefix%"? (yes/no)
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
set /P prefix=Type the path (or 'x' to exit): %=%
set "conda=%prefix%\Scripts\conda.exe"
if exist "%conda%" goto ask
if "%prefix%" == "x" goto exit
echo "%conda%" was not found!
goto no
:yes

set "_cnd=%conda%"
:: </miniconda path confirmation>


set PYTHONNOUSERSITE=1
set "PATH=%prefix%\Scripts;%prefix%\condabin;%PATH%"

%call% activate.bat base
"%prefix%\python.exe" "%here%\setup\clear_global_channels.py" "%_cnd%"

%run% conda.exe remove -n "%env%" --all
%run% conda.exe env remove --name "%env%"
%run% conda.exe update conda
%run% conda.exe env create --file "%here%\env\%yaml%"

%call% conda.bat deactivate
%call% activate.bat "%env%"


:: <custom commands after activate>
cd /d "%here%\env"
call "%here%\env\post.bat"
:: </custom commands after activate>

%call% conda.bat deactivate
pause
:exit
