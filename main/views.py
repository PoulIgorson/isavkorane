from os import listdir
from os.path import join as path_join
import tempfile

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from isavkorane.settings import MEDIA_ROOT
from main.support import *


def index_page(request):
    context = get_base_context(request, 'Главная', 'index')
    return redirect("russian")
    return render(request, 'index.html', context)

def load_images_page(request):
    context = get_base_context(request, 'Загрузка картинок', 'load_images')
    if request.method == "POST" and request.FILES:
        for i, file in enumerate(request.FILES.getlist("files"), start=1):
            name = file.name
            fs = FileSystemStorage()
            fmt = name[name.rindex(".")+1:]
            fs.save(f'{request.POST.get("name")}/{i}.{fmt}', file)

            # get file: FileSystemStorage().url(filename)
        return redirect("index")
    return render(request, 'load_images.html', context)

def russian_page(request):
    context = get_base_context(request, 'Русский', 'russian')
    context["header"] = "Коран об Исе"
    context["pages"] = list(map(lambda f: "Русский/"+f, listdir(path_join(MEDIA_ROOT, "Русский"))))
    return render(request, 'russian.html', context)
