"""
Blog seeding modlue
"""
from .factories import blog_factory, generate

def seed(session):
    tags = list(generate(blog_factory.TagFactory, 50))
    entries = list(generate(
        blog_factory.EntryFactory,
        300,
        kwargs={'use_tags': tags}
    ))

    session.add_all(tags)
    # TODO: integrate 5 random tags on every Entry object
    # TODO: integrate 10-500 visits on every Entry object
    session.add_all(entries)
