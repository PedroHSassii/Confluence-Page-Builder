import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "SUA URL AQUI"
EMAIL = "SEU EMAIL AQUI"
API_TOKEN = "SEU TOKEN AQUI"

SPACE_ID = "SEU SPACEID AQUI"
PARENT_PAGE_ID = "SEU PAGEID AQUI"

auth = HTTPBasicAuth(EMAIL, API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

estrutura = {
    "PM Rodeio Bonito": {},
    "PM Alto Alegre": {},
    "PM Campos Borges": {},
    "PM São Vicente do Sul": {},
}


def criar_pagina(titulo, parent_id):
    url = f"{BASE_URL}/wiki/api/v2/pages"

    body =  f""" <h1>Sistema Ambiental - {titulo}</h1>

<p>Documentação do módulo/sistema Ambiental de uso exclusivo da {titulo}</p>

<h2>Visão geral</h2>
<p>O módulo Ambiental atende às rotinas da Secretaria Municipal responsável pelo meio ambiente em {titulo}, abrangendo o controle de processos, licenças, autorizações e demais atividades relacionadas à gestão ambiental municipal.</p>

<h2>Escopo / Funcionalidades</h2>
<ul>
  <li>Cadastro e gestão de processos ambientais municipais (A confirmar)</li>
  <li>Emissão e controle de licenças e autorizações ambientais (A confirmar)</li>
  <li>Controle de empreendimentos/atividades sujeitas a licenciamento ambiental (A confirmar)</li>
  <li>Gestão de vistorias, pareceres técnicos e laudos ambientais (A confirmar)</li>
  <li>Acompanhamento de condicionantes e prazos de licenças ambientais (A confirmar)</li>
  <li>Protocolo e tramitação interna de documentos ambientais (A confirmar)</li>
</ul>

<h2>Acessos</h2>
<ul>
  <li>Produção: A confirmar</li>
  <li>Homologação / testes: A confirmar</li>
</ul>

<h2>Perfis e permissões</h2>
<ul>
  <li>Perfil Analista Ambiental: A confirmar</li>
  <li>Perfil Fiscal / Vistoriador Ambiental: A confirmar</li>
  <li>Perfil Gestor / Coordenador Ambiental: A confirmar</li>
  <li>Perfil Atendimento / Protocolo Ambiental: A confirmar</li>
</ul>

<h2>Cadastros / Parametrizações</h2>
<p>Configurações e cadastros básicos utilizados pelo módulo Ambiental da {titulo}</p>

<h2>Rotinas principais</h2>
<ul>
  <li>Abertura de processo ambiental</li>
  <li>Análise técnica e vistorias ambientais</li>
  <li>Emissão de documentos ambientais</li>
  <li>Acompanhamento pós-emissão</li>
</ul>

<h2>Integrações</h2>
<p>Integração com Ambiental Net: A confirmar</p>

<h2>Relatórios / Documentos emitidos</h2>
<p>Relatórios e documentos gerados diretamente pelo sistema Ambiental da {titulo}: A confirmar</p>

<h2>Usuários-chave / Contatos</h2>
<ul>
  <li>Gestor responsável pelo módulo Ambiental na PM: A confirmar</li>
  <li>Contato de suporte interno: A confirmar</li>
  <li>Contato de suporte junto ao fornecedor: A confirmar</li>
</ul>

<h2>Observações</h2>
<p>Este documento é exclusivo da {titulo} e destina-se exclusivamente à documentação do módulo/sistema Ambiental.</p>
"""

    payload = {
        "spaceId": SPACE_ID,
        "status": "current",
        "title": titulo,
        "parentId": parent_id,
        "body": {
            "representation": "storage",
            "value": body
        }
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        auth=auth
    )

    if response.status_code not in [200, 201]:
        print(f"ERRO ao criar: {titulo}")
        print(response.status_code)
        print(response.text)
        return None

    page = response.json()
    page_id = page["id"]

    print(f"CRIADA: {titulo} | ID: {page_id}")
    return page_id


def criar_hierarquia(arvore, parent_id):
    for titulo, filhos in arvore.items():
        page_id = criar_pagina(titulo, parent_id)

        if page_id and filhos:
            criar_hierarquia(filhos, page_id)


if __name__ == "__main__":
    criar_hierarquia(estrutura, PARENT_PAGE_ID)
    print("Finalizado.")