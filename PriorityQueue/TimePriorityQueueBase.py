class TimePriorityQueueBase:
    """Base class for a time-based priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items.
           '_key': Tuple of (Time To Expire, Priority)
           '_value': Task to Perform
           Time To Expire : datetime object
           Priority : int
        """
        __slots = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            """
                Run the tasks with lower time to expire first.
                If time to expire matches then run higher priority first.
            """

            if self._key[2] < other._key[2]:
                return True
            elif self._key[2] == other._key[2]:
                if self._key[1] >= other._key[1]:
                    return True
                else:
                    return False
            else:
                return False

    def is_empty(self):
        return len(self) == 0
