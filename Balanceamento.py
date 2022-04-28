#Intala primeiro: pip install pythonds

from pythonds.basic.stack import Stack

def VerificarPar(ParentesesString):
    Pilha = Stack()
    Equilibra = True
    indice = 0
    while indice < len(ParentesesString) and Equilibra:
        Parenteses = ParentesesString[indice]
        if Parenteses == "{" or Parenteses == "(" or Parenteses == "[":
            Pilha.push(Parenteses)
        else:
            if Pilha.isEmpty():
                Equilibra = False
            else:
                Pilha.pop()

        indice = indice + 1

    if Equilibra and Pilha.isEmpty():
        return True
    else:
        return False

print(VerificarPar('((()))')) # True
print(VerificarPar('(())')) # True
print(VerificarPar('()())')) # false

#Referente ao exercicio do hackerrank -->  {[()]} -> balanceado {[(])} -> não balanceado {{[[(())]]}} -> balanceado
print(VerificarPar('{[()]}')) # True
print(VerificarPar('{[()[]}')) # false
print(VerificarPar('{{[[(())]]}}{')) # false
