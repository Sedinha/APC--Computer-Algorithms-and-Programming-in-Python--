def fNaoRecursivo(n):
  antePenultimo = 0
  penultimo = 1

  if(n == 1 or n == 0):
    return n

  i=1
  while(i<n):
    resultado = penultimo+antePenultimo
    antePenultimo = penultimo
    penultimo = resultado
    i+=1
  return resultado

fNaoRecursivo(10)