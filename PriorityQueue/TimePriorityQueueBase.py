'''
MIT License

Copyright (c) 2017 Himanshu Maurya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

class TimePriorityQueueBase:
    """Base class for a time-based priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items.
           '_key': Tuple of (Time To Expire, Priority, Difference from start time)
           '_value': Task to Perform
           Time To Expire : datetime object
           Priority : int
           Difference from start time: datetime object
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
