menu = """
------- BANK ------
[0] DEPOSITAR
[1] SACAR
[2] EXTRATO
[3] Sair
------------------
"""
saldo = 0
extrato = ""
numero_saques = 0
limite_Diario = 500
SAQUES_DIARIOS = 3

while True:
    op = int(input(menu))

    if op == 0:
        valor_depositar = float(input("Quanto Depositar?: "))
        saldo += valor_depositar
        extrato += f"Deposito de: {valor_depositar}\n"

        print(f"Saldo Atual: {saldo:.02f}")

    if op == 1:
        valor_sacar = float(input("Quanto a Sacar [Limite: 500 / 3 Saques Diarios]: "))
        if valor_sacar <= limite_Diario and numero_saques < SAQUES_DIARIOS:
            if valor_sacar <= saldo:
                saldo -= valor_sacar
                limite_Diario -= valor_sacar
                numero_saques+=1
                extrato += f"Saque de: {valor_sacar}\n"
                print(f"Saldo Atual: {saldo}")
            else:
                print("Saldo Insuficiente")
        else:
            print("Limite ou Saques execidos, retorne amanhã")
    if op == 2:
        print(extrato)

    if op == 3:
        print("Agradecemos Seu Acesso e Esperamos que Retorne Novamente!")
        break
