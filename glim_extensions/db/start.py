from glim.utils import empty
from db import Database, Orm


# extension loader
def before(config):
	if not empty('db', config):
		Database.register(config['db'])
		if not empty('orm', config):
			Orm.register(Database.engines)