# ollections is a very powerful Python standard library module that provides specialized container types beyond the usual list, dict, set, and tuple.

# Commonly Used collections Types
# Counter
# Counts occurrences of elements in a list (or iterable)
# Returns a dictionary-like object
from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
count = Counter(nums)
print(count)


# deque
# Double-ended queue — efficient for adding/removing from both ends
# Can replace list when you need O(1) pops from left
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)
dq.popleft()
dq.pop()
print(dq)


# Here’s how you can implement a Stack in Python. There are two common ways: using a list (simplest) or deque (more efficient for large data).



# Create an empty stack
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)  # [10, 20, 30]

# Pop elements (removes from top)
print("Popped:", stack.pop())        # 30
print("Popped:", stack.pop())        # 20

print("Stack now:", stack)           # [10]

# Peek at top element without popping
print("Top element:", stack[-1])     # 10

# Check if stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
    
    
    
    
    # Using deque (more efficient for big stacks)
    
    
from collections import deque

# Create stack
stack = deque()

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)  # deque([10, 20, 30])

# Pop elements
print("Popped:", stack.pop())        # 30
print("Stack now:", stack)           # deque([10, 20])

# Peek at top
print("Top element:", stack[-1])     # 20