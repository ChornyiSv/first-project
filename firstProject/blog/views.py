from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

def post_list(request):

    queryset = Post.objects.all()

    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    paginator = Paginator(queryset, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)


    context ={
        'title': 'Post list',
        'objects_list': queryset,
        'page_request_var': page_request_var
    }

    return render(request, 'post_list.html', context)

def post_create(request):

    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None,
                    request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Post is created successfully')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': 'Post create',
        'form': form
    }
    return render(request, 'post_create.html', context)

def post_detail(request, id=None):

    instance = get_object_or_404(Post, id=id)
    context = {
        'title': 'Post detail',
        'object': instance

    }

    return render(request, 'post_detail.html', context)

def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,
                    request.FILES or None,
                    instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, '<a href="#">Post</a> is updated successfully', extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': 'Post update',
        'form': form
    }

    return render(request, 'post_create.html', context)

def post_delete(request, id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect('blog:post_list')

def home_page(requesst):
    return HttpResponse('<h1 style="color: red;">Home page</h1>')

# http://127.0.0.1:8000/firstProject/