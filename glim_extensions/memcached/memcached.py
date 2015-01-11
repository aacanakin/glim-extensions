from glim.core import Facade
from glim.ext import Extension
from glim import Log

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
		except MemcacheError as e:
			Log.error(e)

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

		except MemcacheError as e:
			Log.error(e)

class Cache(Facade):
	accessor = MemcachedExtension
