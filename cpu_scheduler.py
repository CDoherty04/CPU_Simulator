import linkedqueue


class CPUScheduler:
    """
    The CPU_Scheduler is in charge of adding Processes to a Queue,
    allowing them CPU time, then moving them to the back of the queue if they need
    """

    def __init__(self):
        self.process_queue = linked_queue.Linked_Queue()

    def add_process(self, process):
        """Adds a process to process_queue"""
        pass

    def move_to_back(self):
        """Moves a process to the back of the queue"""
        pass
