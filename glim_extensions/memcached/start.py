from ext.memcached.memcached import Cache

def before(config):
	Cache.register(config)