import os
import traceback

from glim.command import Command
from glim import Log

from queue import JobQueue
from exception import FailedJobError

import glim.paths as paths

class ConsumeCommand(Command):
	name = 'consume'
	description = 'consumes jobs given jobs list'

	def configure(self):
		self.add_argument('--name', help = 'enter jobs list name', default = 'jobs')

	def run(self):
		Log.info("Listening for jobs..")

		while(True):
			name = self.args.name
			job = JobQueue.pop()
			if job:
				try:
					job.run()
					Log.info('job %s is consumed' % job.id)
				except FailedJobError as e:
					Log.error(e)
					JobQueue.push_failed(job)
				except Exception as e:
					Log.error("An unknown exception has occured!!")
					Log.error(traceback.format_exc())
				

class ProduceCommand(Command):
	name = 'produce'
	description = 'produces a job given parameters and job name'

	def configure(self):
		pass

	def run(self):
		pass

class InitCommand(Command):
	name = 'init'
	description = 'initializes the jobs extension'

	def configure(self):
		self.add_argument('--name', help = 'enter jobs file name', default = 'jobs')

	# touches the jobs.py into app folder
	def run(self):
		jobs_path = os.path.join(paths.APP_PATH, '%s.py' % self.args.name)
		fhandle = open(jobs_path, 'a')
		try:
			os.utime(jobs_path, None)
			Log.info("app/jobs.py created successfully")
		except Exception as e:
			Log.error(e)
		finally:
			fhandle.close()


# class CreateCommand(Command):
# 	name = 'create'
# 	description = 'appends a job on your jobs file'

# 	def configure(self):
# 		self.add_argument('name', help = 'enter job name')

# 	# appends a new job given name
# 	def run(self):
# 		pass
