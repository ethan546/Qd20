#A .py version of rand_dice.ipynb
#Uses command line args as input, if provided

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
import numpy as np
import sys

def handle_input(strg):
    #this func will take an input of the form 3d6p2
    #then split and return calls = 3, size = 6, add = 2
    split = strg.split("d")
    
    #allows for $d20 call
    if split[0] == '':
        split[0] = '1'

    #case for add const
    if "p" in split[1] :
        split2 = split[1].split("p")
        return(int(split[0]),int(split2[0]),int(split2[1]))
    elif "+" in split[1] :
        split2 = split[1].split("+")
        return(int(split[0]),int(split2[0]),int(split2[1]))
    elif "m" in split[1]:
        split2 = split[1].split("m")
        return(int(split[0]),int(split2[0]),-int(split2[1]))
    elif "-" in split[1]:
        split2 = split[1].split("-")
        return(int(split[0]),int(split2[0]),-int(split2[1]))
    
    #no add    
    else:
        return(int(split[0]),int(split[1]),0)


def create_circuit(size):
    #take size as int, build a circuit with equal chances of each state
    qubits = int(np.ceil(np.log2(size)))
    qr = QuantumRegister(qubits,'x')
    cr = ClassicalRegister(qubits,'c')
    qc = QuantumCircuit(qr,cr)       
    for i in range (qubits):
        qc.h(i)        
    qc.measure(qr,cr)
    return qc


def count_to_dec(count):
    #takes result.get_counts() and converts to a decimal result
    strg = str(count)
    split = strg.split("'")
    num = int(split[1],2)
    return (num+1)
    
    
    
def main(inp):
    #take in the roll text and run everything!
    #for external usage, outputs all prints in a list

    #grab input, make sure its valid
    try:
        calls,size,add = handle_input(inp)
    except:
        print("bad input. Plese provide roll in form of 1d20 or 3d6p2.")
        return ["invalid input"]
    
    if size < 2:
        print ("That's not a real dice!!!")
        return ["invalid input"]

    #make quantum circuit and other vars
    out = []
    qc = create_circuit(size)
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    total_roll = add
    array = []
    
    for _ in range (calls):
        reroll = True
        while reroll:
            #sym and run the circuit
            job = simulator.run(compiled_circuit, shots=1)
            result = job.result()
            roll = count_to_dec(result.get_counts())
            
            #reroll if result is too big
            if roll <= size:
                reroll = False
            else:
                continue

            #show each roll individually -- dissabled now
            #if calls > 1:
            #    msg = "d"+str(size)+": "+str(roll)
            #    print (msg)
            #    out.append(msg)

            #nat 20 clause
            if size == 20 and roll == 20:
                msg = "nat 20!!!"
                print (msg)
                out.append(msg)

        total_roll+=roll
        array.append(roll)
    
    msg = "you rolled "+str(inp)+" and got "+str(total_roll)+"!"
    print (msg)
    out.append(msg)
    if calls > 1:
        print (array)
        out.append(array)
    return out


#main call
if __name__ == "__main__":
    if len(sys.argv) == 2:
        roll = sys.argv[1]
    else:
        roll = '1d20'
    main(roll)