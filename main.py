from fastapi import FastAPI # Importa a ferramenta.

app = FastAPI(); # Cria o chefe principal.

@app.get("/")
def read_root():
    return {'hellow': 'world'}

@app.get("/tarefas")
def get_tarefas():
    return [{"id": 1, "descricao": "Comprar pão"}, {"id": 2, "descricao": "Estudar Docker"}]
