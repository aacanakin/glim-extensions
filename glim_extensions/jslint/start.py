from . import JSLint
from glim import Log

# extension loader
def before(config):
    try:
    	JSLint.register(config)
    	JSLint.check()
    except Exception as e:
		Log.error(e)
