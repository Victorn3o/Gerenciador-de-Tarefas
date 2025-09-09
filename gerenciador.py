import json
import os
from colorama import Fore, Style, init
import pyfiglet

# Inicializa o colorama
init(autoreset=True)

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r") as f:
            return json.load(f)
    return {}

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump(tarefas, f, indent=4)

def listar_tarefas(tarefas):
    if not tarefas:
        print(Fore.YELLOW + "Nenhuma tarefa cadastrada.")
    else:
        print(Fore.CYAN + "\n=== Lista de Tarefas ===")
        for id, tarefa in tarefas.items():
            status = "✅" if tarefa["concluida"] else "❌"
            print(f'{id} - {tarefa["descricao"]} [{status}]')

def adicionar_tarefa(tarefas):
    descricao = input("Descrição da nova tarefa: ").strip()
    if descricao:
        novo_id = str(len(tarefas) + 1)
        tarefas[novo_id] = {"descricao": descricao, "concluida": False}
        salvar_tarefas(tarefas)
        print(Fore.GREEN + f"Tarefa {novo_id} adicionada com sucesso!")
    else:
        print(Fore.RED + "Descrição não pode estar vazia!")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    tarefa_id = input("\nDigite o ID da tarefa a concluir: ").strip()
    if tarefa_id in tarefas:
        if not tarefas[tarefa_id]["concluida"]:
            tarefas[tarefa_id]["concluida"] = True
            salvar_tarefas(tarefas)
            print(Fore.GREEN + f"Tarefa {tarefa_id} concluída com sucesso!")
        else:
            print(Fore.YELLOW + f"Tarefa {tarefa_id} já está concluída.")
    else:
        print(Fore.RED + "ID inválido.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    tarefa_id = input("\nDigite o ID da tarefa a remover: ").strip()
    if tarefa_id in tarefas:
        tarefas.pop(tarefa_id)
        salvar_tarefas(tarefas)
        print(Fore.GREEN + f"Tarefa {tarefa_id} removida com sucesso!")
    else:
        print(Fore.RED + "Tarefa não encontrada.")

def menu():
    tarefas = carregar_tarefas()

    while True:
        # Cabeçalho ASCII estilizado
        titulo = pyfiglet.figlet_format("To-Do App")
        print(Fore.MAGENTA + titulo)

        print(Fore.CYAN + "=== Menu de opções ===")
        print("1 - Listar tarefas")
        print("2 - Adicionar tarefa")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            print(Fore.CYAN + "Saindo... Até a próxima!")
            break
        else:
            print(Fore.RED + "Opção inválida.")

if __name__ == "__main__":
    menu()
