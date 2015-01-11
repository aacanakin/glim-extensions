from . import View

# extension loader
def before(config):
	View.register(config)