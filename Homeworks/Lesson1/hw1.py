def pull(n: int) -> tuple[int, int]:
    max_epic = 10
    max_legendary = 90
    legendary = n // max_legendary
    if n >= max_legendary:
        n -= 1
    epic = n // max_epic
    return epic, legendary