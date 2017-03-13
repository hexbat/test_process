from multiprocessing import Process
import time

def f(arrs, arrs2):
    for i in xrange(arrs2):
        arrs.append(i)
    print arrs

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    t = []
    for x in xrange(10):
        p = Process(target=f, args=[a, x])
        t.append(p)
        time.sleep(0.01)
        p.start()
    for prc in t:
        prc.join()
    print a