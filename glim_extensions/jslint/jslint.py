import subprocess
import os

from glim.core import Facade
from glim import Log
from glim import paths


DEFAULT_CONFIG = {
	'source': os.path.join(paths.APP_PATH, 'assets/js'),
}

class JSLint(object):
	def __init__(self, config):
		self.config = DEFAULT_CONFIG
		for key, value in config.items():
			self.config[key] = value
		Log.debug("config")

	def check(self):
		try:
			command = 'jslint'
			arguments = '%s%s' % (self.config['source'], '/*')

			Log.debug("command: %s" % command)
			Log.debug("arguments: %s" % arguments)
			# find ./public/javascripts/ -name '*.js' -print0 | xargs -0 jslint
			cmd = "find %s -name '*.js' -print0 | xargs -0 jslint" % self.config['source']

			# cmd = '%s %s' % (command, arguments)
			Log.debug("cmd: %s" % cmd)
			p = subprocess.Popen(cmd,
								 stdout=subprocess.PIPE,
								 stderr=subprocess.PIPE,
								 shell=True)
			out, err = p.communicate()
			Log.info("Linting javascript..")
			Log.write(out)
			Log.error(err)
		except Exception as e:
			Log.error(e)

class JSLintFacade(Facade):
	accessor = JSLint
