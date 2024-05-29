import threading

class Job:
    def __init__(self, size, priority):
        self.id = None
        self.size = size
        self.priority = priority
        self.executed = False

    def __repr__(self):
        return f"{self.id}\t{self.size}\t{self.priority}\t{self.executed}"

    def execute_job(self):
        self.executed = True

        return True

class Scheduler:
    _current_job_id = 0
    _jobs = []
    
    @staticmethod
    def _generate_id():
        Scheduler._current_job_id += 1

        return Scheduler._current_job_id
    
    @staticmethod
    def add_job(job:Job):
        job.id = Scheduler._generate_id()
        Scheduler._jobs.append(job)

    @staticmethod
    def sjf_get_job() -> Job:
        """ Verifica qual o próximo JOB deve ser executado com Shortest Job First """
        if len(Scheduler._jobs) == 0:
            return
        
        size = Scheduler._jobs[0].size
        job = Scheduler._jobs[0]

        for j in Scheduler._jobs:
            if j.size < size:
                size = j.size
                job = j
        
        Scheduler._remove_job(job)
        
        return job
    
    @staticmethod
    def ps_get_job() -> Job:
        """ Verifica qual o próximo JOB deve ser executado com Priority Scheduling """
        if len(Scheduler._jobs) == 0:
            return 
        
        priority = Scheduler._jobs[0].priority
        job = Scheduler._jobs[0]
        
        for j in Scheduler._jobs:
            if j.priority < priority:
                priority = j.priority
                job = j

        Scheduler._remove_job(job)
        
        return job

    @staticmethod    
    def run_ps(thread_count):
        thread_count = thread_count
        threads = []
        workers = []

        for _ in range(thread_count):
            w = Worker()
            workers.append(w)

            t = threading.Thread(target=w.run_ps, args=())
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        for w in workers:
            print(w.get_mean_wait_time())            

    def run_sjf(thread_count):
        thread_count = thread_count
        threads = []
        workers = []

        for _ in range(thread_count):
            w = Worker()
            workers.append(w)

            t = threading.Thread(target=w.run_sjf, args=())
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        for w in workers:
            print(w.get_mean_wait_time())

    @staticmethod
    def _remove_job(job:Job):
        Scheduler._jobs.remove(job)

class Worker:
    def __init__(self):
        self.jobs_count = 0
        self.burst_time = 0
        self.waiting_time = 0

    def get_mean_wait_time(self):
        return self.waiting_time // self.jobs_count

    def run_ps(self):
        while True:
            job = Scheduler.ps_get_job()

            if job == None:
                print("All jobs done")            
                break
            else:
                job.execute_job()
                self.burst_time += job.size
                self.jobs_count += 1
                
                self.waiting_time += self.burst_time
                print(job)

    def run_sjf(self):
        while True:
            job = Scheduler.sjf_get_job()

            if job == None:
                print("All jobs done")
                break            
            else:
                job.execute_job()
                self.burst_time += job.size
                self.jobs_count += 1

                self.waiting_time += self.burst_time
                print(job)



                