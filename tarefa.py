class Tarefa:
    """Classe que representa uma tarefa."""

    def __init__(self, id, descricao, status='pendente'):
        self.id = id
        self.descricao = descricao
        self.status = status

    def concluir(self):
        """Marca a tarefa como concluída."""
        self.status = 'concluída'

    def __str__(self):
        return f"[{self.id}] {self.descricao} - {self.status}"

    def to_dict(self):
        """Converte a tarefa em dicionário para salvar em JSON."""
        return {
            'id': self.id,
            'descricao': self.descricao,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        """Cria uma tarefa a partir de um dicionário."""
        return cls(id=data['id'], descricao=data['descricao'], status=data['status'])
