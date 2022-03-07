# Template Python
Template de repositório para projetos em Python

[![pdm](https://img.shields.io/badge/pdm-managed-blueviolet)](https://github.com/pdm-project/pdm)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


---

## ⚠️ Para fazer o setup do projeto que herdar este template, atualize os metadados sobre o projeto no `pyproject.toml` e este README para se adequar ao projeto.

> ⚠️ Não esqueça também de redefinir os comandos específicos pro seu projeto, como os de inicializar o servidor de um backend se for o caso e afins.

### Execução do projeto
Ao clonar o repositório, execute o script de setup com `python -m config.scripts.setup` para a instalação do Poetry, ambiente virtual e pre-commit hooks. É necessário possuir Python 3.8+ para este projeto.

---

#### Comandos
- `poetry add <lib>`: Adiciona uma biblioteca nova ao projeto.
- `poetry add -D <lib>`: Adiciona uma biblioteca de desenvolvimento nova ao projeto (que não será instalada no ambiente de produção).
- `poetry remove <lib>`: Remove uma biblioteca (para remover uma de desenvolvimento, passe a flag `-D`)
- `poe <comando>`: Executa um comando da lista de comandos personalizados na seção de scripts. Você pode verificar quais comandos existem também rodando apenas `poe`, na última parte da mensagem.

### Estrutura de pastas

| Pastas                 | Descrição                                            |
|:-----------------------|:-----------------------------------------------------|
|📦 PROJETO              | Raiz do projeto                                      |
| ┣ 📂 .github           | Configurações do github                              |
| ┣ 📂 docs              | Arquivos de documentação                             |
| ┣ 📂 config            | Arquivos de configuração geral do projeto            |
|   ┣ 📂 scripts         | Scripts padrão para o desenvolvimento do projeto     |
| ┣ 📂 tests             |                                                      |
| ┣ 📂 src               | Diretório base dos scripts do projeto                |
|   ┣ 📂 ...             |                                                      |
