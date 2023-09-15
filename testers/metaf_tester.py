from metar import Metar
print('Actual')
metaf = "METAR SBBR 010000Z 28004KT 9999 FEW045 20/17 Q1012="
obs = Metar.Metar(metaf)
print(obs.string())

print('Prediction')
metaf = "METAR SBGL 021400Z 09014KT 9999  -TSRA  OVC033 FEW030CB 30/20 Q1012=\n"
obs = Metar.Metar(metaf)
print(obs.string())
