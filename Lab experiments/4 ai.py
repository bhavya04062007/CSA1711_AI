import itertools

# Words
word1 = "SEND"
word2 = "MORE"
result = "MONEY"

# Get unique letters
letters = set(word1 + word2 + result)
letters = list(letters)

# There must be <= 10 unique letters
if len(letters) > 10:
    print("Too many letters for digits!")
    exit()

# Leading letters cannot be zero
leading_letters = {word1[0], word2[0], result[0]}

# Convert word to number using mapping
def word_to_number(word, mapping):
    number = ""
    for ch in word:
        number += str(mapping[ch])
    return int(number)

# Try all permutations of digits
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    mapping = dict(zip(letters, perm))

    # Check leading zero condition
    if any(mapping[ch] == 0 for ch in leading_letters):
        continue

    n1 = word_to_number(word1, mapping)
    n2 = word_to_number(word2, mapping)
    n3 = word_to_number(result, mapping)

    if n1 + n2 == n3:
        print("Solution Found!\n")
        print("Mapping:")
        for k in sorted(mapping):
            print(k, "=", mapping[k])

        print("\n", n1)
        print("+", n2)
        print("------")
        print(n3)
        break
else:
    print("No solution found")
