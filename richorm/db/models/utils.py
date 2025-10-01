def default_str(owner):
    class_name = owner.__class__.__name__
    attr_list = []
    for key, value in owner.__dict__.items():
        if not key.startswith('_'):
            attr_list.append(f'{key}={value}')
            
    attrs_str = ','.join(attr_list)
    return f'richORM_{class_name}:({attrs_str})'