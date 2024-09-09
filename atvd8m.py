def pagamento():
    import os
    os.system("cls || clear")
 
    ''''pedindo ao usuario o que ele quer'''
    desconto = 0
    escolha = input("Digite o produto escolhido: ")
    valordoproduto = float (input(f"Qual o valor do produto? ")) 
    os.system("cls || clear")
    ''''fazendo o case'''''
        #fazendo o case da forma de pagamento
    if valordoproduto < 100:
            
            formadepagamento = "pagamento á vista"
            desconto = valordoproduto * 0.10 
            valorfinal = valordoproduto + desconto
            print(f""" o valor do produto foi de {valordoproduto}
                        a forma de pagamento foi {formadepagamento}
                        valor do desconto: {desconto}
                        total a pagar: {valorfinal:.2f}


                """)
    if valordoproduto >= 100:
            
            formadepagamento = "pagamento á vista"
            desconto = valordoproduto * 0.20 
            valorfinal = valordoproduto + desconto
            print(f""" o valor do produto foi de {valordoproduto}
                        a forma de pagamento foi {formadepagamento}
                        valor do desconto: {desconto}
                        total a pagar: {valorfinal:.2f}
        """)

pagamento()