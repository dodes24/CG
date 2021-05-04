#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt

wt = open('wt.extract', 'r').readlines()
tumor = open('tumor.extract', 'r').readlines()

wildp = 0
tump = 0

x = []
y = []

while wildp < len(wt) or tump < len(tumor):
    (wposition, wcoverage) = [int(float(x)) for x in
                              wt[wildp].strip().split('\t')]
    (tposition, tcoverage) = [int(float(x)) for x in
                              tumor[tump].strip().split('\t')]

    if wposition < tposition:
        wildp += 1
        continue
    if tposition < wposition:
        tump += 1
        continue

    wildp += 1
    tump += 1

    if wcoverage == 0 or tcoverage == 0:
        continue

    amount = math.log2(tcoverage / wcoverage)
    x.append(tposition)
    y.append(amount)

plt.axhline(y=0, color='black', linestyle='--')
plt.ylabel('Log2 read-depth ratio')
plt.title('Read depth plot')
plt.xlabel('chrX')
plt.figure(figsize=(15,3))
plt.scatter(x, y, s=0.025, c='green')
plt.savefig('rdp_plot.png')

