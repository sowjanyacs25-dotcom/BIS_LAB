

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


X, y = make_classification(
    n_samples=500,
    n_features=10,
    n_informative=8,
    n_classes=2,
    random_state=42
)

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)


input_size = X.shape[1]
hidden_size = 5
output_size = 1


def sigmoid(x):
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))


def forward_pass(X, weights1, weights2):
    hidden_input = np.dot(X, weights1)
    hidden_output = sigmoid(hidden_input)

    output_input = np.dot(hidden_output, weights2)
    output = sigmoid(output_input)

    return output.ravel()


def compute_fitness(individual):
    predictions = forward_pass(
        X_train,
        individual['w1'],
        individual['w2']
    )

    predictions = (predictions > 0.5).astype(int)

    return accuracy_score(y_train, predictions)


population_size = 20
generations = 50
mutation_rate = 0.1
mutation_strength = 0.1
elite_size = 2

population = []

for _ in range(population_size):
    individual = {
        'w1': np.random.randn(input_size, hidden_size),
        'w2': np.random.randn(hidden_size, output_size)
    }
    population.append(individual)


best_fitness_history = []
average_fitness_history = []

best_individual = None
best_overall_fitness = -1

for generation in range(generations):


    fitness_scores = np.array([
        compute_fitness(individual)
        for individual in population
    ])


    sorted_indices = np.argsort(fitness_scores)[::-1]

    population = [
        population[i] for i in sorted_indices
    ]

    fitness_scores = fitness_scores[sorted_indices]


    best_fitness = fitness_scores[0]
    average_fitness = np.mean(fitness_scores)

    best_fitness_history.append(best_fitness)
    average_fitness_history.append(average_fitness)


    if best_fitness > best_overall_fitness:
        best_overall_fitness = best_fitness

        best_individual = {
            'w1': population[0]['w1'].copy(),
            'w2': population[0]['w2'].copy()
        }

    print(
        f"Generation {generation + 1}: "
        f"Best Fitness = {best_fitness:.4f}, "
        f"Average Fitness = {average_fitness:.4f}"
    )


    new_population = [
        {
            'w1': population[i]['w1'].copy(),
            'w2': population[i]['w2'].copy()
        }
        for i in range(elite_size)
    ]


    while len(new_population) < population_size:


        parent1 = population[
            np.random.randint(0, population_size // 2)
        ]

        parent2 = population[
            np.random.randint(0, population_size // 2)
        ]


        child_w1 = (parent1['w1'] + parent2['w1']) / 2
        child_w2 = (parent1['w2'] + parent2['w2']) / 2


        mask_w1 = np.random.rand(*child_w1.shape) < mutation_rate
        mask_w2 = np.random.rand(*child_w2.shape) < mutation_rate

        child_w1 += (
            np.random.randn(*child_w1.shape)
            * mutation_strength
            * mask_w1
        )

        child_w2 += (
            np.random.randn(*child_w2.shape)
            * mutation_strength
            * mask_w2
        )

        child = {
            'w1': child_w1,
            'w2': child_w2
        }

        new_population.append(child)

    population = new_population

predictions = forward_pass(
    X_val,
    best_individual['w1'],
    best_individual['w2']
)

predictions = (predictions > 0.5).astype(int)

final_accuracy = accuracy_score(y_val, predictions)

print("\nTraining completed!")
print(f"Best Training Fitness: {best_overall_fitness:.4f}")
print(f"Final Validation Accuracy: {final_accuracy:.4f}")


plt.figure(figsize=(10, 5))

plt.plot(
    range(1, generations + 1),
    best_fitness_history,
    label='Best Fitness'
)

plt.plot(
    range(1, generations + 1),
    average_fitness_history,
    label='Average Fitness'
)

plt.title('Fitness Over Generations')
plt.xlabel('Generation')
plt.ylabel('Fitness (Accuracy)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

output

Generation 1: Best Fitness = 0.6275, Average Fitness = 0.5118
Generation 2: Best Fitness = 0.6325, Average Fitness = 0.5434
Generation 3: Best Fitness = 0.6400, Average Fitness = 0.5920
Generation 4: Best Fitness = 0.6650, Average Fitness = 0.6029
Generation 5: Best Fitness = 0.6900, Average Fitness = 0.6307
Generation 6: Best Fitness = 0.7150, Average Fitness = 0.6690
Generation 7: Best Fitness = 0.7300, Average Fitness = 0.6994
Generation 8: Best Fitness = 0.7300, Average Fitness = 0.7130
Generation 9: Best Fitness = 0.7375, Average Fitness = 0.7219
Generation 10: Best Fitness = 0.7400, Average Fitness = 0.7231
Generation 11: Best Fitness = 0.7625, Average Fitness = 0.7273
Generation 12: Best Fitness = 0.7625, Average Fitness = 0.7376
Generation 13: Best Fitness = 0.7625, Average Fitness = 0.7480
Generation 14: Best Fitness = 0.7650, Average Fitness = 0.7441
Generation 15: Best Fitness = 0.7650, Average Fitness = 0.7516
Generation 16: Best Fitness = 0.7675, Average Fitness = 0.7584
Generation 17: Best Fitness = 0.7900, Average Fitness = 0.7629
Generation 18: Best Fitness = 0.7900, Average Fitness = 0.7678
Generation 19: Best Fitness = 0.7925, Average Fitness = 0.7779
Generation 20: Best Fitness = 0.7925, Average Fitness = 0.7769
Generation 21: Best Fitness = 0.8000, Average Fitness = 0.7783
Generation 22: Best Fitness = 0.8000, Average Fitness = 0.7855
Generation 23: Best Fitness = 0.8000, Average Fitness = 0.7870
Generation 24: Best Fitness = 0.8100, Average Fitness = 0.7910
Generation 25: Best Fitness = 0.8100, Average Fitness = 0.7956
Generation 26: Best Fitness = 0.8125, Average Fitness = 0.7910
Generation 27: Best Fitness = 0.8125, Average Fitness = 0.7963
Generation 28: Best Fitness = 0.8125, Average Fitness = 0.7920
Generation 29: Best Fitness = 0.8125, Average Fitness = 0.7969
Generation 30: Best Fitness = 0.8150, Average Fitness = 0.7957
Generation 31: Best Fitness = 0.8150, Average Fitness = 0.7939
Generation 32: Best Fitness = 0.8150, Average Fitness = 0.7964
Generation 33: Best Fitness = 0.8150, Average Fitness = 0.7971
Generation 34: Best Fitness = 0.8150, Average Fitness = 0.7974
Generation 35: Best Fitness = 0.8150, Average Fitness = 0.8030
Generation 36: Best Fitness = 0.8150, Average Fitness = 0.8036
Generation 37: Best Fitness = 0.8175, Average Fitness = 0.8045
Generation 38: Best Fitness = 0.8175, Average Fitness = 0.8070
Generation 39: Best Fitness = 0.8200, Average Fitness = 0.8069
Generation 40: Best Fitness = 0.8200, Average Fitness = 0.8094
Generation 41: Best Fitness = 0.8200, Average Fitness = 0.8017
Generation 42: Best Fitness = 0.8200, Average Fitness = 0.8080
Generation 43: Best Fitness = 0.8250, Average Fitness = 0.8048
Generation 44: Best Fitness = 0.8250, Average Fitness = 0.8071
Generation 45: Best Fitness = 0.8250, Average Fitness = 0.8114
Generation 46: Best Fitness = 0.8250, Average Fitness = 0.8075
Generation 47: Best Fitness = 0.8250, Average Fitness = 0.8127
Generation 48: Best Fitness = 0.8250, Average Fitness = 0.8126
Generation 49: Best Fitness = 0.8250, Average Fitness = 0.8103
Generation 50: Best Fitness = 0.8250, Average Fitness = 0.8140

Training completed!
Best Training Fitness: 0.8250
Final Validation Accuracy: 0.8400
