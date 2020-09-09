# -- coding: utf-8 --
from time import sleep
from redis import Redis
from rq import Queue
from redis_modules import get_user_github

if __name__ == "__main__":
  print "Initializing redis master"
  redis_conn = Redis(host='127.0.0.1',port=6379)
  queue_jobs = Queue('my_queue', connection=redis_conn)
  jobs = []

  users = ['BrunaBelo', 'AndressaKaroline', 'fabiosammy']
  for i in range(len(users)):
    job = queue_jobs.enqueue(get_user_github, users[i])
    jobs.append(job)

  for job in jobs:
    print "Trabalhos enfileirados {0}".format(len(queue_jobs))
    while job.result is None:
      print "O trabalho {0} ainda nao foi concluido".format(job.id)
      sleep(2)
      print job.result