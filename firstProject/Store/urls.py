from django.urls import path
from Store.views import (profile, user_main_page, shopping_cart, login_view, register, admin_main_page, confirm_order, phones,
                         laptops, earphones, product_detail, category, create_product, update_product, product_delete,
                         back_main)
from django.contrib.auth.views import LogoutView


app_name = 'store'

urlpatterns = [
    path('', login_view, name='home_page'),

    path('register/', register, name='register'), # реєстрація юзера
    path('login/', login_view, name='login'), # сторінка на якій юзер чи адмін може залогуватися
    path('logout/', LogoutView.as_view(next_page='store:login'), name='logout'),
    path('admin_main_page/', admin_main_page, name='admin_main_page'), #сторінка адміна де він може додавати товар
    path('user_main_page/', user_main_page, name='user_main_page'), # сторінка з якої можна перейти в профіль, кошик, та одразу має бути видно лист продуктів, і можливість пошуку (по назві)
    path('profile/', profile, name='profile'), # профіль юзера
    path('create_product/', create_product, name='create_product'),
    path('update_product/<int:id>', update_product, name='update_product'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),# звичайний кошик в якому можна побачити доданий товар, поміняти кількість, видалити товар, переглянути вартість кошика
    path('confirm_order/', confirm_order, name='confirm_order'),# підтвердження замовлення
    path('phones/', phones, name='phones'),
    path('laptops/', laptops, name='laptops'),
    path('earphones/', earphones, name='earphones'),
    path('category/<str:topic>/', category, name='category'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('product_delete/<int:id>/', product_delete, name='product_delete'),
    path('back_main/', back_main, name='back_main')

]