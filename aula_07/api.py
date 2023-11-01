# CRUD

# (Read) GET method: retrieves information or data from a specified resource.
# (Create) POST method: submits data to be processed to a specified resource.
# (Update) PUT method: updates a specified resource with new data.
# (Delete) DELETE method: deletes a specified resource.

import json, requests

url = 'https://viacep.com.br/ws/35024410/json/'

resposta = requests.get(url)

conteudo = json.loads(resposta.content)

# print(conteudo)

## CRUD (PGUD)

url_api = 'https://6541a06df0b8287df1fe9099.mockapi.io/usuarios'

usuario = {
    'usuario': 'Julio Cezar',
    'senha': 'Bolaquadrada'

}

#CREATE
# resposta = requests.post(url_api, data=usuario)
# print(resposta.status_code)

#READ
resposta = requests.get(url_api)

# print(resposta.status_code)

conteudo_api = json.loads(resposta.content)
# print(conteudo_api)

#UPDATE
# resposta = requests.put(f"{url_api}/7", data=usuario)
# print(resposta.status_code)

#DELETE
resposta = requests.delete(f"{url_api}/7")
print(resposta.status_code)






