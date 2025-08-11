from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import BlogPost, Category
from .forms import BlogPostForm

def home(request):
    return render(request, 'blog/home.html', {
        'categories': Category.objects.all(),
        'recent_posts': BlogPost.objects.filter(is_draft=False)[:6],
    })

@login_required
def dashboard(request):
    if request.user.is_doctor():
        return render(request, 'blog/doctor_dashboard.html', {
            'my_posts': BlogPost.objects.filter(author=request.user)
        })
    return render(request, 'blog/patient_dashboard.html', {
        'categories': Category.objects.all()
    })

@login_required
def create_blog(request):
    if not request.user.is_doctor():
        messages.error(request, 'Only doctors can create posts.')
        return redirect('dashboard')
    form = BlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, 'Post saved!')
        return redirect('dashboard')
    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def edit_blog(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    form = BlogPostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Post updated!')
        return redirect('dashboard')
    return render(request, 'blog/create_blog.html', {'form': form, 'blog_post': post})

def blog_list(request):
    qs = BlogPost.objects.filter(is_draft=False)
    category_id  = request.GET.get('category')
    search       = request.GET.get('search')
    if category_id: qs = qs.filter(category_id=category_id)
    if search:
        qs = qs.filter(Q(title__icontains=search)|Q(summary__icontains=search)|Q(content__icontains=search))
    page_obj = Paginator(qs, 6).get_page(request.GET.get('page'))
    return render(request, 'blog/blog_list.html', {
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'selected_category': category_id,
        'search_query': search,
    })

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, is_draft=False)
    related = BlogPost.objects.filter(category=post.category, is_draft=False).exclude(pk=pk)[:3]
    return render(request, 'blog/blog_detail.html', {'blog_post': post, 'related_posts': related})

def category_posts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    page_obj = Paginator(BlogPost.objects.filter(category=category, is_draft=False), 6)\
                 .get_page(request.GET.get('page'))
    return render(request, 'blog/category_posts.html', {'category': category, 'page_obj': page_obj})
