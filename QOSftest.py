#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question1
#import the necessary packages
from qiskit import *
from qiskit.tools.monitor import job_monitor
from qiskit.quantum_info import Statevector, partial_trace
from qiskit.visualization import plot_histogram
from qiskit.visualization import plot_state_qsphere
import random
backend = Aer.get_backend('qasm_simulator')


# In[2]:


#define the basic circuit
qr = QuantumRegister(2,'qu')
a = QuantumRegister(4,'anc')
cr= ClassicalRegister(2,'cl')
circuit = QuantumCircuit(qr,a,cr)
circuit.h(0)
circuit.barrier()
circuit.draw("mpl")


# In[3]:


#question2
#introduce error gate for the cases XZ, XI and IZ
r = random.randint(1,40)
if r>20:
    print('The noise is: XZ')
    circuit.x(0)
    circuit.z(1)
elif r<=20 and r>10:
    print('The noise is: ZI')
    circuit.x(0)
else:
    print('The noise is: IX')
    circuit.z(1)
circuit.barrier()
circuit.draw("mpl")


# In[4]:


#question3
#Remove the bit-flip correction 
"""
circuit.cx(qr[0],a[0])
circuit.cx(qr[0],a[1])
circuit.ccx(a[1],a[0],qr[0])
"""
circuit.barrier()

#Remove the phase-flip correction 
"""
circuit.h(1)
circuit.cx(qr[1],a[2])
circuit.cx(qr[1],a[3])
circuit.ccx(a[3],a[2],qr[1])
circuit.h(1)
"""
circuit.barrier()
circuit.cx(0,1)
circuit.draw("mpl")


# In[5]:


#question 4
# Do measurements
circuit.measure(qr,cr)
job = execute(circuit, backend, shots=1024)
job_monitor(job)
counts = execute(circuit,backend).result().get_counts()
print(counts)
plot_histogram(counts)


# In[ ]:




