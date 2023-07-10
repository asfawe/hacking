from models import Memo
import time

def set_attr(obj, prop, value):
    prop_chain = prop.split('.')
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
            if hasattr(obj, cur_prop):
                next_obj = getattr(obj, cur_prop)
            else:
                next_obj = {}
                setattr(obj, cur_prop, next_obj)
        set_attr(next_obj, '.'.join(prop_chain[1:]), value)

memo = Memo.get_memo_by_id("b66951df-4a7d-423f-b164-f7b37b9d9605")

set_attr(memo, "title" + ".data", "hehe")
set_attr(memo, "user" + ".edit_time", time.time())