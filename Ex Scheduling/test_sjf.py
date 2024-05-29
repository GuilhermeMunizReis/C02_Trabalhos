from util import *
from random import randint

for i in range(1000):
    size = randint(1,10)
    priority = randint(1,10)

    job = Job(size, priority)
    Scheduler.add_job(job)

print("ID\tSize\tPrior\tExecuted")

w = Worker()

w.run_sjf()

print(w.get_mean_wait_time())