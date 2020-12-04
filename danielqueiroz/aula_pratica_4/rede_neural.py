import numpy as np

def sigmoide(x, deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))

X=np.array([[0,0,1],
		    [0,1,1],
		    [1,0,1],
		    [1,1,1]])

y=np.array([[0],
			[1],
			[1],
			[0]])

np.random.seed(1)

sinapse0= 2*np.random.random((3,4))-1
sinapse1= 2*np.random.random((4,1))-1

for j in range (100000):

	k0=X
	k1=sigmoide(np.dot(k0,sinapse0))
	k2=sigmoide(np.dot(k1,sinapse1))
	k2_erro = y - k2
    if (j % 10000) == 0:
        print "Erro: " + str(np.mean(np.abs(k2_erro)))

    k2_delta = k2_error * nonlin(k2, deriv=True)

    k1_error = k2_delta.dot(sinapse1.T)

    k1_delta = k1_error * nonlin(k1, deriv=True)

    syn1 += k1.T.dot(k2_delta)
    syn0 += k0.T.dot(k1_delta)

print k2
