# -*- coding: utf-8 -*-

""" Auswertung zum Beispiel Sensordiagnose:
Wahrscheinlichkeit mit der ein Sensor wirklich defekt ist,
wenn er mit einer Diagnosefunktion als defekt eingestuft wurde
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
SMALL_SIZE = 14
matplotlib.rc('font', size=SMALL_SIZE)
matplotlib.rc('axes', titlesize=SMALL_SIZE)

# Generate dataset
PD = 1e-4
PND = 1-1e-4
PED_D = 0.9999
PED_ND = 0.0002

x = np.logspace(-4, 0, 50)
P_D_ED = PED_D*PD / (PED_D*PD+x/100*PND)

# Plot results
fig, ax = plt.subplots(figsize=(7, 5))
ax.semilogx(x, P_D_ED, 'C0', linewidth=2)
ax.semilogx(0.02, 0.333, 'C0o', markersize=6)
ax.grid(True)
ax.axis([1e-4, 1, 0, 1])
ax.set_xlabel("Wahrscheinlichkeit P(B|A') / %")
ax.set_ylabel('Aussagesicherheit P(A|B) / %')
ax.text(0.04, 0.4, "P(B|A') = 0.02 %\n P(A|B) = 33.3 %",
        bbox={'facecolor': 'white', 'edgecolor': 'white', 'alpha': 1, 'pad': 5}
        )

# Format and save file
plt.tight_layout()
filename = sys.argv[0].split('\\')[-1].split('.')[0]
plt.savefig(filename+'.pdf')
plt.savefig(filename+'.png')
