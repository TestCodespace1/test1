# -*- coding: utf-8 -*-
""" Relative Häufigkeit mit einem regelmäßigen Würfel eine gerade
Zahl zu Würfeln als Funktion der Anzahl von Versuchen
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
SMALL_SIZE = 14
matplotlib.rc('font', size=SMALL_SIZE)
matplotlib.rc('axes', titlesize=SMALL_SIZE)

# Generate dataset with N samples
N = 10000
n = np.arange(N)+1
x = np.random.randint(0, 2, N)
xc = np.cumsum(x)
xm = np.divide(xc, n)

# Plot results
fig, ax = plt.subplots(figsize=(7, 5))
ax.semilogx(n, xm, 'C0', linewidth=2)
ax.grid(True)
ax.axis([1, N, 0, 1])
ax.set_xlabel('Versuchsumfang N')
ax.set_ylabel('Relative Häufigkeit h(A)')
ax.set_yticks([0, 0.5, 1], minor=False)

# Format and save file
plt.tight_layout()
filename = sys.argv[0].split('\\')[-1].split('.')[0]
plt.savefig(filename+'.pdf')
plt.savefig(filename+'.png')
