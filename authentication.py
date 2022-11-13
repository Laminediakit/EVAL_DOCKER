import os
import requests
import json

#os.environ['LOG'] = "1"
# définition de l'adresse de l'API
api_address = os.environ['api_address']
# port de l'API
api_port = os.environ['api_port']
user = {'alice':'wonderland', 'bob':'builder', 'clementine':'mandarine'}

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
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output.format(status_code=status_code, test_status=test_status, u=username, p=password))

#Test 1
for key, value in user.items():
    test_auth(key, value)

