from django.http import HttpResponse

#Декоратор для перевірки хто дає запит на функцію
def admin_or_staff(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("Access Denied")

    return wrapper

