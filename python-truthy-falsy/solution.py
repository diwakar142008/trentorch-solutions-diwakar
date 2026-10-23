def is_truthy(value) -> bool:
    """Return the truthiness of `value` exactly as Python's own rules would determine it."""
    if value is None:
        return False
    if isinstance(value, (int, float, complex)) and value == 0:
        return False
    if isinstance(value, (str, list, tuple, dict, set)) and len(value) == 0:
        return False
    return True


def first_truthy(values: list):
   
    for val in values:
        if is_truthy(val):
            return val
    return None
