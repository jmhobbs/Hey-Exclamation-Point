# -*- coding: utf-8 -*-

import yaml
import sys

def full_path ( relpath ):
	"""
	Translates a relative path to a full path.

	Doesn't work right in the interactive prompt
	"""
	return sys.path[0] + '/' + relpath

class Reminder:
	"""
	Defines a reminder.
	"""
	def __init__ ( self ):
		self.name = 'UNDEFINED'
		self.exceptions = []
		self.days = []

	def load_from_file ( self, path ):
		# Open file, load yaml
		f = open( root + '/' + file )
		raw = yaml.load( f )
		f.close()

if __name__ == "__main__":
	import os
	for root, dirs, files in os.walk( full_path( 'reminders/' ) ):
			for file in files: