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
    config.add_route('tag', '/tag/{tag_id}/{slug}.html')

    # CONTENT MANAGEMENT
    # config.add_route('profile', '/d/{username}')
    # # action=create|edit|delete
    # config.add_route('profile_entries', '/d/{username}/entries/{action}')
    #
    # # moderation: disable|enable|delete -> entries, users and tags
    # config.add_route('moderate', '/mod/{controller}/{action}')
