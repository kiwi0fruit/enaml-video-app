@for %%F in ("%~dp0..") do set "pyexedir=%%~fxF"
@"%pyexedir%\python.exe" -m enaml_video_app
