import streamlit as st
import ToDoListFunctions as fs

file_name = "C:/Users/65866/PycharmProjects/app1/todos.txt"

todos = fs.read_todo(file_name)


def add_todo():
    user_input = st.session_state["new_todo"]
    todos.append(user_input + "\n")
    fs.write_todo(file_name, todos)
    del st.session_state["new_todo"]


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        fs.write_todo(file_name, todos)
        del st.session_state[index]
        st.rerun()

st.text_input(label="add", label_visibility='hidden', placeholder="Add new todo..",
              on_change=add_todo, key='new_todo')