import re

# Test 1
text1 = "This is an email address: john.doe@email.com and another one: jane.smith@email.net"
pattern1 = r'\b\w+@\w+\.\w+\b'

matches1 = re.findall(pattern1, text1)

if matches1:
    print("Matches found in Text 1:")
    for match in matches1:
        print(match)
else:
    print("No matches found in Text 1")

# Test 2
text2 = "Phone numbers: 123-456-7890, 555-8675309, and 999-888-7777"
pattern2 = r'\d{3}-\d{3}-\d{4}'

matches2 = re.findall(pattern2, text2)

if matches2:
    print("\nMatches found in Text 2:")
    for match in matches2:
        print(match)
else:
    print("No matches found in Text 2")

# Test 3
text3 = "This is a list of dates: 2023-11-08, 1990-05-15, and 2022-12-31"
pattern3 = r'\d{4}-\d{2}-\d{2}'

matches3 = re.findall(pattern3, text3)

if matches3:
    print("\nMatches found in Text 3:")
    for match in matches3:
        print(match)
else:
    print("No matches found in Text 3")

# text4 = "Shrey g is a great  1234 @ jain" # fail
text4 = "Shrey g is a great 1234 @ jain"
pattern4 = r'g\w+\s\d{4}'
print(re.search(pattern4, text4).group())
