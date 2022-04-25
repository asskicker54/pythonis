import numpy as np

table = np.genfromtxt("./data/ABBREV.csv", delimiter=";", dtype=None, names=True, encoding="utf8")

maxK = table[np.argmax(table['Energ_Kcal'])]['Shrt_Desc']
print('1)', maxK)

maxS = table[np.argmax(table['Sugar_Tot_g'])]['Shrt_Desc']
print('2)', maxS)

maxP = table[np.argmax(table['Protein_g'])]['Shrt_Desc']
print('3)', maxP)

maxC = table[np.argmax(table['Vit_C_mg'])]['Shrt_Desc']
print('4)', maxC)