import logging

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

from .models import User

log = logging.getLogger(__name__)


class Auth(authentication.BaseAuthentication):
    # def authenticate(self, request):
    #     username = request.data.get('username', None)
    #     password = request.data.get('password', None)
    #
    #     if not username or not password:
    #         raise exceptions.AuthenticationFailed(_('No credentials provided.'))
    #
    #     credentials = {
    #         get_user_model().USERNAME_FIELD: username,
    #         'password': password
    #     }
    #
    #     user = authenticate(**credentials)
    #
    #     if user is None:
    #         raise exceptions.AuthenticationFailed(_('Invalid username/password.'))
    #
    #     if not user.is_active:
    #         raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
    #
    #     return user, None  # authentication successful
    #
    def authenticate(self, username, password):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            log.error("user with login %s does not exists " % username)
            return None
        except Exception as e:
            log.error(repr(e))
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(sys_id=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            log.error("user with %(user_id)d not found")
            return None
