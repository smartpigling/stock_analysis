#-*- coding:utf-8 -*-
def nn_index_group(ids):
    """自然数序列分组"""  
    _ids = []
    for i, id in enumerate(ids):
        _ids.append(id)
        try:
            if ids[i+1] - id != 1:
                yield _ids
                _ids=[]
        except IndexError:
            yield _ids