from src.services.tasks import TaskService
from src.utils.enums import Status


def test_create_task():
    title = 'test'
    description = 'test'

    task = TaskService().create_task(title, description)

    assert task.get("status") is True
    assert task.get("task", {}).get("title") == title
    assert task.get("task", {}).get("description") == description
    assert task.get("task", {}).get("status") == Status.OPEN.value


def test_update_task():
    title = 'test'
    description = 'test'
    updated_title = 'test2'
    updated_description = 'test2'

    task = TaskService().create_task(title, description)

    assert task.get("status") is True
    assert task.get("task", {}).get("title") == title
    assert task.get("task", {}).get("description") == description
    assert task.get("task", {}).get("status") == Status.OPEN.value

    updated_task = TaskService().update_task(task.get("task", {}).get("id"), updated_title, updated_description)

    assert updated_task.get("status") is True
    assert updated_task.get("task", {}).get("title") == updated_title
    assert updated_task.get("task", {}).get("description") == updated_description
    assert updated_task.get("task", {}).get("status") == Status.OPEN.value


def test_update_task_status():
    title = 'test'
    description = 'test'

    task = TaskService().create_task(title, description)

    assert task.get("status") is True
    assert task.get("task", {}).get("title") == title
    assert task.get("task", {}).get("description") == description
    assert task.get("task", {}).get("status") == Status.OPEN.value

    task = TaskService().update_task_status(task.get("task", {}).get("id"))

    assert task.get("status") is True
    assert task.get("task", {}).get("title") == title
    assert task.get("task", {}).get("description") == description
    assert task.get("task", {}).get("status") == Status.TESTING.value

    task = TaskService().update_task_status(task.get("task", {}).get("id"))

    assert task.get("status") is True
    assert task.get("task", {}).get("title") == title
    assert task.get("task", {}).get("description") == description
    assert task.get("task", {}).get("status") == Status.DONE.value


def test_delete_task():
    title = 'test'
    description = 'test'

    task = TaskService().create_task(title, description)

    assert task.get("status") is True
    assert task.get("task", {}).get("title") == title
    assert task.get("task", {}).get("description") == description
    assert task.get("task", {}).get("status") == Status.OPEN.value

    task = TaskService().delete_task(task.get("task", {}).get("id"))

    assert task.get("status") is True
    assert task.get("task", {}).get("title") == title
    assert task.get("task", {}).get("description") == description
    assert task.get("task", {}).get("status") == Status.DELETED.value


def test_get_tasks():

    title = 'test'
    description = 'test'

    task = TaskService().create_task(title, description)

    assert task.get("status") is True
    assert task.get("task", {}).get("title") == title
    assert task.get("task", {}).get("description") == description
    assert task.get("task", {}).get("status") == Status.OPEN.value

    tasks = TaskService().get_tasks()

    assert tasks.get("status") is True
    assert len(tasks.get("tasks")) > 0


