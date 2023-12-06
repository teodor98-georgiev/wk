
a = "I can go everywhere and I'm glad for that. I have also to say that i love travelling"
def count_a():
    b = []
    for element in a:
        if element == "a" in a:
           b += element
        else:
           continue
    return len(b)
result = count_a()
print(result)