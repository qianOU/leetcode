def back_trace(s, cur, path):
    if len(path) == 2: return path 
    for i in range(cur+1, len(s)):
        path += s[i]
        yield from back_trace(s, cur+1, path)
        path = path[:-1]

a = 