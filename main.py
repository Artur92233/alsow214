from nname import name


def ask_surname(surname: str) -> str:
    full_name = f"Hello, {name} {surname}"
    print(full_name)
    return full_name
