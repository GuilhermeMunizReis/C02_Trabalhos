from util2 import *
import threading

account = Account("Jorge", 15000)

Transfer.set_account(account)

threads = []
random_transactions = []

clients = 3
for i in range(clients):
    r = RandomTransaction()
    random_transactions.append(r)

    t = threading.Thread(target=r.do_transaction, args=(), name = f"Client {i+1}")
    r.thread = t
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()