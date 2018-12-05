"""
delete all channels from global .condarc except 'defaults'
first argument is the conda path
"""
import sys
import subprocess

conda = sys.argv[1]
out = subprocess.Popen([conda, 'config', '--get', 'channels'],
                       stdout=subprocess.PIPE).stdout.read().decode('utf-8')
channels = [s.strip("'") for s in out.split() if s[0] == s[-1] == "'"]
for channel in (c for c in channels if c != 'defaults'):
    subprocess.call([conda, 'config', '--remove', 'channels', channel])
