# Press the green button in the gutter to run the script.
from src.conta import Conta

if __name__ == '__main__':
    minhaConta = Conta(1001, 2000)
    aux = minhaConta.getNumero()
    print(aux)
    print(minhaConta)
    
    destino = Conta(10, 0)
    print(destino)

    minhaConta.sacar(200)
    print(minhaConta)

    if minhaConta.sacar(10000) is False:
        print("Saldo insuficiente")

    minhaConta.depositar(500)
    print(minhaConta)

    minhaConta.transferir(destino, 400)
    print(minhaConta)

    if minhaConta.transferir(destino,4000000) is False:
        print("Saldo insuficiente")

    if minhaConta.sacar(1950) is False:
        print("Saldo insuficiente")

    minhaConta.depositar(50)
    print(minhaConta)

    minhaConta.depositar(60)
    print(minhaConta)

    minhaConta.depositar(210)
    print(minhaConta)

    minhaConta.transferir(destino, 30)
    print(minhaConta)

    minhaConta.transferir(destino, 40)
    print(minhaConta)

    minhaConta.sacar(2)
    print(minhaConta)

    minhaConta.sacar(25)
    print(minhaConta)
    minhaConta.sacar(20)
    extrato = minhaConta.verExtrato()
    print(f'Tamanho lista extrato: {len(extrato)}')
    for i in range(len(extrato)):
      print(extrato[i])
