file_name = "C:/Users/65866/PycharmProjects/app1/todos.txt"


def read_todo(file):
    """Reads the to-do list from the file."""
    try:
        with open(file, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_todo(file, todos):
    """Writes the to-do list to the file."""
    with open(file, 'w') as file:
        file.writelines(todos)
