# PASSO 1: Importe o pytest
import pytest
from fastapi.testclient import TestClient
from main import app

# PASSO 2: Transforme o 'client' em uma "Fixture" (O "Armário de Panelas")
@pytest.fixture
def client():
    # Isso é o "setup": cria a "panela limpa"
    c = TestClient(app)
    # A palavra 'yield' é como um 'return' especial para fixtures
    yield c
    # (Qualquer código de "limpeza" poderia vir aqui, depois do 'yield')

# PASSO 3: Mude a "assinatura" dos testes para ELES PEDIREM a fixture
#
# (Observe o 'client' como argumento da função)
def test_read_root(client):
    # O 'client' que esta função recebe é a "panela limpa"
    # que a fixture @pytest.fixture def client() acima criou!
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# (Observe o 'client' como argumento da função)
def test_tarefas(client):
    # Este 'client' também é uma "panela limpa" novinha,
    # totalmente separada da panela do test_read_root.
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "descricao": "Comprar pão"}, {"id": 2, "descricao": "Estudar Docker"}]