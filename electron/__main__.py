#!/usr/bin/env python3

from __future__ import print_function
import sys

import modules
import util
from .util.logging import *

import argparse
import os
import PIL

class App():
    def __init__(self):
        # check if we were passed a command line argument
        parser = argparse.ArgumentParser(prog='UltraTrace')
        parser.add_argument('path', help='path (unique to a participant) where subdirectories contain raw data', default=None, nargs='?')
        args = parser.parse_args()

        # initialize modules
        self.Data = modules.Metadata( self, args.path )
        self.Control = modules.Control(self)
        self.Trace = modules.Trace(self)
        self.Dicom = modules.Dicom(self)
        self.Audio = modules.Playback(self)
        self.TextGrid = modules.TextGrid(self)
        self.Spectrogram = modules.Spectrogram(self)
        self.Search = modules.Search(self)

        self.filesUpdate()

if __name__ == '__main__':
	app = App()
	# app.mainloop()
	while True:
		try:
			app.mainloop()
			break
		except UnicodeDecodeError as e:
			error(e)