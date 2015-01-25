jslint - javascript linting extension for glim framework
========================================================

Installation
------------
- install jslint from npm
```
$ npm install -g jslint
```

Configuration
-------------
- Add the following config to the extensions config;
```python
config = {
	'extensions' : {
		'jslint': {
            'source': os.path.join(paths.APP_PATH, 'assets/js'),
        }
    },
	# ...
}
```

Roadmap
-------
- Autolint after file changes
- Show lint errors on served page
