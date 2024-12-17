"""

Problem #3 - Debug Calendar Design

Your teammate has implemented a calendar program, but it doesn’t work as expected.  
Ideally, a user should be able to add a new event, if it does not cause a double booking. Double bookings occur when two events overlap in time. For example, Event A lasts from Saturday 2 pm - 5 pm and Event B lasts Saturday 3 pm - 4 pm. These events overlap and would be considered a double booking.
Events are represented as a pair of ints - start and end. Two events can be scheduled back to back, e.g. Event A can be [2,3) and Event B can be [3, 4).
Your teammate has already implemented the Calendar class:
Calendar() Initializes the calendar object.
boolean schedule(int start, int end) Returns true if the event can be added without causing a double booking. Returns false otherwise  and does not add the event to the calendar.

Your teammate’s code can be found in the attached file calendar.py.  Please debug the code to fix the current issues. When submitting this portion of the assignment, please attach your fixed code and a README.md file that explains how you debugged it step-by-step and what the underlying issue was. We may discuss this document at the end of the evaluation.
Example Input & Output
calendar = Calendar()
calendar.book(5, 10) -> Expect True
calendar.book(8, 13) -> Expect False
calendar.book(10, 15) -> Expect True
"""

from typing import Optional


class Node():
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:
        if node.start >= self.end:
            if not self.right_child:
                self.right_child = node
                return True
            return self.right_child.insert(node)
        elif node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node)
        else:
            return False

class Calendar():
    def __init__(self):
        self.root: Node = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start=start, end=end)
            return True
        return self.root.insert(node=Node(start, end))

if __name__ == "__main__":
    calendar = Calendar()
    print(calendar.book(5, 10))
    print(calendar.book(8, 13))
    print(calendar.book(10, 15))
