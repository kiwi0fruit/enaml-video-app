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

4. If on **Windows** install [Git Bash](https://git-scm.com/downloads).
  Install instructions are straight-forward.

5. Create conda environment with the app:

    - open *this folder* in terminal (if on Windows:
      right mouse click in the white space of the current folder then "Git Bash Here"),
    - type `. ./install`, enter,  

      >  **or**  

    - open terminal (Git Bash if on Windows),
    - type dot (`.`), type space (` `),
    - drag'n'drop `install` script to the terminal, enter  


## Uninstall

If you need to uninstall environment - run terminal with
activated root conda environment. Then type:

    conda remove --name enaml_video_app --all
    conda env remove --name enaml_video_app

Sometimes conda environment is not deleted but renamed and placed to special trash
folder inside root Miniconda installation. It's out of action this way but still takes
disk space. You may need to delete it via `conda clean --help`. Manually deleting may
break your conda installation.


## Reinstall

If you need to reinstall the app (this would be with latest packages) simply run
installation again: it will delete the appropriate environment first.

*Save this folder somewhere in case you would like to reinstall it in future*.
