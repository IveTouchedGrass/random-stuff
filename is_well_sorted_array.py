def is_well_shuffled(arr: list) -> bool:
    try:
        for i in range(len(arr)):
            if (arr[i] == arr[i + 1] - 1 and arr[i + 1] == arr[i + 2] - 1) or (arr[i] == arr[i + 1] + 1 and arr[i + 1] == arr[i + 2] + 1):
                return False
    except IndexError:
        pass
    return True

exec(f"print(is_well_shuffled({input()}))")