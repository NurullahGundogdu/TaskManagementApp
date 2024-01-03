from enum import Enum


class Status(Enum):
    OPEN = 'open'
    TESTING = 'testing'
    DONE = 'done'
    DELETED = 'deleted'
