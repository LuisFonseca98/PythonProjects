import numpy as np
import re

def write2File(ac, dc, filename):

    dc_len_bin = format(int(len(dc)), '0%db'%20)
    ac_len_bin = format(int(len(ac)), '0%db'%20)
    dcac = ac_len_bin + ac + dc_len_bin + dc
    
    tamanhoRestante = 0
    if((len(dcac) + 3) % 8 != 0):
        tamanhoRestante = 8 - ((len(dcac) + 3) % 8)
        
    header = format(tamanhoRestante, '0%db'%3) 
    zerosAdicionais = tamanhoRestante * '0'
    
    stringFinal = header+dcac+zerosAdicionais
    
    binaryArray = re.findall('[01]{8}', stringFinal)
    intArray = [int(i, 2) for i in binaryArray]
    finalArray = np.array(intArray, dtype = 'uint8')
    byteArray = bytearray(finalArray)
    
    
    newFile = open(filename, "wb")
    # write to file
    newFile.write(byteArray)
    newFile.close()



