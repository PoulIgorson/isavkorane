"""isavkorane URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeView

from isavkorane import settings
from main import views, admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('_/get_auth/', admin.api_get_auth, name='admin_get_auth'),
    path('_/add_page/', admin.add_page_page, name='admin_add_page'),
    path('_/pages/<int:page_id>/new_block/', admin.add_block_page, name='admin_add_block'),
    path('_/pages/delete_block/', admin.delete_block_page, name='admin_delete_block'),
    path('_/pages/block_set_text', admin.block_set_text_page, name='admin_block_set_text'),
    path('_/pages/block_set_image', admin.block_set_image_page, name='admin_block_set_image'),

    path('accounts/password_change/', PasswordChangeView.as_view(
        template_name='registration/password_change.html'), name='password_change'),
    path('accounts/login/', views.LoginView.as_view(
        template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', views.RegistrationView.as_view(
        template_name='registration/registration.html'), name='registration'),

    path('load_images/', views.load_images_page, name='load_images'),
    path('', views.index_page, name='index'),
    path('pages/<str:name>/', views.router_pages, name='router'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
