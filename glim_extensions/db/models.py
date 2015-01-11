import datetime

from . import Database as DB
from . import Orm
from . import Model

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text

# class Migration:
class Migration(Model):

	__tablename__ = 'glim_migrations'
	id = Column(String(255), primary_key=True)
	name = Column(String(255))
	created_at = Column(DateTime, default=datetime.datetime.utcnow)
	description = Column(Text)

	def __repr__(self):
		return "<Migration(id=%s, name=%s)>" % (self.id, self.name)
                             
