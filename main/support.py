def get_menu_context():
    return [
        {"url_name": 'index', "name": "Русский", 'active': False},
    ]

def get_id_page_in_menu(menu, url_name):
    for i in range(len(menu)):
        if menu[i]['url_name'] == url_name:
            return i
    return -1

def get_base_context(request, pagename, url_name):
    context = {
        'menu': get_menu_context(),
        'pagename': pagename,
    }
    id = get_id_page_in_menu(context['menu'], url_name)
    if id != -1:
        context['menu'][id]['active'] = True
    return context
