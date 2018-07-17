"""
blog views definitions
"""
# from pyramid.response import Response
from pyramid.view import view_config
from pyramid.response import Response
from dingen_pyramid.models import Entry
from dingen_pyramid.serializers.blog import EntrySchema

# from sqlalchemy.exc import DBAPIError


@view_config(
    route_name='api_collection',
    match_param=('scope=blog', 'endpoint=entries'),
    request_method="GET",
)
def entries_ep(request):
    ''' show a list of entries
    '''

    entries = request.dbsession.query(Entry).all()
    entry_schema = EntrySchema(many=True)
    return Response(text=entry_schema.dumps(entries).data, content_type="application/json")

#@view_config(
#    route_name='tag',
#    request_method="GET",
#    renderer='../templates/tag_results.jinja2'
#)
#def tag_view(request):
#    """
#    Shows the entries related to a single tag
#    """
#    return {}
#
#
#@view_config(
#    route_name='profile_entries',
#    match_param=('action=create', 'entry=_'),
#    request_method='GET',
#    renderer='../templates/entries/create.jinja2'
#)
#def create_entry_view(request):
#    """
#    shows create a new entry form
#    """
#    return {}
#
#
#@view_config(
#    route_name='profile_entries',
#    match_param='action=edit',
#    request_method='GET',
#    renderer='../templates/entries/edit.jinja2'
#)
#def edit_entry_view(request):
#    """
#    shows the edit entry form
#    """
#    return {}
