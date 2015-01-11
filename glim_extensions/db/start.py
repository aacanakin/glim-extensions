import traceback

from glim.utils import empty
from glim import Log

from . import Database, Orm


# extension loader
def before(config):
	try:
		Database.register(config)
		Orm.register(Database.engines)
	except Exception as e:
		Log.error(traceback.format_exc())
