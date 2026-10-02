import threading,time
mutex=threading.Lock()
def work():
    mutex.acquire()
    for i in range(10):
        time.sleep(0.1)
        print('nih')
    mutex.release()
if __name__ == '__main__':
    t=threading.Thread(target=work)
    t.start()
    time.sleep(0.5)
    print('hello')







