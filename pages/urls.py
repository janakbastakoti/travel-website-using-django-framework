from django.urls import path
from . import views


urlpatterns = [
    path('contact',views.contact_page,name='contact'),
    path('blog',views.blog_page,name='blog'),
    path('about',views.about_page,name='about'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('account',views.account_page,name='account'),
    path('settings',views.settings_page,name='settings'),
    path('register',views.register_page,name='register'),
    path('addblog',views.addblog_page,name='addblog'),
]