from setuptools import setup, find_packages


setup(
    name='enaml-video-app',
    version='0.1.0',

    description=('Enaml video application.'),
    url='https://github.com/kiwi0fruit/enaml-video-app',
    author='kiwi0fruit',
    author_email='peter.zagubisalo@gmail.com',
    license='MIT',

    packages=find_packages(),

    install_requires=['setuptools'],
    
    include_package_data=True,

    scripts=[
        'scripts/enaml-video-app.bat',
        'scripts/enaml-video-app',
    ],
)
