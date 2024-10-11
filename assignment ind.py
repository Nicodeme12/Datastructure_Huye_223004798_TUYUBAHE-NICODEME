undo_stack = []

def distribute_item(item):
    # Code to distribute the item
    undo_stack.append(item)

def undo_last_distribution():
    if undo_stack:
        last_item = undo_stack.pop()
        # Code to undo the distribution of last_item
    else:
        print("No distributions to undo.")
from collections import deque

distribution_queue = deque()

def add_to_queue(item):
    distribution_queue.append(item)

def process_next_distribution():
    if distribution_queue:
        next_item = distribution_queue.popleft()
        # Code to process the distribution of next_item
    else:
        print("No items in the distribution queue.")
items_list = []

def track_item(item, status):
    items_list.append({'item': item, 'status': status})

def display_tracked_items():
    for entry in items_list:
        print(f"Item: {entry['item']}, Status: {entry['status']}")

# Example usage
distribute_item("jordan")
add_to_queue("airforce")
track_item("jordan", "Distributed to shelter A")
track_item("airforce", "Pending distribution")

process_next_distribution()
undo_last_distribution()
display_tracked_items()
