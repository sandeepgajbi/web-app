import streamlit as st
import ToDoListFunctions as fs

todos = fs.read_todo(fs.file_name)


def add_todo():
    if "new_todo" in st.session_state:
        new_todo = st.session_state.new_todo.strip()
        if new_todo:
            todos.append(new_todo + "\n")
            fs.write_todo(fs.file_name, todos)
            st.session_state.new_todo = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        fs.write_todo(fs.file_name, todos)
        del st.session_state[index]
        st.rerun()

st.text_input(label="add", label_visibility='hidden', placeholder="Add new todo..",
              key='new_todo')
st.button("Add", on_click=add_todo)
