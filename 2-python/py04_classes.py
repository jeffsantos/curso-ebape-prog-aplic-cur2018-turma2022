class Turma():
    def __init__(self, limite, disciplina):
        self.limite = limite
        self.disciplina = disciplina
        self.alunos = []

    def add_alunos(self, nome):
        if self.vagas() == 0:
            return False
        
        self.alunos.append(nome)
        return True

    def vagas(self):
        return self.limite - len(self.alunos)

class Aluno():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


turma1 = Turma(5, 'Prog Aplic 2')
turma2 = Turma(10, 'Prog Aplic 3')

print(f"Turma: {turma1.disciplina} tem limite de {turma1.limite} alunos")
print(f"Turma: {turma2.disciplina} tem limite de {turma2.limite} alunos")

aluno1 = Aluno("Joao", "Copacabana")
aluno2 = Aluno("Luca", "Leme")
aluno3 = Aluno("Thaisa", "Tijuca")
aluno4 = Aluno("Carlos", "Ipanema")
aluno5 = Aluno("Gabriel", "Barra")
aluno6 = Aluno("Carina", "Copacabana")


lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6]

for aluno in lista_alunos:

    ret = turma1.add_alunos(aluno)

    if ret:
        print(f"Aluno {aluno.nome} matriculado")
    else:
        print(f"Não há mais vagas para incluir o aluno {aluno.nome}")
