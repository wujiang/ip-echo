from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='home.mako')
def home(request):
    return {
        "ip":
        request.remote_addr,
    }
