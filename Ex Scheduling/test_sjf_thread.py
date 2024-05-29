from util import *
from random import randint

for i in range(1000):
    size = randint(1,10)
    priority = randint(1,10)

    job = Job(size, priority)
    Scheduler.add_job(job)

print("ID\tSize\tPrior\tExecuted")
Scheduler.run_sjf(3)