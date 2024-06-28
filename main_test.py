import pytest
from main import ToDoList


@pytest.fixture
def todo_list():
    return ToDoList()


def test_add_task(todo_list):
    todo_list.add_task("Task 1")
    assert "Task 1" in todo_list.tasks


def test_view_tasks_empty(todo_list, capsys):
    todo_list.view_tasks()
    captured = capsys.readouterr()
    assert captured.out == "No tasks in the to-do list.\n"


def test_delete_task_valid(todo_list):
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    todo_list.delete_task(1)
    assert "Task 1" not in todo_list.tasks
    assert "Task 2" in todo_list.tasks


def test_delete_task_invalid(todo_list, capsys):
    todo_list.add_task("Task 1")
    todo_list.delete_task(3)
    captured = capsys.readouterr()
    assert "Invalid task number." in captured.out
    assert "Task 1" in todo_list.tasks


def test_view_tasks(todo_list, capsys):
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    todo_list.view_tasks()
    captured = capsys.readouterr()
    assert "1. Task 1" in captured.out
    assert "2. Task 2" in captured.out
