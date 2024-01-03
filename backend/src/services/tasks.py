import uuid
from datetime import datetime
from src.db.inmemorydb import tasks
from src.utils.enums import Status
from src.models.task import Task
from flask_restful import marshal
from src.utils.task_fields import task_fields


class TaskService:

    def create_task(self, title: str, description: str):
        try:
            myuuid = str(uuid.uuid4())

            task = Task(id=myuuid,
                        title=title,
                        status=Status.OPEN.value,
                        description=description,
                        created_at=datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"),
                        updated_at=datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"))

            tasks[myuuid] = task

            return {"task": marshal(task.__dict__, task_fields), "status": True}
        except:
            return {"status": False}

    def update_task(self, _id: str, title: str, description: str):
        try:
            if not tasks.get(_id):
                return {"status": False, "message": "Task not found!!!"}

            tasks[_id].title = title
            tasks[_id].description = description
            tasks[_id].updated_at = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")

            return {"task": marshal(tasks.get(_id).__dict__, task_fields), "status": True}
        except:
            return {"status": False}

    def update_task_status(self, task_id: str):
        try:
            if not tasks.get(task_id):
                return {"status": False, "message": "Task not found!!!"}

            if tasks.get(task_id).status == Status.OPEN.value:
                tasks[task_id].status = Status.TESTING.value
            elif tasks.get(task_id).status == Status.TESTING.value:
                tasks[task_id].status = Status.DONE.value
            else:
                return {"status": False, "message": "Can not update task status!!!"}

            return {"status": True, "task": marshal(tasks.get(task_id).__dict__, task_fields)}
        except:
            return {"status": False}

    def delete_task(self, task_id):
        try:
            if not tasks.get(task_id):
                return {"status": False, "message": "Task not found!!!"}

            tasks[task_id].status = Status.DELETED.value

            return {"status": True, "task": marshal(tasks.get(task_id).__dict__, task_fields)}
        except:
            return {"status": False}

    def get_tasks(self):
        try:
            tasks_list = [marshal(task.__dict__, task_fields) for task_id, task in tasks.items() if task.status != Status.DELETED.value]

            return {"tasks": tasks_list, "status": True}
        except:
            return {"status": False}
