"""
blog models definitions
"""
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    DateTime
)

from .meta import Base
from . import export_model


@export_model
class Entry(Base):
    ''' Mapper for all the blog entries
    '''

    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)

    title = Column(String(200), nullable=False)
    body_markdown = Column(Text, nullable=False)
    body_html = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    update_at = Column(DateTime, nullable=False)


Index('entries_index', Entry.title, unique=True, mysql_length=255)
