@for %%F in ("%~dp0..") do set "pyexedir=%%~fxF"
@start "" "%pyexedir%\pythonw.exe" -m enaml_video_app
