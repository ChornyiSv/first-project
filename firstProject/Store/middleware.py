import datetime

#клас для запису данних авторизації + дозволи для службових аккаунтів.
class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'login' in request.path and request.method == 'POST':
            status = 'Unknown'
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    status = 'Superuser'
                elif request.user.is_staff:
                    status = 'Staff'
                else:
                    status = 'User'

            with open('login_log.txt', 'a') as log_file:
                log_file.write(
                    f'{datetime.datetime.now()} - User {request.user.get_username()} logged in as {status}.\n')

        response = self.get_response(request)

        return response
