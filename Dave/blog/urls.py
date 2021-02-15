from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView
from .views import *

app_name = 'blog'
urlpatterns = [

    # Main Navbar
    path('contact-me/', contactUs, name='contact'),
    # path('blog/subscribe/',subscribeNews, name='subscribenews'),
    path('', HomeView.as_view(), name='home'),
    # path('expertise/digital_marketing',views.ExpertiseView.as_view(), name='expertise'),
    path('expertise/digital_marketing/', expertiseView, name='expertise'),
    # path('agency/',AgencyView.as_view(),name='agency'),
    path('agency/', agencyView, name='agency'),
    # path('portfolio/photography', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/photography/', portfolioView, name='portfolio'),
    path('products/', productsView, name='products'),
    path('blog/', BlogViews, name='post'),
    path('connect/', ConnectView.as_view(), name='connect'),
    path('letsconnect/', letsConnect, name='letsconnect'),
    # path('letsconnect/',letsConnect,name='letsconnect'),


    #  ExpertiseSubViews
    path('expertise/digital_marketing/',
         ExpertiseSubView.as_view(), name='digital_marketing'),
    path('expertise/ui_ux/', ExpertiseSub1View, name='ui_ux'),
    path('expertise/gaming/', ExpertiseSub2View, name='gamming'),
    path('expertise/seo/', ExpertiseSub3View, name='seo'),
    path('expertise/logo_creator/',
         ExpertiseSub4View, name='logo_creator'),
    path('expertise/web_development/',
         ExpertiseSub5View, name='web_developer'),

    # PortfolioSubViews
    path('portfolio/photography/', PortfolioSub1View.as_view(), name='photography'),
    path('portfolio/logo_design/', PortfolioSub2View, name='logo_design'),
    path('portfolio/web_design/', PortfolioSub3View, name='web_design'),
    path('portfolio/vfx/', PortfolioSub4View, name='vfx'),
    path('portfolio/animations/', PortfolioSub5View, name='animations'),
    path('portfolio/xyz/', PortfolioSub6View, name='xyz'),






    path('blog/<slug:slug>/', BlogDetail, name='detail'),
    path('search/', searchPost, name='search'),

]

# url(r'^ckeditor/', include('ckeditor_uploader.urls')),