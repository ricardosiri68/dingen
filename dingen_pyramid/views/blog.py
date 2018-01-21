"""
blog views definitions
"""
# from pyramid.response import Response
from pyramid.view import view_config

# from sqlalchemy.exc import DBAPIError


@view_config(
    route_name='entry',
    request_method="GET",
    renderer='../templates/entries/show.jinja2'
)
def entry_view(request):
    ''' Shows the full content of the entry
    '''

    return {}


@view_config(
    route_name='tag',
    request_method="GET",
    renderer='../templates/tag_results.jinja2'
)
def tag_view(request):
    """
    Shows the entries related to a single tag
    """
    return {}


@view_config(
    route_name='profile_entries',
    match_param=('action=create', 'entry=_'),
    request_method='GET',
    renderer='../templates/entries/create.jinja2'
)
def create_entry_view(request):
    """
    shows create a new entry form
    """
    return {}


@view_config(
    route_name='profile_entries',
    match_param='action=edit',
    request_method='GET',
    renderer='../templates/entries/edit.jinja2'
)
def edit_entry_view(request):
    """
    shows the edit entry form
    """
    return {}
