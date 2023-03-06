from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from main.support import *

from main.models import TypeBlock, Block, Page
from main.forms import CreatePageForm


@login_required
def add_page_page(request):
    context = get_base_context(request, 'Добавление страницы', 'add_page')
    form = CreatePageForm()
    if request.method == "POST":
        form = CreatePageForm(request.POST)
        if form.is_valid():
            if not Page.objects.filter(name=form.cleaned_data["name"]).count():
                print(Page.objects.create(
                    name=form.cleaned_data["name"],
                ))
                return redirect('router', name=form.cleaned_data["name"])
            else:
                form.errors["name"] = ["Такая страница уже существует"]
    context['form'] = form
    return render(request, "admin/add_page.html", context)


def add_block_page(request, page_id):
    if request.method != 'POST':
        raise PermissionError('Здесь может быть только POST-запрос')
    page = get_object_or_404(Page, id=page_id)
    
    type = request.POST.get('get')
    if type == 'text':
        type = TypeBlock.TEXT
    elif type == 'image':
        type = TypeBlock.IMAGE
    else:
        raise ValueError('Неверный тип блока. Поддерживаетмые типы: '+TypeBlock.TEXT+', '+TypeBlock.IMAGE)
            
    block = Block.objects.create(type=type, page=page)

    return JsonResponse({"status": 200, "block_id": block.id})

