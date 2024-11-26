from rest_framework.decorators import api_view
from rest_framework.response import Response

from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    '''
    Displays a simple root page for the API.
    '''
    return Response({
        "message":
        "Hello. I am Aperta's API. I was coded with Django REST framework."
    })


@api_view(['POST'])
def logout_route(request):
    '''
    Handles JWT cookies upon logout. Expiry date in the past,
    ensuring cookies immediately deactivated.
    '''
    response = Response()

    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )

    return response
