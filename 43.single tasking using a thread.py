from threading import Thread
import time
class myexam:
    def q1(self):
        print("question one solved")
    def q2(self):
        print("question two solved")
    def q3(self):
        print("question three solved")
        
    def solve_question(self):
        self.q1()
        time.sleep(5)
        self.q2()
        time.sleep(5)
        self.q3()

myc=myexam()# creating object of myexam class
t=Thread(target=myc.solve_question)# creating object of Thread calss with target
t.start()# starting thread
