# ✅ Gerenciador de Tarefas (To-Do App)

Este é meu primeiro projeto, que fiz com o intuito de consolidar e aplicar meus aprendizados em programação.

É um simples gerenciador de tarefas em Python, executado no terminal.
Permite adicionar, listar, concluir e remover tarefas, salvando tudo em um arquivo JSON.
Feito para treinar organização de código, persistência de dados e boas práticas em Python.

## -> Funcionalidades

➕ Adicionar novas tarefas

📋 Listar todas as tarefas

✅ Concluir tarefas

🗑️ Remover tarefas

💾 Armazenamento em arquivo tarefas.json

## -> Como executar
## 1. Clone este repositório
```text
git clone https://github.com/Victorn3o/Gerenciador-de-Tarefas
cd Gerenciador-de-Tarefas
```

## 2. (Opcional) Crie um ambiente virtual
python -m venv venv
### Windows:
venv\Scripts\activate
### Linux/Mac:
source venv/bin/activate

## 3. Instale as dependências
pip install colorama pyfiglet

##  4. Rode o projeto
python -m main

## -> Demonstração

Ao iniciar, o terminal exibe um cabeçalho estilizado e o menu:

```text

████████╗ ██████╗     ██████╗  ██████╗       █████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔═══██╗    ██╔══██╗██╔═══██╗     ██╔══██╗██╔══██╗██╔══██╗
   ██║   ██║   ██║    ██║  ██║██║   ██║     ███████║██████╔╝██║  ██║
   ██║   ██║   ██║    ██║  ██║██║   ██║     ██╔══██║██╔═══╝ ██║  ██║
   ██║   ╚██████╔╝    ██████╔╝╚██████╔╝     ██║  ██║██║     ██████╔╝
   ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝      ╚═╝  ╚═╝╚═╝     ╚═════╝

=== Menu de opções ===
1 - Listar tarefas
2 - Adicionar tarefa
3 - Concluir tarefa
4 - Remover tarefa
0 - Sair

```

## -> Estrutura do projeto

```text
todo-app/
│── main.py
│── tarefa.py
│── gerenciador.py
│── storage.py
│── tarefas.json
│── README.md
│── LICENSE

```

## -> Tecnologias usadas

Python 3

Colorama
 (cores no terminal)

Pyfiglet
 (cabeçalho estilizado)

## 📜 Licença

Este projeto está sob a licença MIT.
Consulte o arquivo LICENSE
 para mais detalhes.