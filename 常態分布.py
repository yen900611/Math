import random
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import scipy.stats as stats
import math

times = 1000000
N = 100
p = 0.5
results = [0] * (N+1)

for i in tqdm(range(times)):
    c = 0
    for j in range(N):
        if random.random() > 1-p:
            c += 1
    results[c] += 1


y_pos = np.arange(len(results))
plt.bar(y_pos, results, align='center', width=0.95, color = 'g', alpha = 0.7)

mu = N*p
variance = N*p*(1-p)
sigma = math.sqrt(variance)

for i in range(1,4):
    sum = 0
    for j in range(int(mu-i*sigma), int(mu+i*sigma)):
        sum += results[j]
    probability = sum / times
    print(f'Probability within {i}-sigma is {probability}')

x = np.linspace(0, N+1, N+1)
plt.plot(x, stats.norm.pdf(x, mu, sigma)*times)

plt.xlabel('Heads')
plt.ylabel('Counts')
plt.title(f'Toss of {N} coins')
plt.show()