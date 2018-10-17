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

    entry_points={
        'console_scripts': [
            'enaml-video-app=enaml_video_app.enaml_video:main',
        ],
    },

    scripts=[
        'scripts/enaml-video-appw',
    ],
)
