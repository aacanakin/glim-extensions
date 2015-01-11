view - jinja2 extension for glim framework
==========================================
This repo includes the necessary components to integrate jinja2 with glim framework.

Installation
------------
- install jinja2
```
$ pip install jinja2
```

Configuration
-------------
- Add the following config to the extensions config;
```python
config = {
	'extensions' : {
		'view': {
            'package': 'app.views' # folder name for rendering templates
        }
	},
	# ...
}
```

- Initialize view extension
```sh
$ glim view:init
# creates views folder on your application path
```

Usage
-----
- put your template into your views folder
```html
# views/hello.html
<html>
    <body>
    name: {{ user.name }}
    surname: {{ user.surname }}
    </body>
</html>
```

```python
# controllers.py
from glim_extensions.view import View

class BaseController(Controller):

    def hello(self):
    	return View.render('hello', user={
    		'name': 'Aras Can',
    		'surname': 	'Akin'
		})

```

- That's it!