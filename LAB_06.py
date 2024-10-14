
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# Depth Limited Search function (DLS)
def DLS(node, target, depth):
    if node == target:  # Base case: target node found
        return True
    if depth <= 0:  # If depth limit reached, return False
        return False
    
    for neighbor in graph.get(node, []):  # Explore neighbors
        if DLS(neighbor, target, depth - 1):  # Recursively check neighbors
            print(neighbor, end=" -> ")
            return True
    return False

# Iterative Deepening Search (IDS) function
def IDS(start, target, max_depth):
    for depth in range(max_depth):
        print(f"\nDepth level: {depth}")
        if DLS(start, target, depth):
            print(start)
            return True
    return False

# Driver code
start_node = '5'
target_node = '8'
max_depth_limit = 3

print(f"Following is the Iterative Deepening Search for target node '{target_node}'")
if not IDS(start_node, target_node, max_depth_limit):
    print(f"Target node '{target_node}' was not found within depth limit {max_depth_limit}.")
