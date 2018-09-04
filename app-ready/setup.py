from setuptools import setup
from setuptools.command.install import install


class PostInstallCommand(install):
    def run(self):
        """
        Creates desktop shortcuts to app exec. and app module folder
        via shortcutter: https://github.com/kiwi0fruit/shortcutter
        Logs shortcut creation errors to ~/app_install_error_log.txt
        """
        import app  # make sure the main module is installed
        import io
        from os import path as p
        import inspect
        from shortcutter import ShortCutter

        # Find module without importing:
        # from importlib.util import find_spec as find_module
        # find_module('app').origin

        error_log = io.StringIO()

        sc = ShortCutter(error_log=error_log)
        sc.create_desktop_shortcut('app')
        app_dir = p.dirname(inspect.getfile(app))
        sc.create_desktop_shortcut(p.join(app_dir, 'extra'), 'app_extra_dir')
        sc.create_shortcut_to_env_terminal(menu=False)

        print(error_log.getvalue(), file=open(p.join(p.expanduser('~'),
                                                     'app_install_error_log.txt'),
                                              'w', encoding="utf-8"))
        error_log.close()

        # must have:
        install.run(self)


setup(
    name='app-ready',
    version='0.1.0',
    cmdclass={'install': PostInstallCommand},

    description='Shortcuts for App.',
    url='https://github.com/me/app-ready',
    author='My Name',
    author_email='me@mail.com',
    license='Proprietary',
    # it's a sample setup.py. Actually this file's license is the same as the whole repo's

    # install_requires=['app'],  # Do not add such deps!
    # Because 'app' is already on pypi and setup.py will attempt to install from there.
    # And it's not the 'app' that we need.
)
