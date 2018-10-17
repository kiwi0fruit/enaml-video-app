@for %%F in ("%~dp0..") do set "pyexe=%%~fxF\python.exe"
@"%pyexe%" -m enaml_video_app --main
