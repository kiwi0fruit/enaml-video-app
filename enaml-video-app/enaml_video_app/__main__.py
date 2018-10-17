from .enaml_video import main
import sys

if __name__ == '__main__':

    arg = sys.argv[1] if len(sys.argv) > 1 else ''

    if arg == '':
        main()
    elif arg == '--main':
        main()
    else:
        raise ValueError('Unsupported argument: ' + arg)
