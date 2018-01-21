"""
search view module
"""
from pyramid.view import view_config


@view_config(
    route_name='search',
    request_method="GET",
    renderer='../templates/search_results.jinja2')
def search_view(request):
    ''' Search action and rendering search result view
    '''
    advance_search = request.GET.get('advanced', 'off') == 'on'

    return {
        'advance_search': advance_search
    }
