@set "script_dir=%~dp0"
@cd "%script_dir%"
@cd ..
@start "Enaml video app" /min ".\python.exe" -m enaml_video_app

