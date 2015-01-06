from glim.core import Facade
from glim.component import Extension
from glim.facades import Log

from pymemcache.client import Client, MemcacheError

class MemcachedExtension(Extension):
	def __init__(self, config):
		self.config = config
		self.active = 'default'
		self.connections = {}

		for key, config in self.config.items():
			self.connections[key] = self.connect(config)

	def __getattr__(self, attr):
		try:
			return getattr(self.connections[self.active], attr)
		except Exception, e:
			Log.error(e)
			return None

	def connection(self, key = None):
		if key:
			self.active = key
		else:
			self.active = 'default'

	def connect(self, config):
		try:
			connection = Client((
				config['host'], config['port']
			))

			return connection

		except Exception, e:
			Log.error(e)
			return None

class Cache(Facade):
	accessor = MemcachedExtension
