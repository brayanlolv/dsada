
from getLOF import isMono
import json 


teste = [    
     {
        'leagueId': '9468e29a-a085-3ab8-8d19-d25cc8630618',
        'queueType': 'RANKED_SOLO_5x5',
        'tier': 'CHALLENGER',
        'rank': 'I',
        'summonerId': 'OxrRjRLROuFeiM9jWRup3nP0LeaQkH3JMffdJ71ufOpX3w',
        'summonerName': 'Twitch Lord Semi',
        'leaguePoints': 1165,
        'wins': 190,
        'losses': 174
    },
      {
        'leagueId': '9468e29a-a085-3ab8-8d19-d25cc8630618',
        'queueType': 'RANKED_SOLO_5x5',
        'tier': 'CHALLENGER',
        'rank': 'I',
        'summonerId': 'O0-OMg0BF3yjuS1RCxP6j1woiyZSGfKnT8yRfcLFuqTl1Cc',
        'summonerName': 'kaze 7',
        'leaguePoints': 1161,
        'wins': 265,
        'losses': 209
    }, {
        'leagueId': '9468e29a-a085-3ab8-8d19-d25cc8630618',
        'queueType': 'RANKED_SOLO_5x5',
        'tier': 'CHALLENGER',
        'rank': 'I',
        'summonerId': 'O0-OMg0BF3yjuS1RCxP6j1woiyZSGfKnT8yRfcLFuqTl1Cc',
        'summonerName': 'kaze 7',
        'leaguePoints': 1161,
        'wins': 265,
        'losses': 209
    },
]

result =isMono(teste)

with open('saida.json','w') as f:
    f.write(json.dumps(result))
    