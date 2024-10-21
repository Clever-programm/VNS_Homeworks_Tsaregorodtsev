def pull(n: int) -> tuple[int, int]:
    max_epic = 10
    max_legendary = 90
    legendary = n // max_legendary
    epic = n // max_epic if n % max_legendary != 0 else n // max_epic - 1
    return epic, legendary