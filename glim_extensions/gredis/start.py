from ext.gredis import Redis

def before(config):
	Redis.register(config)