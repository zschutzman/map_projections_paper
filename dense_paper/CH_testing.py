import numpy as np 
from math import *

alpha2 = 1
alpha1 = alpha2/2
beta2 = alpha2/2
beta1 = beta2/2

CH_A = 1-(1-cos(alpha1))/(1-cos(alpha2))
CH_B = 1-(1-cos(beta1))/(1-cos(beta2))

CH_pA = 1- (tan(alpha1)**2)/(tan(alpha2)**2)
CH_pB = 1- (tan(beta1)**2)/(tan(beta2)**2)
print('CH scores before: A:' + str(CH_A) + ' B:' + str(CH_B))
print('CH scores after: A:' + str(CH_pA) + ' B:' + str(CH_pB))
score_stay = (CH_A>CH_B and CH_pA>CH_pB)

if not score_stay:
    print('scores reversed')

