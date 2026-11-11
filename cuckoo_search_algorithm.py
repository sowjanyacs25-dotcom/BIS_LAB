

import random

n = 10
Pa = 0.25
MaxIter = 100

tasks = [3, 5, 2, 7, 4, 6, 3, 5]
employees = 3


def generate():
    return [random.randint(0, 2) for _ in tasks]


def fitness(x):
    time = [0] * employees
    for i in range(len(tasks)):
        time[x[i]] += tasks[i]
    return max(time)

nests = [generate() for _ in range(n)]
best = min(nests, key=fitness)


for t in range(MaxIter):

    for i in range(n):
        new = nests[i].copy()


        j = random.randint(0, len(tasks)-1)
        new[j] = random.randint(0, employees-1)

        if fitness(new) < fitness(nests[i]):
            nests[i] = new


    for i in range(n):
        if random.random() < Pa:
            nests[i] = generate()


    current = min(nests, key=fitness)
    if fitness(current) < fitness(best):
        best = current.copy()


for e in range(employees):
    assigned = [i+1 for i in range(len(tasks))
                if best[i] == e]
    print("Employee", e+1, "Tasks:", assigned)

print("Minimum Completion Time:", fitness(best), "hours")

output

Employee 1 Tasks: [4, 8]
Employee 2 Tasks: [2, 5, 7]
Employee 3 Tasks: [1, 3, 6]
Minimum Completion Time: 12 hours
