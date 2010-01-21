# -*- coding: utf-8 -*-

import sys

def full_path ( relpath ):
	"""
	Translates a relative path to a full path.

	Doesn't work right in the interactive prompt
	"""
	return sys.path[0] + '/' + relpath

class Day:
	def __init__ ( self ):
		return

class Reminder:
	"""
	Defines a reminder.
	"""
	def __init__ ( self, path=None ):
		self.name = 'UNDEFINED'
		self.text = 'UNDEFINED'
		self.exceptions = []
		self.days = []

		if None != yaml:
			self.load_from_file( path )

	def load_from_file ( self, path ):
		# TODO: Load XML
		self.name = raw['reminder']['name']
		self.text = raw['reminder']['text']
		for day in raw['reminder']['days']:
			if 'monday' == day.lower():
			elif 'tuesday' == day.lower():
			elif 'wednesday' == day.lower():
			elif 'thursday' == day.lower():
			elif 'friday' == day.lower():
			elif 'saturday' == day.lower():
			elif 'sunday' == day.lower():

if __name__ == "__main__":

	reminders = {}

	import os

	for root, dirs, files in os.walk( full_path( 'reminders/on/' ) ):
			for file in files:
				if '.xml' == file[-4:]:
					reminders[file[-4:]] = Reminder( root + file )