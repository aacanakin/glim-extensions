glim-memcached - memcached extension for glim
=============================================

memcached is a glim framework extension for bringing up memcached features to
glim. It uses [pinterest's memcache module](https://github.com/pinterest/pymemcache)

Installation
------------
- clone the repo inside ext folder
- install [pymemcache](https://github.com/pinterest/pymemcache)
- move memcached folder into ext
- remove `.git` directory if exists

Configuration
-------------
- Add the following config to the extensions config;
```python
config = {

    'extensions' : {
        'memcached' : {
            'default' : {
                'host' : 'localhost',
                'port' : 11211,
            }
            # add a new dict for connecting multiple redis
            # servers
        }
    },
    # ...
}
```

Here `default` is used for connection aliasing. Memcached can handle
multiple connections.

- Start your web server and that's it!

Usage
-----
```python
from ext.memcached.memcached import Cache

# performs operations in default connection
Cache.set('foo', 'bar')
Cache.get('foo')

# performs operations in aliased connection
Cache.connection('connection-name').set('foo', 'bar')
```