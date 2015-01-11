from glim.core import Facade
from glim.ext import Extension
from glim import Log

import redis

class GredisExtension(Extension):

	def __init__(self, config):
		self.config = config
		self.active = 'default'
		self.connections = {}

		for k, config in self.config.items():
			try:
				self.connections[k] = self.connect(config)
			except Exception as e:
				Log.error(e)

	def __getattr__(self, attr):
		try:
			return getattr(self.connections[self.active], attr)
		except redis.RedisError as e:
			Log.error(e)
			return None

	def connection(self, key = None):
		if key:
			self.active = key
		else:
			self.active = 'default'
		return 

	def connect(self, config):
		try:
			connection = redis.StrictRedis(
				host = config['host'],
				port = config['port'],
				db = config['db'])

			connection.ping()
			return connection

		except redis.RedisError, e:
			Log.error(e)
			return None

class Redis(Facade):
	accessor = GredisExtension
