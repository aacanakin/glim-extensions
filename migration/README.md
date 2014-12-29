glim-migrations
===============

This repository is a glim framework extension for bringing up rdb migration implementation to glim. It uses various features of SQLAlchemy.

Installation
------------
- Clone the repo, move migration folder into ext folder
- Remove `.git` directory if exists

Configuration
-------------
```python
# app/config/<env>.py
config = {
    'extensions' : {
        'migration' : {
            'db' : 'default' # the connection alias
        }
    },

    'db' : {
        'default' : {
            'driver' : 'mysql',
            'host' : 'localhost',
            'schema' : 'test',
            'user' : 'root',
            'password' : ''
        }
    }

    # it is required to have at least one db connection
}
```

Initializing Migration Extension
--------------------------------
```sh
$ glim migration:init
# this will create a glim_migrations table using rdb connection
# also, it will create app/migrations.py file
```

Syncing models into db
----------------------
Suppose that you have the following model in your models;

```python
# app/models.py
from glim.db import Model
from sqlalchemy import Column, Integer, String

class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    fullname = Column(String(255))
    password = Column(String(255))
```

You can easily sync with db using following;

```sh
$ glim migration:sync --name User
# OR
$ glim:migration:sync # syncs all your db models
```

NOTE: This command will not sync if db table already exists.

Create a migration
------------------
```python
# app/migrations.py
from app.models import User
from ext.migration.migration import Migration

class AddUserMigration(Migration):

    description = 'creates a sample user in users table'

    def run(self):
        user = User(id=5, name='Aras')
        self.orm.add(user)
        self.orm.commit()
        return True

    def rollback(self):
        user = self.orm.query(User).filter_by(id=5).first()
        if user is not None:
            self.orm.delete(user)
            self.orm.commit()
```

To migrate this run the following;

```sh
$ glim migration:run --name AddUserMigration
# output
# Migrating AddUserMigration..
# Done.
```

Optionally, you can migrate all with the following command;
```sh
$ glim migration:run # migrates all defined migrations
```

This command will add a sample user & add a row into `glim_migrations` table.

Rollback a migration
--------------------
```sh
$ glim migration:rollback --name AddUserMigration
# output
# Rolling back AddUserMigration
# Done.
```

Optionally, you can rollback all migrations ordered by created_at desc;
```sh
$ glim migration:rollback # rollbacks all migrations
```

**NOTE: Do not change anything in the glim_migrations table manually if you don't want migration extension to crash.**
