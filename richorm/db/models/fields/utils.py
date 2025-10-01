def get_default(default):
    """Get the default value for this field."""
    if callable(default):
        return default()
    return default

def valueerror(attr: str, value):
    if attr == "null":
        if not isinstance(value, bool):
            raise TypeError(f"'null' must be a boolean, got {type(value).__name__}")
    elif attr =="unique":
        if not isinstance(value, bool):
            raise TypeError(f"'unique' must be a boolean, got {type(value).__name__}")
    else:
        pass