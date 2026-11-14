"""I checked your Coding_Excersize repo. This problem isn't there.

A hiker starts at sea level, 0:
* U means go up by 1.
* D means go down by 1.

A valley starts when the hiker goes below 0 and ends when they return to 0. Count the valleys.

Example: "UDDDUDUU" → 1 valley.
Levels: 0, 1, 0, -1, -2, -1, -2, -1, 0.

For your local practice, write:

def counting_valleys(path):
    # your code here

Test cases:
"UDDDUDUU" → 1
"DDUUDDUDUUUD" → 2
"UDUD" → 0
"DDDDUUUU" → 1

Use a loop and if/else. """

def counting_valleys(path):
    level = 0
    valleys = 0
    for step in path:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        elif step == 'D':
            level -= 1
    return valleys

print(counting_valleys("UDDDUDUU"))
