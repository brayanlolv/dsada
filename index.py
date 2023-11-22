from flask import Flask,jsonify,request
from scrapping import scraping
from getLOF import isMono
import requests
import json

app = Flask("servidor")
print(app)

chave_riot =  "RGAPI-23df26c8-6ffe-475e-ac69-302be706e516"
get_chall_url = "https://br1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I"





@app.route("/")
def home():
    return "Ola"

    
@app.route("/verperfil")
def teste():
    print("teste")
    res =  isMono("Arthur Lanches")
    if(res == None):
        return "none"

    return jsonify(res)

    monochall = [{
    "leagueId": "9468e29a-a085-3ab8-8d19-d25cc8630618",
    "queueType": "RANKED_SOLO_5x5",
    "tier": "CHALLENGER",
    "rank": "I",
    "summonerId": "_HxWAQV3a31XGE2-1TNAniO4sRxFaxKJssKEcXVMz7DnLoGc6dwije3Qxw",
    "summonerName": "Arthur Lanches",
    "leaguePoints": 1925,
    "wins": 169,
    "losses": 97,
},{
    "leagueId": "9468e29a-a085-3ab8-8d19-d25cc8630618",
    "queueType": "RANKED_SOLO_5x5",
    "tier": "CHALLENGER",
    "rank": "I",
    "summonerId": "_HxWAQV3a31XGE2-1TNAniO4sRxFaxKJssKEcXVMz7DnLoGc6dwije3Qxw",
    "summonerName": "Arthur Lanches",
    "leaguePoints": 1925,
    "wins": 169,
    "losses": 97,
},{
    "leagueId": "9468e29a-a085-3ab8-8d19-d25cc8630618",
    "queueType": "RANKED_SOLO_5x5",
    "tier": "CHALLENGER",
    "rank": "I",
    "summonerId": "_HxWAQV3a31XGE2-1TNAniO4sRxFaxKJssKEcXVMz7DnLoGc6dwije3Qxw",
    "summonerName": "Arthur Lanches",
    "leaguePoints": 1925,
    "wins": 169,
    "losses": 97,
}]
    teste_mc = open("data/teste.txt","w") 
    print(teste_mc)
    teste_mc.write(json.dumps(monochall))
    print(teste_mc)
    return "ola"


def create_challengers_json():
    chall_arch = open("data/challengers.json","w",encoding="utf-8")
    result = requests.get(get_chall_url,headers={ "X-Riot-Token":chave_riot})
    chall_arch.write(result.text)
    # return result.json()


# for i in range(2):#esse [e para teste]
#     player_status =  isMono( all_challengers_obj[i]["summonerName"])

def getchallmono():
    
        print("all mono")
        all_challengers = open("data/challengers.json","r",encoding="utf-8")
        all_challengers = all_challengers.read() 
        all_challengers_obj = json.loads(all_challengers)
        
        chall_arch = open("data/monochall.txt","w",encoding="utf-8")
        chall_arch_j = open("data/monochall.json","w",encoding="utf-8") 
        nomes = []
        for i in all_challengers_obj:
            nomes.append(i["summonerName"])  
             
        result = isMono(nomes)
        
        print(result)
        chall_arch.write(json.dumps(result))
        chall_arch_j.write(json.dumps(result))
        
        
                    
        

        
# create_challengers_json()
# getchallmono()
app.run(port=4000,host="localhost",
       #debug=True
        debug=False
        )
