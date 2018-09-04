# Installation

0. Download video [Cosmos Laundromat](https://cloud.blender.org/p/cosmos-laundromat/),
   place it on the desktop (~\Desktop in case of Unix)
   and rename to `cosmos_laundromat.mp4`

1. Install [Miniconda3](https://conda.io/miniconda.html)
  (this instruction is for Python 3.6). I suggest
  installing to default location and not adding Miniconda
  to the PATH unless you have a reason - the app starts
  nicely via shortcut to be created.
    * on Windows installation is straight-forward,
    * [Linux install instruction](https://conda.io/docs/user-guide/install/linux.html)
      (open folder with downloaded Miniconda in the terminal before running the command),
    * [macOS install instruction](https://conda.io/docs/user-guide/install/macos.html).

2. Install [Git](https://git-scm.com/downloads).
  Install instructions are straight-forward. Another
  option on macOS is to install the Xcode Command
  Line Tools. On Mavericks (10.9) or above you can
  do this simply by trying to run git from the
  Terminal the very first time.

       git --version

    If you don’t have it installed already, it will
    prompt you to install it.

3. Create conda environment with the app (**on Windows**):  

    - run `install.bat` in this folder.  

      > If on error then the script will close (this shouldn't
      > happen normally). To debug press `start`, type `cmd`,
      > press enter - you will launch a command prompt. Then
      > drag'n'drop `install.bat` script into the cmd window,
      > press enter.

5. Create conda environment with the app (**on Linux/macOS**):

    - open this folder in terminal,
    - type `. ./install`,  

      >  **or**  

    - open terminal,
    - type dot (`.`), type space (` `),
    - drag'n'drop `install` script to the terminal, enter  

6. If you need to uninstall environment - run terminal with
  activated root conda environment. Then type:

       conda env remove --name enaml_video_app
