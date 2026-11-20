# Creating array from scratch :

import numpy as np
# zeros array : 
zeros=np.zeros((3,4))
print("Zeros array : \n",zeros)

# ones array :
ones=np.ones((4,4))
print("Ones array : \n",ones)


# full array :
full = np.full((2,2),7)
print("Full array : \n",full)

# random array :
random=np.random.random((2,3))
print("Random array : \n",random)

# sequence array :
sequence=np.arange(0,11,2)
print(sequence)