from setuptools import setup, find_packages


setup(
    name='app',
    version='0.1.0',

    description=('App. Imports `test` function, has `app` CLI executable that prints ' +
                 'PATH to show that the app runs in the activated environment.'),
    url='https://github.com/me/app',
    author='My Name',
    author_email='me@mail.com',
    license='Proprietary',
    # it's a sample setup.py. Actually this file's license is the same as the whole repo's

    packages=find_packages(),

    install_requires=['setuptools'],
    
    # add non .py files from MANIFEST.in:
    include_package_data=True,

    # create cross-platform executables:
    entry_points={
        'console_scripts': [
            'app=app.app:cli',
        ],
    },

    scripts=[
        'scripts/myscript.bat',
        'scripts/myscript',
    ],
)
