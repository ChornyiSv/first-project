# import http.client
#
# from django.contrib import admin
# from django.http import HttpResponse
# from django.urls import path
#
# def home_page(request):
#     return HttpResponse('<h1>test page</h1>')
# def main_page(request):
#     return HttpResponse('<h1>main page</h1>')
#
# def main_home_page(request):
#     return HttpResponse('<h1>main home page</h1>')
#
# class Main:
#
#     def __init__(self, url):
#         self.url = url
#
#     def func(self, request):
#         return HttpResponse(f'<h1>{self.url}</h1>')
#
#     def func_1(self, a, b):
#         return a + b
#     def func_2(self, arg: str):
#         print(arg.title())
#
# obj = Main('http://127.0.0.1:8000/sviat_page/')
# print(obj.url)
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('test/', home_page),
#     path('test/main/', main_page),
#     path('main_page/home/python/', main_home_page),
#     path('sviat_page/', obj.func)
# ]