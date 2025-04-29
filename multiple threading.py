from time import sleep
from threading import*
class hello(thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(5)
class hi(thread):
     def run(self):
        for i in range(5):
            print("hi")
            sleep(8)
t1=hello()
t2=hi()
t1.start()
sleep(0.2)
t2.start()
print("bye")

    
