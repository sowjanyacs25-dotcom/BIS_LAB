

import random
import math

def f(x):
    return sum(xi ** 2 for xi in x)

def pso(num_particles, dimensions, max_iterations,
        c1=2.0, c2=2.0, w=0.7,
        lower_bound=-10, upper_bound=10):

    particles = []

    for _ in range(num_particles):
        position = [
            random.uniform(lower_bound, upper_bound)
            for _ in range(dimensions)
        ]

        velocity = [
            random.uniform(-1, 1)
            for _ in range(dimensions)
        ]

        particles.append({
            "position": position,
            "velocity": velocity,
            "pbest": position.copy(),
            "pbest_value": f(position)
        })

    gbest = min(
        particles,
        key=lambda p: p["pbest_value"]
    )["pbest"].copy()

    gbest_value = f(gbest)

    for iteration in range(max_iterations):

        for particle in particles:

            current_value = f(particle["position"])

            if current_value < particle["pbest_value"]:
                particle["pbest"] = particle["position"].copy()
                particle["pbest_value"] = current_value

        best_particle = min(
            particles,
            key=lambda p: p["pbest_value"]
        )

        if best_particle["pbest_value"] < gbest_value:
            gbest = best_particle["pbest"].copy()
            gbest_value = best_particle["pbest_value"]

        for particle in particles:

            position = particle["position"]
            velocity = particle["velocity"]
            pbest = particle["pbest"]

            for d in range(dimensions):

                r1 = random.random()
                r2 = random.random()

                velocity[d] = (
                    w * velocity[d]
                    + c1 * r1 * (pbest[d] - position[d])
                    + c2 * r2 * (gbest[d] - position[d])
                )

            for d in range(dimensions):
                position[d] += velocity[d]

                position[d] = max(
                    lower_bound,
                    min(position[d], upper_bound)
                )

        print(
            f"Iteration {iteration + 1}: "
            f"Best = {gbest_value:.6f}, "
            f"Position = {gbest}"
        )

    return gbest, gbest_value


best_position, best_value = pso(
    num_particles=30,
    dimensions=2,
    max_iterations=100
)

print("\nFinal Result")
print("Best Position:", best_position)
print("Best Value:", best_value)


output

Iteration 1: Best = 1.418764, Position = [-0.8995012152880548, -0.780808525032807]
Iteration 2: Best = 0.282300, Position = [-0.27816617804963606, 0.4526850768828554]
Iteration 3: Best = 0.282300, Position = [-0.27816617804963606, 0.4526850768828554]
Iteration 4: Best = 0.282300, Position = [-0.27816617804963606, 0.4526850768828554]
Iteration 5: Best = 0.282300, Position = [-0.27816617804963606, 0.4526850768828554]
Iteration 6: Best = 0.102514, Position = [-0.03724425968625056, 0.31800525911954725]
Iteration 7: Best = 0.102514, Position = [-0.03724425968625056, 0.31800525911954725]
Iteration 8: Best = 0.102514, Position = [-0.03724425968625056, 0.31800525911954725]
Iteration 9: Best = 0.102514, Position = [-0.03724425968625056, 0.31800525911954725]
Iteration 10: Best = 0.102514, Position = [-0.03724425968625056, 0.31800525911954725]
Iteration 11: Best = 0.036477, Position = [0.14451618772750197, 0.12486878169699456]
Iteration 12: Best = 0.036477, Position = [0.14451618772750197, 0.12486878169699456]
Iteration 13: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 14: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 15: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 16: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 17: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 18: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 19: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 20: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 21: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 22: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 23: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 24: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 25: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 26: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 27: Best = 0.005183, Position = [-0.051986100970910804, -0.049805269493274906]
Iteration 28: Best = 0.000449, Position = [-0.000973893173220719, 0.021158043918858394]
Iteration 29: Best = 0.000449, Position = [-0.000973893173220719, 0.021158043918858394]
Iteration 30: Best = 0.000449, Position = [-0.000973893173220719, 0.021158043918858394]
Iteration 31: Best = 0.000449, Position = [-0.000973893173220719, 0.021158043918858394]
Iteration 32: Best = 0.000346, Position = [0.006253795729342093, 0.017519459094588075]
Iteration 33: Best = 0.000346, Position = [0.006253795729342093, 0.017519459094588075]
Iteration 34: Best = 0.000346, Position = [0.006253795729342093, 0.017519459094588075]
Iteration 35: Best = 0.000346, Position = [0.006253795729342093, 0.017519459094588075]
Iteration 36: Best = 0.000346, Position = [0.006253795729342093, 0.017519459094588075]
Iteration 37: Best = 0.000346, Position = [0.006253795729342093, 0.017519459094588075]
Iteration 38: Best = 0.000346, Position = [0.006253795729342093, 0.017519459094588075]
Iteration 39: Best = 0.000346, Position = [0.006253795729342093, 0.017519459094588075]
Iteration 40: Best = 0.000346, Position = [0.006253795729342093, 0.017519459094588075]
Iteration 41: Best = 0.000156, Position = [0.000380948183908901, 0.012493062193131937]
Iteration 42: Best = 0.000042, Position = [0.0023909845859286876, 0.006055903632203775]
Iteration 43: Best = 0.000017, Position = [0.003798010067342538, 0.0015498926395540622]
Iteration 44: Best = 0.000017, Position = [0.003798010067342538, 0.0015498926395540622]
Iteration 45: Best = 0.000017, Position = [0.003798010067342538, 0.0015498926395540622]
Iteration 46: Best = 0.000017, Position = [0.003798010067342538, 0.0015498926395540622]
Iteration 47: Best = 0.000017, Position = [0.003798010067342538, 0.0015498926395540622]
Iteration 48: Best = 0.000011, Position = [0.002437515815437923, 0.0021885829769072006]
Iteration 49: Best = 0.000011, Position = [0.002437515815437923, 0.0021885829769072006]
Iteration 50: Best = 0.000011, Position = [0.002437515815437923, 0.0021885829769072006]
Iteration 51: Best = 0.000007, Position = [0.001959525472422956, 0.001742970254534056]
Iteration 52: Best = 0.000005, Position = [0.0007678059566531951, 0.0020266152864671268]
Iteration 53: Best = 0.000005, Position = [0.0007678059566531951, 0.0020266152864671268]
Iteration 54: Best = 0.000004, Position = [0.0006278853218302808, 0.001962646158100087]
Iteration 55: Best = 0.000004, Position = [0.0006278853218302808, 0.001962646158100087]
Iteration 56: Best = 0.000004, Position = [0.0006278853218302808, 0.001962646158100087]
Iteration 57: Best = 0.000004, Position = [0.00022694916555093293, 0.0018691355929286843]
Iteration 58: Best = 0.000003, Position = [-0.00011344659179300437, 0.0016625018987450255]
Iteration 59: Best = 0.000002, Position = [-0.0003517236219337604, 0.0015178583128164643]
Iteration 60: Best = 0.000002, Position = [-0.0005185175430322897, 0.0014166078026664715]
Iteration 61: Best = 0.000002, Position = [-0.0006352732878012603, 0.0013457324455614765]
Iteration 62: Best = 0.000002, Position = [-0.0007170023091395396, 0.0012961196955879799]
Iteration 63: Best = 0.000002, Position = [0.0013153121323143668, -0.00042106398411341874]
Iteration 64: Best = 0.000002, Position = [0.0013153121323143668, -0.00042106398411341874]
Iteration 65: Best = 0.000002, Position = [0.0013153121323143668, -0.00042106398411341874]
Iteration 66: Best = 0.000002, Position = [0.0013153121323143668, -0.00042106398411341874]
Iteration 67: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 68: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 69: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 70: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 71: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 72: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 73: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 74: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 75: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 76: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 77: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 78: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 79: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 80: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 81: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 82: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 83: Best = 0.000000, Position = [-0.00019855028498775868, -0.00020664782640792258]
Iteration 84: Best = 0.000000, Position = [9.311338455347893e-05, -0.0001113448781302071]
Iteration 85: Best = 0.000000, Position = [9.311338455347893e-05, -0.0001113448781302071]
Iteration 86: Best = 0.000000, Position = [9.311338455347893e-05, -0.0001113448781302071]
Iteration 87: Best = 0.000000, Position = [9.311338455347893e-05, -0.0001113448781302071]
Iteration 88: Best = 0.000000, Position = [9.311338455347893e-05, -0.0001113448781302071]
Iteration 89: Best = 0.000000, Position = [-0.0001351162712634426, -6.308193631162653e-06]
Iteration 90: Best = 0.000000, Position = [-0.0001351162712634426, -6.308193631162653e-06]
Iteration 91: Best = 0.000000, Position = [-0.0001351162712634426, -6.308193631162653e-06]
Iteration 92: Best = 0.000000, Position = [-0.0001351162712634426, -6.308193631162653e-06]
Iteration 93: Best = 0.000000, Position = [-0.0001351162712634426, -6.308193631162653e-06]
Iteration 94: Best = 0.000000, Position = [-0.0001351162712634426, -6.308193631162653e-06]
Iteration 95: Best = 0.000000, Position = [8.030127056996928e-05, 2.2383561969523114e-05]
Iteration 96: Best = 0.000000, Position = [8.030127056996928e-05, 2.2383561969523114e-05]
Iteration 97: Best = 0.000000, Position = [8.030127056996928e-05, 2.2383561969523114e-05]
Iteration 98: Best = 0.000000, Position = [8.030127056996928e-05, 2.2383561969523114e-05]
Iteration 99: Best = 0.000000, Position = [8.030127056996928e-05, 2.2383561969523114e-05]
Iteration 100: Best = 0.000000, Position = [8.030127056996928e-05, 2.2383561969523114e-05]

Final Result
Best Position: [8.030127056996928e-05, 2.2383561969523114e-05]
Best Value: 6.9493179015948955e-09
