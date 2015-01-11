import uuid
import os

import glim.paths as paths
from glim import Config
from glim import Log
from glim.command import Command

from . import Database as DB
from . import Orm
from . import Model

from utils import touch
from models import Migration
from migration import MigrationAdapter

class InitCommand(Command):

    name = 'init'
    description = 'initialize the migrations module'

    def configure(self):
        pass

    def run(self):
        Log.info("Initilizing empty migrations file into app..")
        migrations_path = os.path.join(paths.APP_PATH, 'migrations.py')
        result = touch(migrations_path)
        Log.info("Creating glim_migrations table on db..")

        engine = DB.engine('default')
        Migration.metadata.create_all(engine)
        Log.info("Done.")

class SyncCommand(Command):

    name = 'sync'
    description = 'syncs all app models into database'

    def configure(self):
        self.add_argument('--name', help='enter model name to be synced', default=None)
        pass

    def run(self):
        default = Config.get('extensions.db.default')
        all = self.args.name is None
        if all:
            import app.models
            Log.info("Syncing models..")
            Model.metadata.create_all(DB.engine(default))
            Log.info("Done.")
        else:
            import app.models as models
            try:
                Log.info("Syncing %s model" % self.args.name)
                model = getattr(models, self.args.name)
                model.metadata.create_all(DB.engine(default))
            except Exception as e:
                Log.error(e)

class BaseCommand(Command):

    def configure(self):
        self.add_argument('--name', help='enter migration name (default migrates all)')
        self.migration_adapter = MigrationAdapter(DB._get(), Orm._get(), 'app.migrations')

    def can_migrate(self):
        pass

    def dispatch(self, name, rollback=False):
        if self.can_migrate(name):
            result = None
            description = ''
            if rollback:
                result, description = self.migration_adapter.dispatch(name, action='rollback')
            else:
                result, description = self.migration_adapter.dispatch(name, action='run')

            if result is True:
                if rollback:
                    migration = Orm.query(Migration).filter_by(name=name).first()
                    Log.info("Rolling back %s migration.." % name)
                    Orm.delete(migration)
                else:
                    migration = Migration(id=uuid.uuid4(), name=name, description=description)
                    Log.info("Migrating %s.." % name)
                    Orm.add(migration)

                # TODO: check if committed successfully
                Orm.commit()
                Log.info("Done.")

            elif result is None:
                Log.error("Migration %s doesn't exist" % name)
                exit()
            else:
                Log.error("Migration %s has failed to run!" % name)
                exit()
        else:
            if rollback:
                Log.warning("Migration %s doesn't exist" % name)
            else:
                Log.warning("Migration %s already migrated into rdb" % name)


class RunCommand(BaseCommand):

    name = 'run'
    description = 'run rdb migrations'

    def can_migrate(self, name):
        migration = Orm.query(Migration).filter_by(name=name).first()
        if migration is None:
            return True
        else:
            return False

    def run(self):
        name = None if not self.args.name else self.args.name
        all = name is None
        if all is True:
            for m in self.migration_adapter.migrations:
                name = m.__name__
                self.dispatch(name)
        else:
            self.dispatch(self.args.name)

class RollbackCommand(BaseCommand):

    name = 'rollback'
    description = 'rollback rdb migrations'

    def can_migrate(self, name):
        migration = Orm.query(Migration).filter_by(name=name).first()
        if migration is None:
            return False
        else:
            return True

    def run(self):
        name = None if not self.args.name else self.args.name
        all = name is None
        if all is True:
            migrations = Orm.query(Migration).order_by(Migration.created_at.desc()).all()
            for migration in migrations:
                self.dispatch(migration.name, rollback=True)
        else:
            self.dispatch(self.args.name, rollback=True)


