"""
routes configuration module
"""


def includeme(config):
    """
    module inclusion function to manage the route configuration
    """
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('page', '/{action}.html')
    config.add_route('search', '/search')
    config.add_route('entry', '/entry/{entry_id}/{slug}.html')
