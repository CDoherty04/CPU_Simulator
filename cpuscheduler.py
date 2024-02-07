import linkedqueue


class CPUScheduler:
    """
    The CPU_Scheduler is in charge of adding Processes to a Queue,
    allowing them CPU time, then moving them to the back of the queue if they need
    """

    def __init__(self):
        """Initializes the scheduler with an empty process queue"""
        self._process_queue = linkedqueue.LinkedQueue()

    def add_process(self, process):
        """Adds a process to _process_queue"""
        self._process_queue.enqueue(process)

    def give_cpu_time(self, func):
        """Gives time for the top process in the queue"""
        print(f"{self._process_queue.peek_front().get_name()} called the "
              f"function \"{func.get_name()}\"")
        process = self._process_queue.peek_front()
        process.add_call(func)
        self.move_to_back()
        
    def return_next_function(self):
        """Returns the front process' top function"""
        if self._process_queue.peek_front().get_call_stack().peek().get_name() != "main":
            print(f"{self._process_queue.peek_front().get_name()} returned "
                  f"\"{self._process_queue.peek_front().get_call_stack().peek().get_name()}\"")
            self._process_queue.peek_front().return_function()
        else:
            print(f"{self._process_queue.peek_front().get_name()} returned \"main\"")
            print(f"The \"{self._process_queue.peek_front().get_name()}\" process has ended")
            self._process_queue.dequeue()

    def move_to_back(self):
        """Moves a process to the back of the queue"""
        self._process_queue.enqueue(self._process_queue.dequeue())
