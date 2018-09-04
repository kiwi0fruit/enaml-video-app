from setuptools import setup
from setuptools.command.install import install

LOG_FILE = 'enaml_video_app_install_error_log.txt'


class PostInstallCommand(install):
    def run(self):
        """
        Creates desktop shortcuts to app exec. and app module folder
        via shortcutter: https://github.com/kiwi0fruit/shortcutter
        Logs shortcut creation errors to ~/$LOG_FILE
        """
        import enaml_video_app  # make sure the main module is installed
        import io
        import os
        from os import path as p
        import inspect
        from shortcutter import ShortCutter
        from sys import executable as python_executable

        error_log = io.StringIO()

        sc = ShortCutter(error_log=error_log)
        sc.create_desktop_shortcut('enaml-video-app')
        sc.create_shortcut_to_env_terminal(menu=False)
        try:
            os.remove(p.join(p.dirname(python_executable), 'qt.conf'))
        except Exception as e:
            print(e, file=error_log)

        print(error_log.getvalue(), file=open(p.join(p.expanduser('~'), LOG_FILE),
                                              'w', encoding="utf-8"))
        error_log.close()

        # must have:
        install.run(self)


setup(
    name='enaml-video-app-ready',
    version='0.1.0',
    cmdclass={'install': PostInstallCommand},

    description='Shortcuts for Enaml video application.',
    url='https://github.com/kiwi0fruit/enaml-video-app',
    author='kiwi0fruit',
    author_email='peter.zagubisalo@gmail.com',
    license='MIT',
)
