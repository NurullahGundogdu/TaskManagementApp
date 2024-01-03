from flask_restful import fields

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'status': fields.String,
    'id': fields.String
}