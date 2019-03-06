# QT_CONF = """[Paths]
# Prefix = {0}
# Binaries = {0}
# Headers = {1}
# 
# """


def ready():
    """
    Creates desktop shortcuts to enaml-video-app
    via shortcutter: https://github.com/kiwi0fruit/shortcutter
    and deletes qt.conf
    """
    import sys
    import os
    from os import path as p
    from shortcutter import ShortCutter

    error_log = sys.stderr

    sc = ShortCutter(error_log=error_log)
    if sys.platform == 'darwin':
        sc.create_desktop_shortcut('enaml-video-appw')
    else:
        sc.create_desktop_shortcut('enaml-video-app')
    sc.create_shortcut_to_env_terminal(menu=False)

    qt_conf = p.join(p.dirname(sys.executable), 'qt.conf')
    try:
        os.remove(qt_conf)
    except Exception as e:
        if p.isfile(qt_conf):
            print(e, file=error_log)
    # try:
    #     pyside_module = p.join(p.dirname(p.dirname(__file__)), 'PySide2')
    #     pyside_include = p.join(pyside_module, 'include', 'PySide2')
    #     print(QT_CONF.format(pyside_module, pyside_include), file=open(qt_conf, 'w', encoding="utf-8"))
    # except Exception as e:
    #     print(e, file=error_log)
