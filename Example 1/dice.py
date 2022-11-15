import numpy as np
N=10000 #Size of sample
P=[]
N_success = 0
for i in range(1, N+1):
	#Generate 8 dices (1 to 6)
	br1 = np.random.choice(6, size = 8, replace = True)
	br1 += 1
	br2 = np.random.choice(6, size = 8, replace = True)
	br2 += 1
    #End of generating.
    #This code example calculates the probability that out of 8 rolls of 2 dice exactly 7 times the sum was greater than 5
	b = ((br1+br2) > 5)
	if((np.sum(b) == 7)):
		N_success += 1
probability = N_success/N
print(probability)