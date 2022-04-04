import time

class Stopwatch:

    def __init__(self):
        self.total = 0
        self.start = None
        self.duration = 0

    def start_timer(self):
        sec = 0
        if self.start == None:
            self.start = time.time()

    def pause_timer(self):
        if self.start != None:
            now = time.time()
            self.duration = now - self.start
            self.total += self.duration
            self.start = None
    
    def get_duration(self):
        now = time.time()
        duration = now - self.start
        print("duration " + str(duration))

    def get_pause_duration(self):
        print("Pause duration " + str(self.duration))

    def get_number_of_pauses(self):
        pass


if __name__ == "__main__":
    timer = Stopwatch()
    timer.start_timer()
    lis = []
    timer.pause_timer()
    iteration = int(input("Enter the iteration: "))
    for i in range(iteration):
        lis.append(i)
    timer.start_timer()
    a = 0
    b = 0
    for i in range(iteration):
        if i in lis:
            a = a + 1
            lis.remove(i)
    lis.clear()
    timer.get_duration()
    timer.get_pause_duration()