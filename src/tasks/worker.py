from celery import Celery
from celery.exceptions import Ignore
from celery.states import FAILURE
from tasks import EvaluatePoliciesTask

# Create the app

app = Celery('tasks', backend='redis://redis', broker='amqp://user:pass@rabbit:5672')

# Create the task to be registered
evaluate_policies_task = EvaluatePoliciesTask()

# Registers the task
app.tasks.register(evaluate_policies_task)
