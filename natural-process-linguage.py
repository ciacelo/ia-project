import re
from operator import itemgetter

regex = "[a-zA-ZçÇãÃõÕáÁéÉíÍóÓúÚâÂêÊîÎôÔûÛàÀ']+"
texto = open('shakespeare.txt').read().lower()

textoRegex = re.findall(regex, texto)

def bigrama(palavra, palavraAnterior):
    
    palavraCont = 0
    palavraAnteriorCont = 0

    for i in range(len(textoRegex)):
        
        if(palavraAnterior == textoRegex[i]):
            palavraAnteriorCont += 1

        if(i < len(textoRegex)):
            if((palavraAnterior == textoRegex[i]) and (palavra == textoRegex[i+1])):
                palavraCont += 1            
     
    probabilidade = palavraCont/palavraAnteriorCont
    return probabilidade



def trigrama(palavra, palavraAnterior, palavraAnterior2):

    palavraCont = 0
    palavraAnteriorCont = 0
    palavraAnterior2Cont = 0

    for i in range(len(textoRegex)):
     

        if(i < len(textoRegex)):
            if((palavraAnterior2 == textoRegex[i]) and (palavraAnterior == textoRegex[i+1])):
                palavraAnterior2Cont += 1     

        if(i < len(textoRegex)-1):
            if((palavraAnterior2 == textoRegex[i]) and (palavraAnterior == textoRegex[i+1]) and (palavra == textoRegex[i+2])):
                palavraCont += 1     

    probabilidade = palavraCont/palavraAnterior2Cont
    return probabilidade


    

def sugestaoBigrama(frase):

    fraseUsuario = frase.lower()
    fraseRegulada = re.findall(regex, fraseUsuario)
    
    palavra = fraseRegulada[-1]
    palavraAnterior = fraseRegulada[-2]
    palavrasMaiorProbabilidade = []

    listaPalavraProbab = []
    listaUltimaPalavra = list(set(re.findall(palavra + " " + regex, texto)))
    for i in listaUltimaPalavra:
        palavraEmSequencia = i.split(' ')[1]
        fraseComPalavraSeq = (palavraAnterior+" "+palavra+" "+palavraEmSequencia).split()
        probabilidadePalavraSeq = bigrama(fraseComPalavraSeq[-1], fraseComPalavraSeq[-2])
        listaPalavraProbab.append([palavraEmSequencia,probabilidadePalavraSeq])

    palavrasProbabilidade = sorted(listaPalavraProbab, key=itemgetter(1), reverse=True)[:3]
    print(palavrasProbabilidade)
    fraseComSugestao = []
    for palavraSeq in palavrasProbabilidade:
        palavrasMaiorProbabilidade.append(palavraSeq[0])
        fraseComSugestao.append((palavraAnterior+ " "+ palavra + " " +palavraSeq[0]))
    
    return(fraseComSugestao, palavrasMaiorProbabilidade)


def sugestaoTrigrama(frase):

    fraseUsuario = frase.lower()
    fraseRegulada = re.findall(regex, fraseUsuario)
    
    palavra = fraseRegulada[-1]
    palavraAnterior = fraseRegulada[-2]
    palavraAnterior2 = fraseRegulada[-3]
    palavrasMaiorProbabilidade = []

    listaPalavraProbab = []
    listaUltimaPalavra = list(set(re.findall(palavra + " " + palavraAnterior + " " + regex, texto)))
    for i in listaUltimaPalavra:
        palavraEmSequencia = i.split(' ')[2]
        fraseComPalavraSeq = (palavraAnterior+" "+palavra+" "+palavraEmSequencia).split()
        probabilidadePalavraSeq = bigrama(fraseComPalavraSeq[-1], fraseComPalavraSeq[-2])
        listaPalavraProbab.append([palavraEmSequencia,probabilidadePalavraSeq])

    palavrasProbabilidade = sorted(listaPalavraProbab, key=itemgetter(1), reverse=True)[:3]
    print(palavrasProbabilidade)
    fraseComSugestao = []
    for palavraSeq in palavrasProbabilidade:
        palavrasMaiorProbabilidade.append(palavraSeq[0])
        fraseComSugestao.append((palavraAnterior+ " "+ palavra + " " +palavraSeq[0]))
    
    return(fraseComSugestao, palavrasMaiorProbabilidade)

#sugestaoBigrama("Thou mightst as")    

print(sugestaoBigrama("What answer makes"))
print(sugestaoTrigrama("And here I"))