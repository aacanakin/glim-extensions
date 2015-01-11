from glim.core import Facade
from glim import Log

class RedisQueue:

	def __init__(self, config, redis, serializer):
		self.config = config
		self.redis = redis
		self.serializer = serializer
		self.queues = {}

		for key, config in self.config.items():
			self.queues[key] = {}
			self.queues[key]['redis'] = self.redis.connection(config['redis'])
			self.queues[key]['jobs']  = config['jobs']
			self.queues[key]['failed']  = config['failed']

		self.active = self.queues['default']

	# sets active queue connection given key
	def connection(self, name = 'default'):
		self.active = self.queues[name]
		return self

	# generic push for queueing jobs given redis list name
	def _push(self, job, list):
		return self.active['redis'].rpush(list, self.serializer.serialize(job))

	# generic pop for popping jobs given redis list name
	def _pop(self, list):
		raw_job = self.active['redis'].lpop(list)
		if raw_job:
			job_id, job = self.serializer.deserialize(raw_job)
			if job:
				return job
			else:
				return None
		else:
			return None

	# pushes a job on jobs list on active queue connection
	def push(self, job):
		return self._push(job, self.active['jobs'])
	
	# pushes a job on failed list on active queue connection
	def push_failed(self, job):
		return self._push(job, self.active['failed'])

	# pops a job on jobs list on active queue connection
	def pop(self):
		return self._pop(self.active['jobs'])

	# pops a failed job on failed jobs list on active queue connection
	def pop_failed(self):
		return self._pop(self.active['failed'])

class JobQueue(Facade):
	accessor = RedisQueue
