import os
import requests
import json


# définition de l'adresse de l'API
api_address = 'localhost'
# port de l'API
api_port = 8000
user = {'alice':'wonderland', 'bob':'builder', 'clementine':'mandarine'}
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
def test_auth(username, password):

# requête

    r = requests.get(url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': username,
        'password': password
    }
    )
    if (username == 'alice' and password == 'wonderland') or (username == 'bob' and password == 'builder'):

        output = '''
        ============================
            Authentication test
        ============================
        
        request done at "/permissions"
        | username={u}
        | password={p}
        
        expected result = 200
        actual restult ={status_code}
        
        ==>  {test_status}
        
        '''
    else:
        output = '''
        ============================
            Authentication test
        ===========================
        request done at "/permissions"
        | username={u}
        | password={p}
        expected result = 403
        actual restult ={status_code}
        ==>  {test_status}
           '''


# statut de la requête
    status_code = r.status_code

# affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(status_code=status_code, test_status=test_status, u=username, p=password))

# impression dans un fichier
    if os.environ.get('LOG') == 1:
        with open('api_test.log', 'a') as file:
            file.write(output)

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
    if os.environ.get('LOG') == 1:
        with open('api_test.log', 'a') as file:
            file.write(output)

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
    if os.environ.get('LOG') == 1:
        with open('api_test.log', 'a') as file:
            file.write(output)

#Test 1
for key, value in user.items():
    test_auth(key, value)

#Test 2
for i in range(len(users_test2)):
    test_sentiment(users_test2[i]['username'],users_test2[i]['password'],users_test2[i]['sentence'])

#Test 3
for i in range(len(users_test3)):
    test_content(users_test3[i]['username'],users_test3[i]['password'],users_test3[i]['sentence'])

