###Você está organizando uma lista de alunos por turmas em uma escola. Cada turma contém vários alunos, e cada aluno é deve conter um nome, idade e id.
###Exercício da aula passada, porém deve ser resolvido utilizando o que aprendemos sobre POO.

###a) Crie duas turmas, cada uma contendo dois alunos.

###b) Adicionar um novo aluno: Adicione um novo aluno em uma das turmas.

###c) Remover um aluno: Remova um aluno de uma das turmas.

###d) Exibir os alunos de uma turma

class Aluno():
    def __init__(self, nome, idade, id):
        self.nome = nome
        self.idade = idade
        self.id = id

aluno1 = Aluno("Theo", 12, 1)

print(aluno1.nome)
print(aluno1.idade)

#Faça uma função que dado um vetor de inteiros retorne o maior inteiro do vetor.
def MaiorValor(vetor):
    if (len(vetor) == 0):
        return None
    maior = vetor[0]

    for i in range(len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
    return maior

vetor = [23, 45, 56, 7]
print(MaiorValor(vetor))


class Aluno:
    def __init__(self, nome, idade, id):
        self.nome = nome
        self.idade = idade
        self.id = id

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def AdicionarAluno(self, nome, idade, id):
        aluno = Aluno(nome, idade, id)
        self.alunos.append(aluno)
        print(f"Aluno {nome} adicionado à {self.nome} com sucesso!")

    def RemoverAluno(self, idAlunoRemover):
        for aluno in self.alunos:
            if aluno.id == idAlunoRemover:
                self.alunos.remove(aluno)

    def listarAlunos(self):
        if len(self.alunos) == 0:
            print("Essa turma não contém alunos")
            return None
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}. Idade: {aluno.idade}. Id: {aluno.id}")



#Turma A

# Exemplo de uso
turmaA = Turma("Turma A")
turmaB = Turma("Turma B")

aluno1 = Aluno(nome="Thiago", idade=23, id=23188)
aluno2 = Aluno(nome="Romeu", idade=33, id=23189)

turmaA.AdicionarAluno(aluno1.nome, aluno1.idade, aluno1.id)
turmaA.AdicionarAluno(aluno2.nome, aluno2.idade, aluno2.id)


turmaB.AdicionarAluno(nome="Karina", idade=32, id=23190)
turmaB.AdicionarAluno(nome="Francis", idade=18, id=23200)
turmaA.AdicionarAluno(nome="Bruna", idade=38, id=23207)

turmaA.listarAlunos()
turmaB.listarAlunos()

print()