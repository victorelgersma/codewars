# Write a function that always returns a 5
# Bear in mind you can't use the characters 0123456789*+-/

# Attempt 1

def unusual_five():
    word = 'lllll'
    count = word.count('l')
    return count


if __name__ == "__main__":
    print(unusual_five())


