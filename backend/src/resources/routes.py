from .tasks import Tasks, Task, TaskStatus


def initialize_routes(api):
    api.add_resource(Tasks, '/tasks')
    api.add_resource(Task, '/tasks/<string:task_id>')
    api.add_resource(TaskStatus, '/tasks/status/<string:task_id>')
