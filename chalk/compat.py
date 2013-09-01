from django.conf import settings

# Safe User import for Django < 1.5
try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
else:
    User = get_user_model()


# Safe version of settings.AUTH_USER_MODEL for Django < 1.5
auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
