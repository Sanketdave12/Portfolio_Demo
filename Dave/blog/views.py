from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import *
from .form import *
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# class BaseView(TemplateView):
#     template_name = "base.html"

class HomeView(TemplateView):
    template_name = "blog/home.html"


def expertiseView(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/expertise/digital_marketing.html', context)
# class ExpertiseView(TemplateView):
#     template_name = "blog/expertise/digital_marketing.html"


def agencyView(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/agency.html', context)
# class AgencyView(TemplateView):
#     model = Blog
#     post = Blog.objects.all()
#     template_name = "blog/agency.html"


def portfolioView(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/portfolio/photography.html', context)
# class PortfolioView(TemplateView):
#     template_name = "blog/portfolio/photography.html"

def productsView(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/products.html', context)
# class PortfolioView(TemplateView):
#     template_name = "blog/portfolio/photography.html"

class ConnectView(TemplateView):
    template_name = "blog/letsconnect.html"


# Expertise sub page views
class ExpertiseSubView(TemplateView):
    model = Contact
    template_name = "blog/expertise/digital_marketing.html"


# class ExpertiseSub1View(TemplateView):
#     model = Contact
#     template_name = "blog/expertise/ui_ux.html"


def ExpertiseSub1View(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/expertise/ui_ux.html', context)


# class ExpertiseSub2View(TemplateView):
#     model = Contact
#     template_name = "blog/expertise/gaming.html"


def ExpertiseSub2View(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/expertise/gaming.html', context)


# class ExpertiseSub3View(TemplateView):
#     model = Contact
#     template_name = "blog/expertise/seo.html"


def ExpertiseSub3View(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/expertise/seo.html', context)


# class ExpertiseSub4View(TemplateView):
#     model = Contact
#     template_name = "blog/expertise/logo_creator.html"


def ExpertiseSub4View(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/expertise/logo_creator.html', context)


# class ExpertiseSub5View(TemplateView):
#     model = Contact
#     template_name = "blog/expertise/web_development.html"


def ExpertiseSub5View(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/expertise/web_development.html', context)


# PORTFOLIO SUB VIEWS
class PortfolioSub1View(TemplateView):
    template_name = "blog/portfolio/photography.html"


# class PortfolioSub2View(TemplateView):
#     template_name = "blog/portfolio/logo_design.html"


def PortfolioSub2View(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/portfolio/logo_design.html', context)


# class PortfolioSub3View(TemplateView):
#     template_name = "blog/portfolio/web_design.html"

def PortfolioSub3View(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/portfolio/web_design.html', context)

# class PortfolioSub4View(TemplateView):
#     template_name = "blog/portfolio/vfx.html"


def PortfolioSub4View(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/portfolio/vfx.html', context)

# class PortfolioSub5View(TemplateView):
#     template_name = "blog/portfolio/animations.html"


def PortfolioSub5View(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/portfolio/animations.html', context)

# class PortfolioSub6View(TemplateView):
#     template_name = "blog/portfolio/xyz.html"


def PortfolioSub6View(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/portfolio/xyz.html', context)


def BlogViews(request):
    post = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 6)
    if request.method == 'POST':
        subscriberemail = request.POST.get('subscriberemail')
        if len(subscriberemail) < 8:
            messages.error(request, 'Please fill the form correctly.')
        else:
            messages.success(
                request, 'Your message has been successfully sent.')
            subscribenews = SubscribeNewsletter(
                subscriberemail=subscriberemail)
            subscribenews.save()
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def BlogDetail(request, slug):
    posts = Blog.objects.all()
    post = get_object_or_404(Blog, Slug=slug)
    # Tag = get_object_or_404(Blog, Slug = slug)
    # Tags = Blog.Tag.similar_objects()
    comments = post.comments.filter(Active=True, Parent__isnull=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            Parent_obj = None
            try:
                Parent_id = int(request.POST.get('Parent_id'))
            except:
                Parent_id = None
            if Parent_id:
                Parent_obj = Comment.objects.get(id=Parent_id)
                if Parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.Parent = Parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.Post = post
            new_comment.save()
            return redirect('blog:detail', slug)

    else:
        comment_form = CommentForm()

    if request.method == 'POST':
        subscriberemail = request.POST.get('subscriberemail')
        if len(subscriberemail) < 8:
            messages.error(request, 'Please fill the form correctly.')
        else:
            messages.success(
                request, 'Your message has been successfully sent.')
            subscribenews = SubscribeNewsletter(
                subscriberemail=subscriberemail)
            subscribenews.save()
    context = {
        'posts': posts,
        'blog': post,
        'comments': comments,
        'comment_form': comment_form,
        # 'Tag':Tag,
        # 'Tags':Tags
    }
    return render(request, 'blog/blogdetail.html', context)

# def baseBlog(request):
#     post = Blog.objects.all()
#     context = {
#         'post' : post
#     }
#     return render(request,'base.html',context)


def contactUs(request):
    post = Blog.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        url = request.POST['url']
        if len(email) < 3 or len(phone) < 10 or len(message) < 4:
            messages.error(request, 'Please fill the form correctly.')
        else:
            messages.success(
                request, 'Your message has been successfully sent.')
        contact = Contact(name=name, email=email,
                          phone_no=phone, message=message)
        contact.save()
        return HttpResponseRedirect(url)
    context = {
        'post': post
    }
    return HttpResponseRedirect(url)


def letsConnect(request):
    print("Hello")
    connect = LetsConnect.objects.all()
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        lc_email = request.POST['lc_email']
        lc_phone = request.POST['lc_phone']
        lc_message = request.POST['lc_message']
        if len(lc_email) < 3 or len(lc_phone) < 10 or len(lc_message) < 4:
            messages.error(request, 'Please fill the form correctly.')
        else:
            messages.success(
                request, 'Your message has been successfully sent.')
        letsconnect = LetsConnect(firstname=firstname, lastname=lastname,
                                  lc_email=lc_email, lc_phone_no=lc_phone, lc_message=lc_message)
        letsconnect.save()
        return redirect('/letsconnect')
    context = {
        'connect': connect
    }
    return render(request, './blog/letsconnect.html', context)


def searchPost(request):
    context = {}
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    post = Blog.objects.filter(
        Q(Title__icontains=query) | Q(
            Content__icontains=query) | Q(Tag__icontains=query)
    ).distinct()

    if post.count == 0:
        messages.warning(request, 'NO search Results')

    parms = {
        'post': post,
        'title': f'{query}',
    }

    if request.method == 'POST':
        subscriberemail = request.POST.get('subscriberemail')
        if len(subscriberemail) < 8:
            messages.error(request, 'Please fill the form correctly.')
        else:
            messages.success(
                request, 'Your message has been successfully sent.')
            subscribenews = SubscribeNewsletter(
                subscriberemail=subscriberemail)
            subscribenews.save()
    return render(request, './blog/searchpost.html', parms)


# def searchPost(request):
#     posts = Blog.objects.all()
#     page = request.GET.get('page', 1)
#     paginator = Paginator(posts, 6)
#     context = {}
#     if request.GET:
#         query = request.GET.get('q', '')
#         context['query'] = str(query)

#     post = Blog.objects.filter(
#         Q(Title__icontains=query) | Q(
#             Content__icontains=query) | Q(Tag__icontains=query)
#     ).distinct()

#     if post.count == 0:
#         messages.warning(request, 'NO search Results')

#     try:
#         post = paginator.page(page)
#     except PageNotAnInteger:
#         post = paginator.page(1)
#     except EmptyPage:
#         post = paginator.page(paginator.num_pages)

#     parms = {
#         'post': post,
#         'posts': posts,
#         'title': f'{query}',
#     }
#     if request.method == 'POST':
#         subscriberemail = request.POST.get('subscriberemail')
#         if len(subscriberemail) < 8:
#             messages.error(request, 'Please fill the form correctly.')
#         else:
#             messages.success(
#                 request, 'Your message has been successfully sent.')
#             subscribenews = SubscribeNewsletter(
#                 subscriberemail=subscriberemail)
#             subscribenews.save()
#     return render(request, './blog/searchpost.html', parms)
