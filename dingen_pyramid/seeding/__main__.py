"""
main seeder runner
"""
import os
import configparser
import argparse

from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from dingen_pyramid.models.meta import Base
from . import blog_seeder


# CONST
SEEDERS = [
    blog_seeder
]
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

parser = argparse.ArgumentParser(description="Database seeding module")
parser.add_argument(
    'settings_file',
    nargs="+")
parser.add_argument(
    '-s',
    '--seeder',
    dest="seeder",
    help="Select the seeder module")


def get_session(settings):
    """
    create a clean sqlalchemy session
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.bind = engine
    Base.metadata.create_all()
    Session = sessionmaker(bind=engine)

    return Session()


def get_settings(args):
    """
    read the settings .ini file (develop or production)
    """
    config = configparser.SafeConfigParser({'here': PROJECT_PATH})
    settings_file, *_ = args.settings_file
    config.read(settings_file)

    return dict(config.items('app:main'))


def run_seeders(args):
    """
    run all seeders modules allowed on the list: seeders
    """

    settings = get_settings(args)

    session = get_session(settings)

    if not args.seeder:

        for seeder_module in SEEDERS:
            seeder_module.seed(session)

    elif args.seeder in globals():
        globals()[args.seeder].seed(session)

    session.commit()


run_seeders(parser.parse_args())
