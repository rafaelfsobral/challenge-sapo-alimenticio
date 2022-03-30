#System requirements
from flask import Flask
import glob 
import errno 
import re
import pandas as pd
import json

#Created an instance of Flask and saved in the app variable
app = Flask(__name__)

#Get a list of files that match a specified pattern within a specified directory
path = 'data/*.txt' 
files = glob.glob(path) 

vetor = []

#Creating an array with file contents
for name in files: 
    try: 
        with open(name, encoding="Utf-8") as f: 
                for n in f.readlines():
                    if (n.__contains__('NOME') | n.__contains__('------')):
                        continue
                    else:
                        if(n.__contains__(',')):
                            n = n.replace(',','')
                    vetor.append(re.sub('\\s+\s',',', n.replace('\n','')).split(","))
    except IOError as exc: 
        if exc.errno != errno.EISDIR: 
            raise 

vetorJson = []
#Create an array with dictionaries
for indice in range(len(vetor)):
    coluna = 0
    infoProdutos = {'Nome':vetor[indice][coluna], 
                    'Quantidade':vetor[indice][coluna+1],
                    'Proteínas':vetor[indice][coluna+2],
                    'Carboidratos':vetor[indice][coluna+3],
                    'Gorduras':vetor[indice][coluna+4]
    }
    vetorJson.append(infoProdutos)

#Format to JSON String
json_string = json.dumps(vetorJson, ensure_ascii=False)

#Format to list for Pandas DataFrame
json_list = json.loads(json_string)

listaProdutoComMaisProteinas = []
listaProdutoComMaisCarboidratos = []
listaProdutoComMaisGorduras = []

#Configuring the Pandas DataFrame with the data tabularly aligned in rows and columns
df = pd.DataFrame(json_list, columns = ['Nome', 'Quantidade', 'Proteínas', 'Carboidratos', 'Gorduras'] )

#Ordering the fields as requested for each category and converting to json
dfProdutoComMaisProteinas = df.sort_values(by=['Proteínas'], ascending=False).to_json(orient = 'records',force_ascii=False)
dfProdutoComMaisCarboidratos = df.sort_values(by=['Carboidratos'], ascending=False).to_json(orient = 'records',force_ascii=False)
dfProdutoComMaisGorduras = df.sort_values(by=['Gorduras'], ascending=False).to_json(orient = 'records',force_ascii=False)

#API Products Routes
@app.route("/produtosproteinas")
def produtosproteinas():
    return {"produtos": dfProdutoComMaisProteinas}

@app.route("/produtoscarboidratos")
def produtoscarboidratos():
    return {"produtos": dfProdutoComMaisCarboidratos}

@app.route("/produtosgorduras")
def produtosgorduras():
    return {"produtos": dfProdutoComMaisGorduras}

if __name__ == "__main__":
    app.run(debug=True)