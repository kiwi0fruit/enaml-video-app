"""
sets channels in global .condarc to 'defaults' only
"""
import sys
import subprocess

conda = sys.argv[1]
defaults = 'defaults'

out = subprocess.Popen([conda, 'config', '--get', 'channels'], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
channels = [s.strip("'") for s in out.split() if s[0] == s[-1] == "'"]
if channels:
    if not (defaults in channels):
        subprocess.call([conda, 'config', '--add', 'channels', defaults])
    for channel in (c for c in channels if c != defaults):
        subprocess.call([conda, 'config', '--remove', 'channels', channel])
