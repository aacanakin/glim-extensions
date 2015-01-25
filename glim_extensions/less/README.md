less - less css extension for glim framework
============================================

Installation
------------
- install less from npm
```
$ npm install -g less
```

Configuration
-------------
- Add the following config to the extensions config;
```python
config = {
	'extensions' : {
		'less': {
            'source': os.path.join(paths.APP_PATH, 'assets/less/app.less'),
            'destination': os.path.join(paths.APP_PATH, 'assets/css/app.css'),
            'options': [
                'compress',
                'lint',
                'nojs',
                'units'
            ]
        }
    },
	# ...
}
```

- The default configuration is the following;
```python
DEFAULT_CONFIG = {
    'source': os.path.join(paths.APP_PATH, 'assets/less/main.less'),
    'destination': os.path.join(paths.APP_PATH, 'assets/css/main.css'),
    'options': [
        'lint',
        'units',
        'verbose'
    ]
}
```

Usage
-----
- put a main.less file and add some styles
- add main.css import to your html sources
- start the web server
```html
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/assets/css/main.css">
    </head>
</html>
```

Roadmap
-------
- Autocompile after file changes
