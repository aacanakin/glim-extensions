from . import Less
from glim import Log

# extension loader
def before(config):
    try:
    	Less.register(config)
    	Less.compile()
    except Exception as e:
		Log.error(e)
