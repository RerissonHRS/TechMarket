from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI(title="TechMarket API")

class Transfer(BaseModel):
    origem: str
    destino: str
    valor: float

# Simulação de saldos (banco de dados)
saldos = {'123': 5000.0, '456': 2000.0}

@app.post('/transferir')
def transferir(dados: Transfer):
    if dados.origem not in saldos or saldos[dados.origem] < dados.valor:
        raise HTTPException(status_code=400, detail='Saldo insuficiente')
    saldos[dados.origem] -= dados.valor
    saldos[dados.destino] = saldos.get(dados.destino, 0) + dados.valor
    codigo = str(uuid.uuid4())
    return {'status': 'sucesso', 'codigo_transacao': codigo, 'novo_saldo_origem': saldos[dados.origem]}
