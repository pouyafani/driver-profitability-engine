def ensure_not_null(value, message: str):
    if value is None:
        raise ValueError(message)

