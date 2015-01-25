import subprocess
import os

from glim.core import Facade
from glim import Log
from glim import paths

OPTION_MAP = {
	'nojs': '--no-js',
	'lint': '--lint',
	'verbose': '--verbose',
	'units': '-sm=on',
	'compress': '--compress'
}

DEFAULT_CONFIG = {
	'source': os.path.join(paths.APP_PATH, 'assets/less/main.less'),
	'destination': os.path.join(paths.APP_PATH, 'assets/css/main.css'),
	'options': [
		'lint',
		'units',
		'verbose'
	]
}

class Less(object):
	def __init__(self, config):
		self.config = DEFAULT_CONFIG
		for key, value in config.items():
			self.config[key] = value

		# Log.info("config")
		# Log.info(self.config)

	def compile(self):
		source = self.config['source']
		destination = self.config['destination']
		options = self.config['options']

		try:

			options_string = ''
			for option in options:
				options_string += '%s ' % OPTION_MAP[option]
			options_string = options_string.rstrip()

			command = 'lessc'
			arguments = '%s %s > %s' % (options_string, source, destination)

			# Log.debug("command: %s" % command)
			# Log.debug("arguments: %s" % arguments)

			cmd = '%s %s' % (command, arguments)
			p = subprocess.Popen(cmd,
								 stdout=subprocess.PIPE,
								 stderr=subprocess.PIPE,
								 shell=True)
			out, err = p.communicate()
			Log.info("Compiling LESS source..")
		except Exception as e:
			Log.error(e)

class LessFacade(Facade):
	accessor = Less
