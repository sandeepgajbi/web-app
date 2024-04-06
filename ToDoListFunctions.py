from typing import List, Tuple


def read_todo(file) -> List[str]:
    """Reads the to-do list from the file."""
    try:
        with open(file, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_todo(file, todos: List[str]) -> None:
    """Writes the to-do list to the file."""
    with open(file, 'w') as file:
        file.writelines(todos)

