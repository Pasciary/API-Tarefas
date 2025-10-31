# 1. Importa o "Inspetor de Qualidade Robótico"
from fastapi.testclient import TestClient

# 2. Importa o nosso "Chef" (a variável 'app') do nosso arquivo 'main.py'
from main import app

# 3. Cria uma instância do "Inspetor" e entrega a ele uma cópia
#    de "carbono" da nossa API (o 'app') para ele testar.
#    A partir de agora, a variável 'client' é o nosso inspetor.
client = TestClient(app)

# 4. Definimos nossa primeira "ordem de teste".
#    O Pytest vai encontrar isso porque começa com 'test_'.
def test_read_root():
    # 5. Damos a ordem: "Inspetor ('client'), faça um pedido GET
    #    para o endereço '/' e guarde o 'prato' (resposta)
    #    na variável 'response'."
    response = client.get("/")
    
    # 6. AS AFIRMAÇÕES (O "CHECKLIST" DO INSPETOR):
    
    # "Inspetor, afirme (assert) que o 'status_code' do prato
    #  é exatamente igual (==) a 200 (Sucesso)."
    assert response.status_code == 200
    
    # "Inspetor, afirme (assert) que o 'conteúdo .json()' do prato
    #  é exatamente igual (==) a {"Hello": "World"}."
    assert response.json() == {"hello": "world"}

def test_tarefas():
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "descricao": "Comprar pão"}, {"id": 2, "descricao": "Estudar Docker"}]
