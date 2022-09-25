#!/usr/bin/env python3

# Import json module
import urllib.request, json
from datetime import datetime


baseUrl = "http://www.viaggiatreno.it/infomobilita/resteasy/viaggiatreno/"

stazioneName = "MILANO%20REPUBBLICA"
stazioneDestinazione = "TREVIGLIO"
stazioneUrl = baseUrl + "autocompletaStazione/" + stazioneName
#print(stazioneUrl)
stazioneFull = urllib.request.urlopen(stazioneUrl).read()
#print(stazioneFull)
stazioneCode = (str(stazioneFull).split("|")[1]).split("\\")[0]
#print(stazioneCode)

dataRaw = datetime.now()
data = (dataRaw.strftime("%a %b %d %Y %H:%M:%S")).replace(" ", "%20")
#print(data)

treniurl = baseUrl + "partenze/" + stazioneCode + "/" + data

with urllib.request.urlopen(treniurl) as url:
    treni = json.load(url)
 #   print(treni)


def getTreni(destinazione, valori):
    comdata = filter(lambda i: i['destinazione'] == stazioneDestinazione, treni)
    return [dict(zip(valori, [com[valore] for valore in valori]))
            for com in comdata]

elencoTreni = getTreni(stazioneDestinazione, ['compNumeroTreno', 'compOrarioPartenzaZeroEffettivo', 'ritardo'])
print(elencoTreni)
