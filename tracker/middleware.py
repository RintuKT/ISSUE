import datetime
from django.conf import settings
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin

class SessionTimeoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            return

        current_datetime = datetime.datetime.now()
        last_activity = request.session.get('last_activity')

        if last_activity:
            last_activity_datetime = datetime.datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S.%f')
            if (current_datetime - last_activity_datetime).seconds > settings.SESSION_COOKIE_AGE:
                logout(request)

        request.session['last_activity'] = str(current_datetime)
