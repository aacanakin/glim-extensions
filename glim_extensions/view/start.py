from view import ViewFacade as View

# extension loader
def before(config):
	View.register(config)