"""
blog models definitions
"""
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    DateTime,
    Table,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .meta import Base
from . import export_model


entries__tags_REL_TABLE = Table(
    'entries__tags',
    Base.metadata,

    Column('entry_id', Integer, ForeignKey('entries.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


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

    tags = relationship(
        'Tag',
        secondary=entries__tags_REL_TABLE,
        back_populates='entries'
    )
    visits = relationship('Visit', back_populates='entry')


@export_model
class Tag(Base):
    """
    Mapper for the entry tags
    """

    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    text_data = Column(String(64), nullable=False)  # a non space text: hashtag

    entries = relationship(
        'Entry',
        secondary=entries__tags_REL_TABLE,
        back_populates='tags'
    )


@export_model
class Visist(Base):
    """
    Mapper for the visit of a entry
    """

    __tablename__ = 'visits'

    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey('entries.id'), unique=True)
    created_at = Column(DateTime, nullable=False)


Index('entries_index', Entry.title, unique=False, mysql_length=255)
Index('tag_index', Tag.text_data, unique=True, mysql_length=64)
