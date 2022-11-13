import os
import requests
import json

#os.environ['LOG'] = "1"
# définition de l'adresse de l'API
api_address = os.environ['api_address']
# port de l'API
api_port = os.environ['api_port']
users_test2 = [
    {   'username': 'alice',
        'password': 'wonderland',
        'sentence': 'hello world'
    },
    {   'username': 'bob',
        'password': 'builder',
        'sentence': 'hello world'
    }
]

def test_sentiment(username, password, sentence):

# requête

    r1 = requests.get(url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': username,
        'password': password,
        'sentence': sentence
    }
    )
    output1 = '''
        ============================
            Authorization test
        ============================

        request done at "/v1/sentiment"
        | username={u}
        | password={p}
        | sentence={s}

        expected result = 200
        actual restult ={status_code}

        ==>  {test_status}
    
    '''

    r2 = requests.get(url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': username,
        'password': password,
        'sentence': sentence
    }
    )
    if (username == 'alice' and password == 'wonderland'):

        output2 = '''
        ============================
            Authorization test
        ============================

        request done at "/v2/sentiment"
        | username={u}
        | password={p}
        | sentence={s}

        expected result = 200
        actual restult ={status_code}

        ==>  {test_status}

        '''
    else:
        output2 = '''
        ============================
            Authorization test
        ============================

        request done at "/v2/sentiment"
        | username={u}
        | password={p}
        | sentence={s}

        expected result = 403
        actual restult ={status_code}

        ==>  {test_status}

        '''    

# statut de la requête
    status_code1 = r1.status_code
    status_code2 = r2.status_code

# affichage des résultats
    if status_code1 == 200:
        test_status1 = 'SUCCESS'
    else:
        test_status1 = 'FAILURE'
    if status_code2 == 200:
        test_status2 = 'SUCCESS'
    else:
        test_status2 = 'FAILURE'
    print(output1.format(status_code=status_code1, test_status=test_status1, u=username, p=password,s=sentence))
    print(output2.format(status_code=status_code2, test_status=test_status2, u=username, p=password,s=sentence))

# impression dans un fichier
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output1.format(status_code=status_code1, test_status=test_status1, u=username, p=password,s=sentence))
            file.write(output2.format(status_code=status_code2, test_status=test_status2, u=username, p=password,s=sentence))


#Test 2
for i in range(len(users_test2)):
    test_sentiment(users_test2[i]['username'],users_test2[i]['password'],users_test2[i]['sentence'])
