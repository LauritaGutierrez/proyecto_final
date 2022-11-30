#Librerias necesarias para ejecucion del codigo
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
import Functions as Func
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

simulator = Aer.get_backend('qasm_simulator')

# Este es el circ2 del primer caso es constante

#como nos piden n = 4

circ2 = QuantumCircuit(4, 4)
circ2.barrier(range(4))
circ2.i(range(4))# será el rango que tendrá el circuito
circ2.barrier(range(4))
circ2.measure((0, 1, 2, 3), (3, 2, 1, 0))

compil_circ2 = transpile(circ2, simulator)
comienzo = simulator.run(compil_circ2, desde=1000)
result = comienzo.result()
counts = result.get_counts(circ2)
print(circ2) # al hacerlo será 0000 o 1111
plt.show()
plot_histogram(counts)


# Este es el circ2 del segundo ejemplo es balanceada

#como nos piden n = 4 en este caso
circ2 = QuantumCircuit(4, 4)
circ2 = 0

circ2.barrier(range(4))# la barrera del rango
circ2.cx(0, 3)
circ2.barrier(range(4)) # el rango va de (4,4)
circ2.measure((0, 1, 2, 3), ( 3, 2, 1, 0))

compil_circ2 = transpile(simulator, circ2)
comienzo = simulator.run(compil_circ2, desde=1000)
result = comienzo.result()
counts = result.get_counts(circ2)

print(circ2) # al hacer el print será 0000 o 1111 en este caso
plt.show()
plot_histogram(counts) # en el histograma, gráfica se podrá ver
