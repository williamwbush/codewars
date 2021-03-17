# https://www.codewars.com/kata/5550d638a99ddb113e0000a2/solutions/python

# This problem takes its name by arguably the most important event in the life of the ancient historian Josephus: according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.

# Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and proceeded to kill one man every three, until one last man was left (and that it was supposed to kill himself to end the act).

# Well, Josephus and another man were the last two and, as we now know every detail of the story, you may have correctly guessed that they didn't exactly follow through the original idea.

# You are now to create a function that returns a Josephus permutation, taking as parameters the initial array/list of items to be permuted as if they were in a circle and counted out every k places until none remained.

def josephus(items,k):
    e_items = list(enumerate(items))
    i = 0
    distance = 0
    order = []
    indexes = []
    
    while len(order) < len(items):
        value = e_items[i % len(items)][1]

        if i % len(items) in indexes:
            i += 1
            continue
        distance += 1
        if distance == k:
            order.append(value)
            distance = 0
            indexes.append(i % len(items))
        i += 1
    return order

print(josephus([True,False,True,False,True,False,True,False,True],9))