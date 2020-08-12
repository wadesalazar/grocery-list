from views import index, update_list, get_list

grocery_list = { }

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/api/get-list', get_list)
    app.router.add_static('/','web/static/', show_index=True)
    app.router.add_post('/api/update-list', update_list)
    
    
    