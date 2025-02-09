# Read the number of events
n = int(input())

# Read the list of events
events = list(map(int, input().split()))

# Initialize counters for available officers and untreated crimes
available_officers = 0
untreated_crimes = 0

# Simulate the events
for event in events:
    if event == -1:
        # Crime occurs
        if available_officers > 0:
            # Assign an officer to investigate the crime
            available_officers -= 1
        else:
            # No officers available, crime goes untreated
            untreated_crimes += 1
    else:
        # Officers are hired
        available_officers += event

# Print the number of untreated crimes
print(untreated_crimes)