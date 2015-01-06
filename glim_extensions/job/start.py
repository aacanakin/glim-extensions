from ext.job.queue import JobQueue
from ext.job.job import JobSerializer
from ext.gredis.gredis import Redis
from glim.facades import Log

# extension loader
def before(config):
	JobQueue.boot(config, Redis._get(), serializer=JobSerializer())