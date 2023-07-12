from test2 import test, a

def set_attr(obj, prop, value):
    prop_chain = prop.split('.')
    cur_prop = prop_chain[0]
    print(prop_chain)
    print(cur_prop)
    if len(prop_chain) == 1:
        if isinstance(obj, dict):
            obj[cur_prop] = value
        else:
            setattr(obj, cur_prop, value)
    else:
        if isinstance(obj, dict):
            if  cur_prop in obj:
                next_obj = obj[cur_prop]
            else:
                next_obj = {}
                obj[cur_prop] = next_obj
        else:
            if hasattr(obj, cur_prop):
                next_obj = getattr(obj, cur_prop)
            else:
                next_obj = {}
                setattr(obj, cur_prop, next_obj)
        # print(next_obj)
        set_attr(next_obj, '.'.join(prop_chain[1:]), value)


set_attr(test, '__init__.__globals__.__loader__.__init__.__globals__.sys.modules.__main__.test2.secret.password.data', '122222')

print(a.password.data)
