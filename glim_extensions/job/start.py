import traceback

from queue import JobQueue
from job import JobSerializer
from glim_extensions.gredis.gredis import Redis
from glim import Log

# extension loader
def before(config):
	try:
		JobQueue.boot(config, Redis.instance, serializer=JobSerializer())
	except Exception as e:
		Log.error(traceback.format_exc())