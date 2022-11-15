import numpy as np
N=10000 #Size of sample
P=[]
N_success = 0
for i in range(1, N+1):
	#An example of a task where we throw dice 12 times and we need to calculate the probability that a number less than 3 rolls exactly 4 times.
	kockica = np.random.choice(6, size = 12, replace = True)
	kockica += 1
	temp = 0
	for b in kockica:
		if(b < 3):
			temp += 1
	if(temp == 4):
		N_success += 1
	
probability = N_success/N
print(probability)