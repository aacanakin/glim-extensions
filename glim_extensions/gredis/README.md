glim-redis - a redis extension for glim framework
=================================================

gredis is a glim framework extension for bringing up redis features to
glim. It uses https://github.com/andymccurdy/redis-py which is the most
popular redis library for python.

Installation
------------
- Clone the repo, move gredis folder into ext
- Remove `.git` directory if exists
- install `redis` dependancy
```
$ pip install redis
```

Configuration
-------------
- Append gredis dependancy to extensions in your config file;
- Add the following config to the extensions config;
```python
config = {
	'extensions' : {
		'gredis' : {
			'default' : {
				'host' : 'localhost',
				'port' : '6379',
				'db'   : 0
			}
			# add a new dict for connecting multiple redis
			# servers
		}
	},
	# ...
}
```

Here `default` is used for connection aliasing. Gredis can handle
multiple connections.

- Start your web server and that's it!

Usage
-----
```python
from ext.gredis.gredis import Redis

# performs operations in default connection
Redis.set('foo', 'bar')
Redis.set('foo', 'bar')

# performs operations in aliased connection
Redis.connection('connection-name').set('foo', 'bar')
```
