from os import listdir
from os.path import join as path_join

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from isavkorane.settings import MEDIA_ROOT

from main.support import *
from main.models import TypeBlock, Page
from main.forms import RegistrationForm, LoginForm


def get_pages(request, pagename):
    return [
        {"pagename": page.name, "active": page.name == pagename} for page in Page.objects.all()
    ]

def get_pages_context(request, pagename):
    context = get_base_context(request, pagename, "")
    context.update({
        'pages': get_pages(request, pagename),
        'TypeBlock': TypeBlock
    })
    return context

def index_page(request):
    return redirect("router", name="Русский")

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_pages_context(None, 'Регистация'))
        return context

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_pages_context(None, 'Логин'))
        return context

def router_pages(request, name):
    page = get_object_or_404(Page, name=name)
    context = get_pages_context(request, page.name)
    context['page'] = page
    return render(request, 'template_page.html', context)

def load_images_page(request):
    context = get_base_context(request, 'Загрузка картинок', 'load_images')
    if request.method == "POST" and request.FILES:
        for i, file in enumerate(request.FILES.getlist("files"), start=1):
            name = file.name
            # from django.core.files.storage import FileSystemStorage
            # fs = FileSystemStorage()
            # fmt = name[name.rindex(".")+1:]
            # fs.save(f'{request.POST.get("name")}/{i}.{fmt}', file)

            # get file: FileSystemStorage().url(filename)
        return redirect("index")
    return render(request, 'load_images.html', context)
