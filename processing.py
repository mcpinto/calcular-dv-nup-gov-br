def getDV(seq, ano):
  NUPunidade = [2, 3, 4, 2, 2] # código da UNILA como vetor (5 dígitos)
  NUPsequencial = [int(d) for d in '{:06d}'.format(seq)] # sequencial do protocolo como vetor (6 dígitos)
  NUPano = [int(d) for d in '{:04d}'.format(ano)] # ano do protocolo como vetor (4 dígitos)
  NUPV = list(reversed(NUPano)) + list(reversed(NUPsequencial)) + list(reversed(NUPunidade)) # vetor com dígitos invertidos
  dv1 = (11 - ( sum([(i+2)*NUPV[i] for i in range(len(NUPV))]) % 11 )) % 10 # cálculo DV1
  NUPV.insert(0, dv1) # inserir DV1 no vetor
  dv2 = (11 - ( sum([(i+2)*NUPV[i] for i in range(len(NUPV))]) % 11 )) % 10 # cálculo DV2
  return 10*dv1 + dv2