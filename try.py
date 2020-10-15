
import threading
def put_input():
    global x 
    move = input("choose your move: ")
    x = move

t1 = threading.Thread(target = put_input)
t1.start()
t1.join()
for i in range(10):
    print (x)


