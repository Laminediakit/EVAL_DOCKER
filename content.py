import os
import requests
import json

#os.environ['LOG'] = "1"
# définition de l'adresse de l'API
api_address = os.environ['api_address']
# port de l'API
api_port = os.environ['api_port']

users_test3 = [
    {   'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    },
    {   'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
]

def test_content(username, password, sentence):

# requête

    r1 = requests.get(url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': username,
        'password': password,
        'sentence': sentence
    }
    )
    if (sentence == 'life is beautiful'):
        output1 = '''
        ============================
            Content test
        ============================
        request done at "/v1/sentiment"
        | username={u}
        | password={p}
        | sentence={s}
        expected result = +
        actual restult ={score}
        ==>  {test_status}

        '''
    else:
        output1 = '''
        ============================
            Content test
        ============================
        request done at "/v1/sentiment"
        | username={u}
        | password={p}
        | sentence={s}
        expected result = -
        actual restult ={score}
        ==>  {test_status}

        '''
    r2 = requests.get(url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': username,
        'password': password,
        'sentence': sentence
    }
    )
    if (sentence == 'life is beautiful'):

        output2 = '''
        ============================
            Content test
        ============================

        request done at "/v2/sentiment"
        | username={u}
        | password={p}
        | sentence={s}

        expected result = +
        actual restult ={score}

        ==>  {test_status}

        '''
    else:
        output2 = '''
        ============================
            Content test
        ============================

        request done at "/v2/sentiment"
        | username={u}
        | password={p}
        | sentence={s}

        expected result = -
        actual restult ={score}

        ==>  {test_status}

        '''    

# score de la requête
    score1 = json.loads(r1.text)['score']
    score2 = json.loads(r2.text)['score']

# affichage des résultats
    if score1 > 0:
        test_status1 = 'POSITIVE'
    else:
        test_status1 = 'NEGATIVE'
    if score2 > 0:
        test_status2 = 'POSITIVE'
    else:
        test_status2 = 'NEGATIVE'
    print(output1.format(score=score1, test_status=test_status1, u=username, p=password,s=sentence))
    print(output2.format(score=score2, test_status=test_status2, u=username, p=password,s=sentence))

# impression dans un fichier
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output1.format(score=score1, test_status=test_status1, u=username, p=password,s=sentence))
            file.write(output2.format(score=score2, test_status=test_status2, u=username, p=password,s=sentence))

#Test 3
for i in range(len(users_test3)):
    test_content(users_test3[i]['username'],users_test3[i]['password'],users_test3[i]['sentence'])

