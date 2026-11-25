lista_curso = [ 
    {"id": 1, "nome": "Técnico em Informática", "area": "Informação e Comunicação"},
    {"id": 2, "nome": "Técnico em Administração", "area": "Gestão e Negócios"},
    {"id": 3, "nome": "Técnico em Eletrotécnica", "area": "Controle e Processos Industriais"},
]

def listar():
    return lista_curso

def cadastrar(nome, area):
    # Sem banco de dados: o novo id é o id do último aluno + 1
    if len(lista_curso) == 0:
        novo_id = 1
    else:
        ultimo = lista_curso[-1]
        novo_id = ultimo["id"] + 1


    curso = {"id": novo_id, "nome": nome,
             "area": area}
    lista_curso.append(curso)
    return curso