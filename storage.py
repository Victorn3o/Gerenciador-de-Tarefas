import json
from tarefa import Tarefa

ARQUIVO = 'tarefas.json'

def carregar_tarefas():
    """Carrega tarefas do arquivo JSON, retorna lista de objetos Tarefa."""
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        return [Tarefa.from_dict(t) for t in dados]
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Erro ao carregar tarefas: {e}")
        return []

def salvar_alteracoes(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    try:
        tarefas_dict = [tarefa.to_dict() for tarefa in tarefas]
        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump(tarefas_dict, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar tarefas: {e}")
