import mysql.connector

def conectar():
    return  mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='academia',
    )

def cadastrar(conexao):
    cursor = conexao.cursor()
    
    name = input("Digite o nome do Aluno: ")
    peso = int(input("Digite o peso do Aluno: "))
    comando = f'INSERT INTO aluno (nome,peso) VALUES ("{name}" , {peso})'
    cursor.execute(comando)
    conexao.commit() 
    cursor.close()
    
    print("Cadastrado com sucesso!!")
    
def mostrar(conexao):
    cursor = conexao.cursor()
    
    comando = f'SELECT * FROM aluno'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for aluno in resultado:
        print(aluno)
    conexao.commit()
    cursor.close()
    
def editar(conexao):
    cursor = conexao.cursor()
    
    ide= int(input("Id do aluno que deseja alterar: "))
    nomealt = input("Nome para qual deseja alterar: ")
    pesoalt = int(input("Peso para qual quer alterar: "))
    comando = f"UPDATE aluno SET peso = {pesoalt}, nome = '{nomealt}' WHERE id_aluno = {ide} "
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    print("Editado com sucesso!!")
    
    
    
def excluir(conexao):
    cursor = conexao.cursor()
    
    idex = int(input("Id do aluno que deseja excluir: "))
    comando = (f'DELETE FROM aluno WHERE id_aluno = {idex}')
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    print("Excluido com sucesso!!")
    
def main():
    conexao = conectar()
    
    while True:
        
        print("------------------------------")
        print("Bem vindo a academia ")
        print("------------------------------")
        print("1 - Cadastrar aluno")
        print("2 - Mostrar alunos cadastrados")
        print("3 - Editar aluno cadastrado")
        print("4 - Deletar aluno cadastrado")
        print("5 - Parar programa")
        print("------------------------------")
        op = int(input(":"))
        
        if op == 1:
            cadastrar(conexao)
        
        elif op == 2:
           mostrar(conexao)

        elif op == 3:
            editar(conexao)
            
        elif op == 4:
            excluir(conexao)
            
        elif op == 5:
            break
            
        else:
            print("ERRO! Tente novamente")
            
            
    conexao.close()
    
if __name__ == "__main__":
    main()

