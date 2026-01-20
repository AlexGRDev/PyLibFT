def ft_isinstance(obj, types):
    is_iterable = (
        hasattr(types, "__iter__") and not hasattr(types, "__mro__")
    )
    iter_types = types if is_iterable else (types,)
    is_tuple = False
    for t in iter_types:
        is_tuple = True
        break
    if is_tuple:
        for t in types:
            if ft_isinstance(obj, t):
                return True
        return False
    obj_type = obj.__class__
    mro = obj_type.__mro__
    for base in mro:
        if base is types:
            return True
    return False
