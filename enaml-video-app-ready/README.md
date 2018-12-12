# app-ready

Creates desktop shortcuts to app executable and to terminal with activated environment via [shortcutter](https://github.com/kiwi0fruit/shortcutter).
Logs shortcut creation errors to
`~/enaml_video_app_install_error_log.txt`.


# Build instructions

To run the script open Bash terminal, then type <code>. </code> (dot with space), then
drag and drop the script to the Bash terminal (the script will change CWD itself), press enter.

* open terminal with activated environment,
* run `build` script,
* copy python module from `dist/` whenever you want.


Hint: easily create shortcut to activated 
environment via Shortcutter:

* windows only preparation:

      conda install pywin32

* cross-platform installation:

      pip install shortcutter
      shortcutter --terminal

* To start Bash on windows type `%b%` in the terminal created via Shortcutter
