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


@view_config(
    route_name='profile_action',
    request_method='GET',
    match_param="action=edit",
    renderer='../templates/users/edit_profile.jinja2'
)
def edit_profile_view(request):
    """
    show the form to edit the user profile
    """
    return {}
