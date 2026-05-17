from django.shortcuts import render, get_object_or_404
from .models import Category, Post

def home(request):

    featured_post = Post.objects.filter(
        is_featured=True,
        is_published=True
    ).order_by('-created_at').first()
    business_featured = (
        Post.objects
        .filter(category__category_name__iexact="Travel")
        .order_by("-created_at")
        .first()
 )
    tech_post = (
        Post.objects
        .filter(category__category_name__iexact="tech")
        .order_by("-created_at")
        .first()
    )

    design_post = (
        Post.objects
        .filter(category__category_name__iexact="design")
        .order_by("-created_at")
        .first()
    )

    latest_post = (
        Post.objects
        .filter(category__category_name__iexact="latest")
        .order_by("-created_at")
        .first()
    )
    latest_picks = (
        Post.objects
        .order_by("-created_at")[:6]
    )

    if featured_post is None:
        featured_post = Post.objects.filter(is_published=True).order_by('-created_at').first()

    # ✅ Trending posts (latest posts)
    trending_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    latest_posts = Post.objects.order_by('-created_at')[:4]

    
    context = {
        'featured_post': featured_post,
        'trending_posts': trending_posts,
        'latest_posts': latest_posts,
        "business_featured": business_featured,
         "tech_post": tech_post,
        "design_post": design_post,
        "latest_post": latest_post,
        "latest_picks": latest_picks,
    }

    return render(request, 'blog/home.html', context)

def contact(request):
    return render(request, 'blog/contact.html')


def write_for_us(request):
    return render(request, 'blog/write-for-us.html')
    
def category(request, slug):
    category = get_object_or_404(Category, category_name__iexact=slug)
    posts = Post.objects.filter(category=category, is_published=True)

    return render(request, 'blog/category.html', {
        'category': category,
        'posts': posts
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, "blog/post_detail.html", {"post": post})
