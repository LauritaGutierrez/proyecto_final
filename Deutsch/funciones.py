#Librerias necesarias para ejecucion del codigo
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
#import Functions as Func
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# Si la funcion es balanceada o no, recibe una funcion f

def balanceada(f):
    return f(0) != f(1)
# retorna el valor de verdad

# para poder simular la interacción:
simulator = Aer.get_backend('qasm_simulator')

# qubits
circ1 = QuantumCircuit(2,1)
circ1.x(1)
circ1.h(range(2))
circ1.draw(output= 'mpl')

# Para la primera función

circ1 = QuantumCircuit(2, 2)
circ1.barrier()
circ1.cnot(0, 1)
circ1.barrier() #Es una barrera
circ1.draw(output = 'mpl')

circ1.measure([0, 1], [1, 0]) # tomo los bits
compil_circ1 = transpile(circ1, simulator)
comienzo = simulator.run(compil_circ1, desde=1000)
result = comienzo.result()
counts = result.get_counts(circ1)

print(circ1)
plot_histogram(counts)
plt.show()

# Segunda función

circ1 = QuantumCircuit(2, 2)
circ1.x(0)
circ1.x(1)
circ1.barrier()
circ1.x(0)
circ1.cnot(0, 1)
circ1.x(0)
circ1.barrier()
circ1.draw(output = 'mpl')

circ1.measure([0,1], [1,0]) # tomo los bits
compil_circ1 = transpile(circ1, simulator)
comienzo = simulator.run(compil_circ1, desde=1000)

result = comienzo.result()
counts = result.get_counts(circ1)

print(circ1)
plot_histogram(counts)
plt.show()

#Tercer función

circ1.x(0)
circ1.x(1)
circ1.barrier()
circ1.x(1)
circ1.barrier() #Es una barrera

circ1.measure([0,1], [1,0])
compiled_circuit = transpile(circ1, simulator)
comienzo = simulator.run(compil_circ1, desde=1000)

result = comienzo.result()
counts = result.get_counts(circ1)
print(circ1)
plot_histogram(counts)
plt.show()

#Cuarta funcion

circ1.x(0)
circ1.x(1)
circ1.barrier()
circ1.id(0)
circ1.id(1)
circ1.barrier() #Es una barrera

circ1.measure([0,1], [1,0])
compil_circ1 = transpile(circ1, simulator)
comienzo = simulator.run(compil_circ1, desde=1000)
result = comienzo.result()
counts = result.get_counts(circ1)

print(circ1)
# dibujará en un histograma o en la grafica
plot_histogram(counts)
plt.show()

