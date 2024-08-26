import os
os.system("cls || clear")

''''pedindo ao usuario o que ele quer'''
desconto = 0
escolha = input("Digite o produto escolhido: ")
valordoproduto = float (input(f"Qual o valor do produto? ")) 
escolhapagamento = int(input(f"""Qual a forma de pagamento?
                    1 -  Pagamento á vista
                    2 -  pagamento á prazo
                                                        """))
''''fazendo o case'''''
match(escolhapagamento):
    #fazendo o case da forma de pagamento
    case 1:
         
         formadepagamento = "pagamento á vista"
         desconto = valordoproduto * 0.10 
         valorfinal = valordoproduto - desconto
         print(f""" o valor do produto foi de {valordoproduto}
                    a forma de pagamento foi {formadepagamento}
                    valor do desconto: {desconto}
                    total a pagar: {valorfinal:.2f}


               """)
    case 2:
      numparcela =   int(input("Digite a quantidade de parcelas que você deseja pagar, sendo que você pode pagar de até 6 vezes:  "))
      formadepagamento = "á prazo"
      valorparcela = valordoproduto / numparcela
      valorfinal = valordoproduto
      print(f""" o valor do produto foi de {valordoproduto}
                    a forma de pagamento foi {formadepagamento}
                    valor da parcela: {valorparcela}
                    total á prazo: {valorfinal:.2f}


               """)