def funcion(numero):
    if numero < 1:
        raise Exception(f'{numero} es menor a 1')
    
    print(str(numero) + ' es mayor o igual que 1')

funcion(2)

import traceback

try:
    A = 1
    #raise Exception('Esto es un error que va a ir al error_log.txt')
except:
    errorFile = open('error_log.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Error en log')

import logging
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG, format="%(asctime)s - %(levelname)s %(message)s")
#logging.disable(logging.CRITICAL) # Desactiva la impresion de los logs

def factorial(n):
    logging.debug("Empezo factorial")
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug(str(i))
    
    logging.debug(str(total))
    return total

logging.debug("Llamo a la funcion")
print(factorial(5))
logging.debug("Termino a la funcion")