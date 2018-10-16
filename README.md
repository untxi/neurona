# Tarea Neurona

## Despejar m
y = (-w1/w2) * x - (b/w2)


Despejando m de x * w1 + y * w2 + b dado que y = m * x + b
	 x * w1 + y * w2 + b = 0
	 y * w2 = - x * w1 - b
	 y = (- x * w1 - b) / w2

	 x * w1 + y * w2 + b = 0
	x = (- y * w2 - b) / w1

	 x * w1 + y * w2 + b = 0
	b = - x * w1 - y * w2

	y = m * x + b
	m = (b - y) / x

	m = [(- x * w1 - y * w2) - 
		((- x * w1 - b) / w2))] 
		/
 		[(- y * w2 - b) / w1]
