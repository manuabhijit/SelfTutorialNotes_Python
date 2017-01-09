import threading

class MyMessenger(threading.Thread):
    def run(self):
        for _ in range(20):
            print(threading.current_thread().getName() + " ")

x = MyMessenger(name='Sender')
y = MyMessenger(name='Reciever')

x.start()
y.start()

