@for %%F in ("%~dp0..") do set "pyexedir=%%~fxF"
@start "Enaml video app" /min "%pyexedir%\python.exe" -m enaml_video_app
