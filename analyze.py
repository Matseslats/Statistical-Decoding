import matplotlib.pyplot as plt

text = ""
with open("code.txt") as f:
    text = f.readline()

print(text)
counts = [0]*26
labels = [0]*26

for i, a in enumerate(labels):
    labels[i] = chr(ord('@')+i)

for i, a in enumerate(text):
    print(a, ord(a), ord(a)-65)
    counts[ord(a)-65] += 1

plt.bar(labels, counts)

plt.show()