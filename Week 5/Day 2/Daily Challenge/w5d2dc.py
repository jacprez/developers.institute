
# Unit class, gene stores a value that is or 1 or 0
# it has one attribute called value that could or 1 or 0
# Gene has one method mutate --> if value is 1 modify it to zero
# else if it is 0 modify it to 1
# Class Chromosome: is composed of a list of Genes
# self.genes = [Gene() for i in range(10)]
# Mutate method in chromosome: loop through the genes and randomly mutate
# r = random.random() (random number between 0 and 1)
# if r > 0.5 --> mutate the gene else don't touch it
# class DNA: is composed of a list of Chromosomes
# self.chromosomes = [Chromosome() for i in range(10)]
# Mutate method in DNA: loop through the chromosomes and randomly mutate
# r = random.random() (random number between 0 and 1)
# if r > 0.5 --> mutate the chromosome else don't touch it

import random

class Gene:
    def __init__(self):
        self.value = random.choice([True, False]) # True = 1 and False = 0

    def mutate(self):
        self.value = not self.value

    def __repr__(self):
        return "1" if self.value else "0"

class Chromosome:
    def __init__(self):
        self.value = [Gene() for i in range(10)]

    def mutate(self):
        for gene in self.value:
            if random.choice([True, False]):
                gene.mutate()

    def __repr__(self):
        return str(self.value)

class DNA():
    def __init__(self):
        self.value = [Chromosome() for i in range(10)]

    def mutate(self):
        for chromosome in self.value:
            if random.choice([True, False]):
                chromosome.mutate()

    def __repr__(self):
        return str(self.value)


class Organism():
    def __init__(self, dna, probability_to_mutate):
        self.dna = dna
        self.probability_to_mutate = probability_to_mutate

    def mutate(self):
        if random.random() <= self.probability_to_mutate:
            self.dna.mutate()

    def __repr__(self):
        return str(self.dna)



# class Evolution():
#     def __init__(self, num_of_organisms):
#         self.population = [Organism(DNA, 0.8) for i in range(num_of_organisms)]
#         self.generations = 0
#
#     def big_bang(self):
#         for organism in self.population:
#             organism.mutate()
#
#     def is_complete(self):
#         for organism in self.population:
#             for dna in organism:


o1 = Organism(DNA(), 1)
print(o1)


