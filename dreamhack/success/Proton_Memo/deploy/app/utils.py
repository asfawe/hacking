def set_attr(obj, prop, value):
	# obj = user_id;
	# prop = password.data;
	# value = 1212;
    prop_chain = prop.split('.') # ['password', 'data']
    cur_prop = prop_chain[0] # password
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
            if hasattr(obj, cur_prop): # obj에 
                next_obj = getattr(obj, cur_prop)
            else:
                next_obj = {}
                setattr(obj, cur_prop, next_obj)
        set_attr(next_obj, '.'.join(prop_chain[1:]), value)