import json
import pandas as pd

def loadJson(fileName):
  with open(fileName) as f1:
  	data1 = json.load(f1)
  	return data1

#./data/webs/neg/
#bash: for n in *; do printf "'%s',\n" "$n"; done
dataPath='./data/spanish/webs'

negatives=[
	'ar.com.guiaoleo.activity.json',
	'ar.com.mobatio.lanacion.club.json',
	'ar.gob.buenosaires.comollego.json',
	'com.dropbox.android.json',
	'com.gm.despegar.json',
	'com.google.android.apps.finance.json',
	'com.google.android.apps.translate.json',
	'com.google.android.gm.json',
	'com.google.android.googlequicksearchbox.1.json',
	'com.google.android.googlequicksearchbox.2.json',
	'com.google.android.music.json',
	'com.hoyts.json',
	'com.king.candycrushsaga.json',
	'com.mercadolibre.json',
	'com.mobilenik.mobilebanking.individuos.json',
	'com.mobisystems.editor.office_registered.json',
	'com.overflow.cinemark.activity.json',
	'org.microemu.android.model.common.VTUserApplicationLINKMB.json'
]

positives=[
	'ar.com.guiaoleo.activity.json',
	'ar.com.mobatio.lanacion.club.json',
	'ar.gob.buenosaires.comollego.json',
	'com.dropbox.android.json',
	'com.gm.despegar.json',
	'com.google.android.apps.finance.json',
	'com.google.android.apps.translate.json',
	'com.google.android.gm.json',
	'com.google.android.googlequicksearchbox.1.json',
	'com.google.android.googlequicksearchbox.2.json',
	'com.google.android.music.json',
	'com.hoyts.json',
	'com.king.candycrushsaga.json',
	'com.mercadolibre.json',
	'com.mobilenik.mobilebanking.individuos.json',
	'com.mobisystems.editor.office_registered.json',
	'com.overflow.cinemark.activity.json',
	'org.microemu.android.model.common.VTUserApplicationLINKMB.json'
]

negatives_full=[]
positives_full=[]

#Concateno los arrays en uno solo NEGATIVOS
for data in negatives:
  file=dataPath+'/neg/'+data
  print("Loading:"+file)
  negatives_full.extend(loadJson(file))

#Concateno los arrays en uno solo POSITIVOS
for data in positives:
  file=dataPath+'/pos/'+data
  print("Loading:"+file)
  positives_full.extend(loadJson(file))

#Bajo a un archivo NEGATIVOS
print("Generando dump negativos...")
with open('./data/spanish/spanish_negatives.json', 'w') as outfile:
    json.dump(negatives_full, outfile)

#Bajo a un archivo POSTIVIOS
print("Generando dump positivos...")
with open('./data/spanish/spanish_positives.json', 'w') as outfile:
    json.dump(positives_full, outfile)

print("Fin!")