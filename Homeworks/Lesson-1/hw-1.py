
def pull(n: int) -> tuple[int, int]:
    max_epic = 10
    max_legendary = 90
    count = 0 
    legendary = n // 90
    epic = n // 10 if n % 90 != 0 else n // 10 - 1
    return (epic, legendary)


print(pull(int(input())))