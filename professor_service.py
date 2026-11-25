lista_professor = [ 
    {"id": 1, "nome": "Marcos Oliveira", "email": "marcos@exemplo.com", "titulacao": "Mestre"},
    {"id": 2, "nome": "Paula Ribeiro", "email": "paula@exemplo.com", "titulacao": "Doutora"},
    {"id": 3, "nome": "Renato Alves", "email": "renato@exemplo.com", "titulacao": "Especialista"},
]

def listar():
    return lista_professor

def cadastrar(nome, email,titulacao):
    # Sem banco de dados: o novo id é o id do último aluno + 1
    if len(lista_professor) == 0:
        novo_id = 1
    else:
        ultimo = lista_professor[-1]
        novo_id = ultimo["id"] + 1


    professor = {"id": novo_id, "nome": nome,
             "email": email, "titulacao": titulacao}
    lista_professor.append(professor)
    return professor