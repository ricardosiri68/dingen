from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError


@view_config(route_name='entry', request_method="GET", renderer='../templates/show_entry.jinja2')
def entry_view(request):
    ''' Shows the full content of the entry
    '''

    return {}
