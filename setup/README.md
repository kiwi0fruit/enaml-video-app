# Install

1. Download video [Cosmos Laundromat](https://cloud.blender.org/p/cosmos-laundromat/55f35f7f2beb3300960bb077),
   place it on the desktop and rename to `cosmos_laundromat.mp4`  
   (**OR** you can copy and rename any other `*.mp4` video)

2. Download this [`setup`](./) folder.

3. Install [Miniconda3](https://conda.io/miniconda.html)
  (this instruction is for Python 3.6). I suggest
  installing to default location and not adding Miniconda
  to the PATH unless you have a reason - the app starts
  nicely via shortcut to be created.
    * on Windows installation is straight-forward,
    * [Linux install instruction](https://conda.io/docs/user-guide/install/linux.html)
      (open folder with downloaded Miniconda in the terminal before running the command),
    * [macOS install instruction](https://conda.io/docs/user-guide/install/macos.html).

4. Create conda environment with the app (**on Windows**):  

    - run `install.bat` in this folder.  

      > If on error then the script will close (this shouldn't
      > happen normally). To debug press `start`, type `cmd`,
      > press enter - you will launch a command prompt. Then
      > drag'n'drop `install.bat` script into the cmd window,
      > press enter.

5. Create conda environment with the app (**on Linux/macOS**):

    - open *this folder* in terminal,
    - type `. ./install`, enter,  

      >  **or**  

    - open terminal,
    - type dot (`.`), type space (` `),
    - drag'n'drop `install` script to the terminal, enter  


## Uninstall

If you need to uninstall environment - run terminal with
activated root conda environment. Then type:

    conda remove --name enaml_video_app --all
    conda env remove --name enaml_video_app

Sometimes conda environment is not deleted but renamed and placed to special trash folder inside root Miniconda installation. It's out of action this way but still takes disk space. You may need to delete it via `conda clean --help`. Manually deleting may break your conda installation.


## Reinstall

If you need to reinstall the app (this would be with latest packages) simply run installation again: it will delete the appropriate environment first.

*Save this folder somewhere in case you would like to reinstall it in future*.
