glim-jobqueue - a redis jobqueue extension for glim framework
=============================================================

glim-jobqueue is a glim framework extension for bringing up jobqueue implementation to glim. It uses [glim-redis](https://github.com/aacanakin/glim-redis) extension for redis connection

Installation
------------
- Clone the repo, move job folder into ext folder
- Remove `.git` directory if exists

Configuration
-------------
- Append job configuration after gredis configuration in your config file;
```python
config = {
    'extensions' : {
        'gredis' : {
            'default' : {
                'host' : 'localhost',
                'port' : '6379',
                'db'   : 0
            }
        },
        'job' : {
            'default' : {
                'redis'  : 'default',
                'jobs'   : 'jobs',    # redis list name for jobs
                'failed' : 'failed',  # redis list name for failed jobs
            }
        },
    },
    # ...
}
```

Initializing Job Extension
--------------------------
```sh
$ glim job:init
# this will create a job.py on your app folder
```

Creating Jobs
-------------
```python
# jobs.py
from glim.facades import Log
from ext.job.job import Job

class HelloJob(Job):
    def run(self): # self.data is registered when a Job 
        if 'author' in self.data.keys():
            Log.info('hello %s' % self.data['author'])
        else:
            Log.info('hello glim!')

```

Producing Jobs
--------------
```python
from ext.job.queue import JobQueue
data = {
    'author' : 'Aras Can Akin'
}
JobQueue.push(HelloJob(data)) # returns True or False
JobQueue.push(HelloJob)
```

Consuming Jobs
--------------
```sh
$ glim job:consume --name jobs
# output
hello Aras Can Akin
hello
```

Failed Jobs
-----------
In jobqueue, you may want to emulate failed jobs. Therefore, there is an exception that job:consume command is looking for.
```python
# jobs.py
from glim.facades import Log
from ext.job.exception import FailedJobError
from ext.job.job import Job

class HelloJob(Job):
    def run(self):
        if 'author' in self.data.keys():
            Log.info('hello %s' % self.data['author'])
        else:
            raise FailedJobError()
```

In this example, when you push a job without `author`, the job will go to failed list in redis

Roadmap
-------
- the job system should work for many other message queue services like AWSQ, RabbitMQ, IronMQ, etc.
- command for flushing job queue