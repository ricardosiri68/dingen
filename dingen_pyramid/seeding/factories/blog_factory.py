"""
random test data factory models
"""
from . import generate
import factory
import random
from dingen_pyramid.models import Entry, Tag, Visit


class EntryFactory(factory.Factory):
    """
    Factory for faking the data of a Entry model mapper
    """

    class Meta:
        model = Entry

    class Params:
        use_tags = []

    title = factory.Faker('sentence', nb_words=5)
    body_markdown = factory.Faker('paragraph', nb_sentences=40)
    body_html = factory.LazyAttribute(lambda obj: obj.body_markdown)
    created_at = factory.Faker('date_object')
    updated_at = factory.Faker('date_object')

    @factory.lazy_attribute
    def tags(self):
        return random.sample(self.use_tags, 5)

    @factory.lazy_attribute
    def visits(self):
        return list(generate(VisitFactory, (10, 500)))


class TagFactory(factory.Factory):
    """
    Factory for faking the data of a Tag model mapper
    """

    class Meta:
        model = Tag

    text_data = factory.Sequence(lambda n: 'taggy_%s' % n)


class VisitFactory(factory.Factory):
    """
    Factory for faking the date of the a Visit model mapper
    """

    class Meta:
        model = Visit

    created_at = factory.Faker('date_object')
