import pyclbr

from . import Database
from . import Orm

from glim.utils import import_module
from sqlalchemy import exc

from models import Migration

class Migration(object):

    description = ''

    def __init__(self, db, orm):
        self.db = db
        self.orm = orm

    def run(self):
        pass

    def rollback(self):
        pass

class MigrationAdapter(object):

    def __init__(self, db, orm, migrations_mstr):
        self.db = db
        self.orm = orm
        self.migrations_mstr = migrations_mstr
        self.migrations_module = import_module(migrations_mstr, pass_errors=True)
        self.migrations = []
        self.retrieve_migrations()
        
    def retrieve_migrations(self):
        if self.migrations_module is not None:
            class_names = pyclbr.readmodule(self.migrations_mstr).keys()

            for name in class_names:
                if name != 'Migration' and 'Migration' in name:
                    cobject = getattr(self.migrations_module, name)
                    self.migrations.append(cobject)

    def dispatch(self, name, action='run'):
        for migration in self.migrations:
            if migration.__name__ == name:
                mig = migration(self.db, self.orm)
                action = getattr(mig, action)
                try:
                    action()
                    return True, mig.description
                except exc.SQLAlchemyError as e:
                    print e
                    return False, mig.description

        return None, ''

