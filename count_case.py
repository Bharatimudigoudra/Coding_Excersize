"""Write a function count_case(text).
It counts how many uppercase and how many lowercase letters are in text.
Ignore spaces, digits, symbols.
Print both counts.
Use def + for loop only."""

def count_case(text):
    upper = 0
    lower = 0
    for ch in text:
        if ch >= "A" and ch <= "Z":
            upper = upper + 1
        elif ch >= "a" and ch <= "z":
            lower = lower + 1
    print("Uppercase:", upper, "Lowercase:", lower)

count_case("Bharati Mudigoudra")