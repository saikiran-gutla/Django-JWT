"""
This is a custom authentication file, we need to override the authenticate method
Implemented using the rest framework authentication
"""
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication):
    """
    Need to call them in the views in the authentication classes.
    Make a request as : {localhost}/api?username=sai
    """

    def authenticate(self, request):
        # from the URL , username is retrieved and checks for user is present or not
        user_name = request.GET.get('username')
        if user_name is None:
            return None
        try:
            user = User.objects.get(username=user_name)
        except user.DoesNotExist:
            raise AuthenticationFailed('Provided Credentials are not valid. Please Provide Valid Credentials'
                                       )
        return (user, None)


class CustomTokenAuthentication(BaseAuthentication):
    """
    Need to call them in the views in the authentication classes.
    Make a request as : {localhost}/api?username=sai&key=a12asd22aad
    """

    def authenticate(self, request):
        user_name = request.GET.get('username')
        token_key = request.get('key')
        if user_name is None or token_key is None:
            return None
        c1 = len(token_key) == 7
        c2 = token_key[0] == user_name[-1].lower()
        try:
            user = User.objects.get(username=user_name)
        except user.DoesNotExist:
            raise AuthenticationFailed('User Not found with the provided USER ID')
        if c1 and c2:
            return (user, None)
        raise AuthenticationFailed('Provided Key is Invalid , Please provide a valid Key')
