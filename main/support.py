def get_menu_context():
    return [
        {"url_name": 'index', "name": "Русский", 'active': ''},
        {"url_name": 'index', "name": "Татарча (Татарский)", 'active': ''},
        {"url_name": 'index', "name": "Башкирский", 'active': ''},
        {"url_name": 'index', "name": "O'zbek (Узбекский)", 'active': ''},
        {"url_name": 'index', "name": "Чеченский", 'active': ''},
        {"url_name": 'index', "name": "English (Английский)", 'active': ''},
        {"url_name": 'index', "name": "Четыре духовные истины", 'active': ''},
    ]

def get_id_page_in_menu(menu, url_name):
    for i in range(len(menu)):
        if menu[i]['url_name'] == url_name:
            return i
    return 0

def get_base_context(request, pagename, url_name):
    context = {
        'menu': get_menu_context(),
        'pagename': pagename,
    }
    context['menu'][get_id_page_in_menu(context['menu'], url_name)]['active'] = True
    return context
