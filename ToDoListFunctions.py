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


def add_todo(todo: str, todos: List[str]) -> List[str]:
    """Adds a new item to the to-do list."""
    todos.append(todo.capitalize())
    return todos


def see_todo(todos) -> None:
    """Displays the current to-do list."""
    if todos:
        print("\n Your to-do list:")
        for index, task in enumerate(todos, start=1):
            print(f"{index}. {task.strip()}")
    else:
        print("\n Your to-do list is empty.")


def complete_todo(item_number: int, todos) -> tuple[{__name__}, str] | str:
    """Deletes an item from the to-do list."""
    try:
        if 1 <= item_number <= len(todos):
            del todos[item_number - 1]
            return todos, "\n Task deleted from your to-do list."
        else:
            return "\n Invalid item number."
    except ValueError:
        return "\n Invalid input. Please enter a valid item number."


def edit_todo(item_number: int, new_task: str, todos) -> tuple[{__name__}, str] | str:
    """Edits an item in the to-do list."""
    try:
        if 1 > item_number or item_number > len(todos):
            return "\n Invalid item number."
        else:
            todos[item_number - 1] = new_task.capitalize() + "\n"
            return todos, "\n Task deleted from your to-do list."
    except ValueError:
        return "\n Invalid input. Please enter a valid item number."
