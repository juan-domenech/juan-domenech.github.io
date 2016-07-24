#!/usr/bin/python
# https://docs.python.org/2/library/thread.html?highlight=thread#module-thread

# Threading exercise
# Launch a multi-threaded function and keep only once instance running at once.

import threading
import time

class Threading (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print "Starting " + self.name
        print_time(self.name, 1, 5)
        print "Exiting " + self.name
        del self

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

print "Starting Main Thread"

counter = 0

thread = Threading(1,"Thread-1")

while counter < 5:
    if thread.isAlive() == False:
        thread = Threading(1,"Thread-1")
        thread.start()
        counter += 1

print "Exiting Main Thread"
