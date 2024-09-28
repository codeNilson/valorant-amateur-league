import os


def get_env_variable(variable_name: str, default_value=None) -> str:
    if not isinstance(variable_name, str):
        return default_value
    return os.environ.get(variable_name, default_value)


def get_env_list(variable_name: str) -> list:
    if not isinstance(variable_name, str):
        return []
    value = get_env_variable(variable_name, "")
    list_value = [value.strip() for value in value.split(",") if value]
    return list_value
