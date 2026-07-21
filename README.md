# Confluence Page Builder

Automação em Python para consultar espaços e criar páginas hierárquicas no Confluence Cloud por meio da API da Atlassian.

## Funcionalidades

- Criação de páginas em um espaço do Confluence.
- Definição de uma página-pai para organizar o conteúdo.
- Criação recursiva de uma árvore de páginas.
- Inclusão de conteúdo HTML no formato `storage` do Confluence.
- Consulta auxiliar de informações de um espaço.

## Estrutura do projeto

- `criar_paginas_confluence.py`: cria as páginas definidas no dicionário `estrutura`.
- `busca_espaço.py`: consulta um espaço do Confluence pela chave informada na URL.

## Requisitos

- Python 3.10 ou superior.
- Acesso a uma instância do Confluence Cloud.
- E-mail de uma conta Atlassian.
- Token de API da Atlassian.
- Permissão para visualizar o espaço e criar páginas nele.

## Instalação

Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale a dependência:

```powershell
python -m pip install requests
```

## Configuração

Antes de executar a automação, confira no script principal:

- `BASE_URL`: endereço da organização Atlassian.
- `EMAIL`: e-mail da conta utilizada na autenticação.
- `API_TOKEN`: token de API da Atlassian.
- `SPACE_ID`: identificador numérico do espaço.
- `PARENT_PAGE_ID`: identificador da página sob a qual as novas páginas serão criadas.
- `estrutura`: títulos e hierarquia das páginas desejadas.

No script de consulta, ajuste também a chave do espaço presente na URL da requisição.

> **Segurança:** não publique tokens de API no repositório. Prefira armazenar as credenciais em variáveis de ambiente e mantenha arquivos locais de configuração fora do controle de versão. Caso um token tenha sido exposto, revogue-o e gere outro no painel da Atlassian.

## Uso

Para consultar um espaço:

```powershell
python ".\busca_espaço.py"
```

Para criar as páginas:

```powershell
python .\criar_paginas_confluence.py
```

O programa mostra no terminal o título e o ID de cada página criada. Se a API rejeitar uma operação, também exibe o código de resposta e a mensagem retornada pelo Confluence.

## Como definir a hierarquia

As chaves do dicionário são os títulos das páginas. Um dicionário vazio representa uma página sem filhas:

```python
estrutura = {
    "Página principal": {
        "Visão geral": {},
        "Procedimentos": {
            "Primeiros passos": {}
        }
    }
}
```

## Atenção antes da execução

A automação cria páginas reais no espaço configurado. Confirme o `SPACE_ID`, o `PARENT_PAGE_ID`, os títulos e o conteúdo antes de executar o script, pois novas execuções podem criar páginas duplicadas.

## Licença

Este projeto está disponível sob a [Licença MIT](LICENSE).
