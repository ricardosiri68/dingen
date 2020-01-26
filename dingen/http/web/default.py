"""
default views module
"""
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError


@view_config(
    route_name='home',
    request_method='GET',
    renderer='../templates/home.jinja2'
)
@view_config(
    route_name='page',
    request_method='GET',
    match_param="action=home",
    renderer='../templates/home.jinja2'
)
def home_view(request):
    ''' home view
    '''
    try:
        # query = request.dbsession.query(MyModel)
        # one = query.filter(MyModel.name == 'one').first()
        pass
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {}


@view_config(
    route_name='page',
    request_method='GET',
    match_param="action=trending",
    renderer='../templates/trending.jinja2'
)
def trending_view(request):
    ''' trending view
    '''
    return {}


@view_config(
    route_name='page',
    request_method='GET',
    match_param="action=about_us",
    renderer='../templates/about_us.jinja2'
)
def about_us_view(request):
    ''' about us view
    '''
    return {}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_dingen_pyramid_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
