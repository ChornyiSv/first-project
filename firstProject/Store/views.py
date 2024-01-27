from datetime import datetime

from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .decorators import admin_or_staff
import Store.models
from Store.models import CreateProduct
from Store.forms import CreateProductForm, LoginForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# функція для формування пагінації
def paginate_queryset(request, queryset, items_per_page=6, page_request_var='page'):
    paginator = Paginator(queryset, items_per_page)
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    return paginated_queryset, paginator.num_pages, page_request_var

# для повернення користувача в залежності від його прав
def back_main(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('store:admin_main_page')
    else:
        return redirect('store:user_main_page')

# треба створити профіль
def profile(request):
    context = {

    }
    return render(request, 'profile.html', context)

# головна сторінка користувача
@login_required
def user_main_page(request):
    products = CreateProduct.objects.all()

    query = request.GET.get('q')

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    paginated_products, num_pages, page_request_var = paginate_queryset(request, products)

    context = {
        'title': 'Home page',
        'products_list': paginated_products,
        'num_pages': num_pages,
        'page_request_var': page_request_var
    }

    return render(request, 'user_main_page.html', context)

# головна сторінка адміністратора
@admin_or_staff
@login_required
def admin_main_page(request):
    products = CreateProduct.objects.all()

    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    paginated_products, num_page, page_request_var = paginate_queryset(request, products)

    context = {
        'title': 'Admin page',
        'products_list': paginated_products,
        'num_page': num_page,
        'page_request_var': page_request_var
    }
    return render(request, 'admin_main_page.html', context)


# потрібно доробити картку закуп
def shopping_cart(request):
    context = {

    }
    return render(request, 'shopping_cart.html', context)

# реєстрація акаунта через фронтенд
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully for {user.username}!')
            return redirect('store:login')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'registration.html', context)

# логування
def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return redirect('store:admin_main_page')
        else:
            print('Start login')
            messages.success(request, f'Welcome, {request.user.username}!')
            return redirect('store:user_main_page')
    else:
        print('Start login')
        if request.method == 'POST':
            form = LoginForm(request.POST)
            print('Before form.is_valid()')
            if form.is_valid():
                print('After form.is_valid()')
                username = form.cleaned_data['login']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome, {user.username}!')
                    if user.is_superuser or user.is_staff:
                        return redirect('store:admin_main_page')
                    else:
                        return redirect('store:user_main_page')
                else:
                    messages.error(request, 'Your username and password didn\'t match. Please try again.')

        else:
            form = LoginForm()

    context = {'form': form}
    return render(request, 'registration/login.html', context)

# потрібно доробити підтвердження замовлення
def confirm_order(request):
    context = {

    }
    return render(request, 'confirm_order.html', context)

# створення продукту через фронтенд
@admin_or_staff
def create_product(request):
    form = CreateProductForm(request.POST or None,
                             request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        image_url = instance.image.url
        messages.success(request, 'Product is created successfully!')
        messages.info(request, '<a href="http://127.0.0.1:8000/store/create_product/">Створити новий продукт</a>',
                      extra_tags='html_safe')
        messages.info(request,
                      '<a href="http://127.0.0.1:8000/store/admin_main_page/">Повернутися</a> на головну стоірнку',
                      extra_tags='html_safe')
        messages.info(request, f'<a href="{image_url}">Переглянути картинку</a>',
                      extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': 'Create product',
        'form': form,
        'action': 'Create'
    }
    return render(request, 'create_product.html', context)

# функція огляду продукту
def product_detail(request, id=None):
    instance = get_object_or_404(CreateProduct, id=id)
    context = {
        'title': 'Product detail',
        'product': instance
    }
    return render(request, 'product_detail.html', context)

#  функція оновлення продукту
@admin_or_staff
def update_product(request, id=None):
    instance = get_object_or_404(CreateProduct, id=id)
    form = CreateProductForm(request.POST or None,
                             request.FILES or None,
                             instance=instance)
    if form.is_valid():
        if form.has_changed():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Product is updated successfully!')
            messages.info(request, '<a href="http://127.0.0.1:8000/store/create_product/">Створити новий продукт</a>',
                          extra_tags='html_safe')
            messages.info(request,
                          '<a href="http://127.0.0.1:8000/store/admin_main_page/">Повернутися</a> на головну стоірнку',
                          extra_tags='html_safe')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            # Відобразити повідомлення про помилку, коли форма недійсна
            messages.error(request, 'Ви не внесли зміни у продукт.')
            return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': 'Update product',
        'form': form,
        'action': 'Update'
    }
    return render(request, 'create_product.html', context)

# категорії продуктів
def category(request, topic=None):
    instance = get_object_or_404(CreateProduct, topic=topic)
    context = {
        'title': f'Category {topic}',
        'object': instance
    }
    return render(request, 'category.html', context)

# категорія телефонів
def phones(request):
    products = CreateProduct.objects.all()

    query = request.GET.get('q')

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        'title': 'Phones',
        'products_list': products
    }
    return render(request, 'phones.html', context)

# категорія компютерів
def laptops(request):
    products = CreateProduct.objects.all()
    query = request.GET.get('q')

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        'title': 'Laptops',
        'products_list': products
    }
    return render(request, 'laptops.html', context)

# категорія навушників
def earphones(request):
    products = CreateProduct.objects.all()

    query = request.GET.get('q')

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        'title': 'Earphones',
        'products_list': products
    }
    return render(request, 'earphones.html', context)

# функція для видалення продукту
@admin_or_staff
def product_delete(request, id=None):
    instance = get_object_or_404(CreateProduct, id=id)
    instance.delete()
    return redirect('store:admin_main_page')

# треба додати  main_page з вибором логування або реєстрації
