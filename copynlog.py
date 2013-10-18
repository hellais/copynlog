"""
# CopyNLog

by Art. <art@fuffa.org>

This code is released under [WTFPL](http://www.wtfpl.net/)

I choose Freedom, so you can do what the fuck you want with this code :)
"""


import sys
import os
from os.path import join as pj
from os.path import basename

import shutil

class Disker(object):
    def __init__(self, srcs, dst):
        self.srcs = srcs
        self.dst = dst
        self.log_file = basename(dst) + '.md'

    def set_target_drive(self):
        """
        XXX
        """
        pass

    def copy_directory(self):
        """
        XXX
        """
        pass

    def list_directory(self):
        """
        XXX
        """
        pass

    def write_to_log(self):
        """
        XXX
        """
        pass

    def copy(self):
        with open(self.log_file, 'w+') as f:
            f.write('# %s\n' % self.log_file.replace('.md', ''))
        for src in self.srcs:
            print "* Copying %s in %s" % (src, dst)
            album_name = basename(src)
            try:
                if os.path.isdir(src):
                    shutil.copytree(src, pj(dst, album_name))
                elif os.path.exists(src):
                    shutil.copy(src, pj(dst, album_name))
                else:
                    raise Exception("No such file or directory!")
                with open(self.log_file, 'a+') as f:
                    f.write("  * %s\n" % album_name)
            except Exception, e:
                print e
                print "[!] Failed to copy %s into %s" % (src, pj(dst, album_name))

description = 'Assists you in moving Music to an SD card and keep a log of it.'

srcs = []
for arg in sys.argv[1:-1]:
  srcs.append(arg)

dst = sys.argv[-1]

disker = Disker(srcs, dst)
disker.copy()
