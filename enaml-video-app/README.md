# Build instructions

Start app via `enaml-video-app` executable. `enaml-video-app-ready` CLI creates desktop shortcuts to app executable and to terminal with activated environment via [shortcutter](https://github.com/kiwi0fruit/shortcutter).

First:

    conda install conda-build "python>=3.6"

On Windows additionally install [Git Bash](https://git-scm.com/downloads).

To run the script open Bash terminal, then type <code>. </code> (dot with space), then
drag and drop the script to the Bash terminal (the script will change CWD itself), press enter.

* open terminal with activated environment,
* run `build` script,
* copy python module from `dist/` whenever you want.

you also should have python>=3.6 available to the `build` script in the activated env.

Outputs of building can be found in the `./dist/noarch`

To create pypi package use `build_pypi` script.

**Hint**: easily create shortcut to activated 
environment via Shortcutter:

* cross-platform installation:

      conda install -c defaults -c conda-forge shortcutter
      shortcutter --terminal

* To start Git Bash on windows (installed to default location) type `%b%` in the terminal created via Shortcutter
