import json
import base64
import io
import time

from PIL import Image

from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import InMemoryUploadedFile

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
    
    data = json.loads(request.body)
    if not data:
        data = request.POST

    type = data.get('type')
    if type == 'text':
        type = TypeBlock.TEXT
    elif type == 'image':
        type = TypeBlock.IMAGE
    else:
        raise ValueError(f'`{type}` - неверный тип блока. Поддерживаетмые типы: {TypeBlock.TEXT}, {TypeBlock.IMAGE}')
    
    prev_block_id = int(data.get('prev_block_id'))
    block_to_prev = Block.objects.filter(prev_block_id=prev_block_id).first()
            
    block = Block.objects.create(type=type, page=page, prev_block_id=prev_block_id)

    if block_to_prev:
        block_to_prev.prev_block_id = block.id
        block_to_prev.save()

    return JsonResponse({"status": 200, "block": block.as_dict()})


def delete_block_page(request):
    if request.method != 'POST':
        raise PermissionError('Здесь может быть только POST-запрос')
    
    data = json.loads(request.body)
    if not data:
        data = request.POST
        
    block = get_object_or_404(Block, id=int(data.get("block_id")))

    block_to_prev = Block.objects.filter(prev_block_id=block.id).first()
    if block_to_prev:
        block_to_prev.prev_block_id = block.prev_block_id
        block_to_prev.save()

    block.delete()

    return JsonResponse({"status": 200})


def block_set_text_page(request):
    if request.method != 'POST':
        raise PermissionError('Здесь может быть только POST-запрос')
    
    data = json.loads(request.body)
    if not data:
        data = request.POST
    
    block = get_object_or_404(Block, id=int(data.get("block_id")))
    block.type = TypeBlock.TEXT
    block.text = data["text"]
    block.save()

    return JsonResponse({"status": 200})


def decodeImage(b64data):
    try:
        if 'data:' in b64data and ';base64,' in b64data:
            b64data = b64data.split(';base64,')[-1]
        data = base64.b64decode(b64data.encode('UTF-8'))
        buf = io.BytesIO(data)
        img = Image.open(buf)
        return img
    except:
        return None

gtype = type
def block_set_image_page(request):
    if request.method != 'POST':
        raise PermissionError('Здесь может быть только POST-запрос')
    
    data = json.loads(request.body)
    if not data:
        data = request.POST

    type = data["image"][data["image"].index(':')+1:data["image"].index(';')]
    name = str(data.get("block_id")) + '_' + str(time.time())

    img = decodeImage(data["image"])
    img_io = io.BytesIO()
    img.save(img_io, format=type.split('/')[-1])
    new_img = InMemoryUploadedFile(
        img_io, field_name=None,
        name=name+'.'+type.split('/')[-1],
        content_type=type, size=img_io.tell(), charset=None
    )

    block = get_object_or_404(Block, id=int(data.get("block_id")))
    block.type = TypeBlock.IMAGE
    block.image = new_img
    block.save()

    return JsonResponse({"status": 200})
