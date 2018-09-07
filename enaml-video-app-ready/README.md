# app-ready

Creates desktop shortcuts to app executable and to terminal with activated environment via [shortcutter](https://github.com/kiwi0fruit/shortcutter).
Logs shortcut creation errors to
`~/enaml_video_app_install_error_log.txt`.


# Build instructions

* open terminal with activated environment,
* on Linux / macOS type <code>. </code> (dot, space),
* drag and drop `build.bat`
  (`build` on Linux / macOS) to the terminal window
  and press enter,
* copy python module from `dist/` whenever you want.


Hint: easily create shortcut to activated 
environment via Shortcutter:

* windows only preparation:

      conda install pywin32

* cross-platform installation:

      pip install shortcutter
      shortcutter --terminal
