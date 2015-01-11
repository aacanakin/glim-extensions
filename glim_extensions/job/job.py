import uuid
import pickle
import json

from glim import Log

class Job:

	def __init__(self, data = {}):
		self.id = self.generate_id()
		self.data = data

	# default run function
	def run(self):
		Log.info('running default job!')

	# generate time based uuid
	def generate_id(self):
		return uuid.uuid1().hex

	def __str__(self):
		return json.dumps({
			'id'     : self.id,
			'data'   : self.data,
			'object' : pickle.dumps(self)
		})

class JobSerializer:

	def serialize(self, job):
		job_string = '%s' % job
		return job_string

	def deserialize(self, job_string):
		raw_job = json.loads(job_string)
		try:
			job = pickle.loads(raw_job['object'])
		except Exception, e:
			Log.error(e)
			return None, None

		return job.id, job