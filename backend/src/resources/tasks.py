from src.services.tasks import TaskService
from flask_restful import Resource, reqparse


class Tasks(Resource):
    def __init__(self):
        self.reqparse_post = reqparse.RequestParser()
        self.reqparse_post.add_argument('title',
                                        type=str,
                                        required=True,
                                        help='No task title provided',
                                        location='json')
        self.reqparse_post.add_argument('description',
                                        type=str,
                                        required=True,
                                        help='No task title provided',
                                        location='json')
        self.reqparse_put = self.reqparse_post.copy()
        self.reqparse_put.add_argument('id',
                                       type=str,
                                       required=True,
                                       help='No task id provided',
                                       location='json')
        super(Tasks, self).__init__()

    def get(self):
        return TaskService().get_tasks()

    def put(self):
        body = self.reqparse_put.parse_args()
        return TaskService().update_task(body.get("id"),
                                         body.get("title"),
                                         body.get("description"))

    def post(self):
        body = self.reqparse_post.parse_args()
        return TaskService().create_task(body.get("title"),
                                         body.get("description"))


class Task(Resource):
    def delete(self, task_id):
        return TaskService().delete_task(task_id)


class TaskStatus(Resource):
    def put(self, task_id):
        return TaskService().update_task_status(task_id)
