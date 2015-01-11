import os
import traceback

from glim import paths
from glim import Log
from glim import Config
from glim.utils import copytree
from glim.command import Command

class InitCommand(Command):
	name = 'init'
	description = 'initializes views.py given views extension configuration'

	def configure(self):
		pass

	def run(self):
		try:
			proto_path = os.path.join(os.path.dirname(__file__), 'prototype')
			Log.info("Creating views folder..")
			copytree(proto_path, paths.APP_PATH)
			Log.info('Done')
		except Exception as e:
			Log.error(traceback.format_exc())