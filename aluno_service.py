lista_aluno = [ 
    {"id": 1, "nome": "Ana Souza", "telefone": "(86)99999-0001", "cidade": "Teresina"},
    {"id": 2, "nome": "Bruno Lima", "telefone": "(86)99999-0002", "cidade": "Timon"},
    {"id": 3, "nome": "Carla Mendes", "telefone": "(86)99999-0003", "cidade": "Parnaíba"},
]

def listar():
    return lista_aluno



def cadastrar(nome, telefone, cidade):
    # Sem banco de dados: o novo id é o id do último aluno + 1
    if len(lista_aluno) == 0:
        novo_id = 1
    else:
        ultimo = lista_aluno[-1]
        novo_id = ultimo["id"] + 1


    aluno = {"id": novo_id, "nome": nome,
             "telefone": telefone, "cidade": cidade}
    lista_aluno.append(aluno)
    return aluno
