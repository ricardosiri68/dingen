"""
user views definitions
"""
from pyramid.view import view_config


@view_config(
    route_name='login',
    request_method='GET',
    renderer='../templates/login.jinja2'
)
def login_view(request):
    """
    Show the login form
    """
    return {}


@view_config(
    route_name='profile',
    request_method='GET',
    renderer='../templates/users/show_profile.jinja2'
)
def user_profile_view(request):
    """
    shows user profile
    """
    return {}
