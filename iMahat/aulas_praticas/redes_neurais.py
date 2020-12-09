import numpy as np

def sigmoide(x, deriv = False):
    if ( deriv == True):
        return x * (1-x)
    return 1/(1+np.exp(-x))
    
X = np.array ([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
               
y = np.array([[0,1,1,1]]).T

np.random.seed(1)

sinapse = 2 * np.random.random((3,1)) -1

for iter in range (100000):
    
    l0 = X
    l1 = sigmoide (np.dot(l0, sinapse))
    
    l1_erro = y - l1
    
    l1_delta = l1_erro * sigmoide (l1, True)
    
    sinapse += np.dot(l0.T, l1_delta)
    
print("Saida após treinamento: ")
print(l1)