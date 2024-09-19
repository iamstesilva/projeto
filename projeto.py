import time

print('\033[1;32;40mBEM-VINDO A PIZZARIA!!\033[m')
time.sleep(2)

class Pizzaria:
    def __init__(self):
        self.menu_pizzas = {
            "1": {"nome": "Margherita", "preco": 25.00},
            "2": {"nome": "Pepperoni", "preco": 30.00},
            "3": {"nome": "Quatro Queijos", "preco": 35.00},
            "4": {"nome": "Vegetariana", "preco": 28.00},
            "5": {"nome": "Calabresa", "preco": 30.00},
            "6": {"nome": "Frango com Catupiry", "preco": 35.00},
            "7": {"nome": "Carne Seca", "preco": 35.00}
        }
        self.menu_bebidas = {
            "1": {"nome": "Refrigerante", "preco": 0.00},  # Apenas marcador
            "2": {"nome": "Suco Natural", "preco": 0.00},  # Apenas marcador
            "3": {"nome": "Refrigerante 2L", "preco": 3.00}
        }
        self.menu_refrigerantes = {
            "1": {"nome": "Sprite", "preco": 7.00},
            "2": {"nome": "Coca-Cola", "preco": 7.00},
            "3": {"nome": "Fanta Laranja", "preco": 7.00},
            "4": {"nome": "Fanta Uva", "preco": 7.00},
            "5": {"nome": "Pepsi", "preco": 7.00}
        }
        self.menu_sucos = {
            "1": {"nome": "Suco de Goiaba", "preco": 6.50},
            "2": {"nome": "Suco de Laranja", "preco": 6.50},
            "3": {"nome": "Suco de Uva", "preco": 6.50},
            "4": {"nome": "Suco de Morango", "preco": 6.50}
        }
        self.menu_refrigerantes_2l = {
            "1": {"nome": "Coca-Cola 2L", "preco": 15.00},
            "2": {"nome": "Fanta Uva 2L", "preco": 15.00},
            "3": {"nome": "Fanta Laranja 2L", "preco": 15.00},
            "4": {"nome": "Pepsi 2L", "preco": 15.00}
        }
        self.pedido = []

    def mostrar_menu(self, tipo):
        if tipo == 'pizza':
            print("\n\033[1;35;40m=== Menu de Pizzas ===\033[m")
            for key, pizza in self.menu_pizzas.items():
                print(f"{key}. {pizza['nome']} - R$ {pizza['preco']:.2f}")
        elif tipo == 'bebida':
            print("\n\033[1;35;40m=== Menu de Bebidas ===\033[m")
            for key, bebida in self.menu_bebidas.items():
                print(f"{key}. {bebida['nome']}")
        print('')

    def mostrar_menu_refrigerantes(self):
        print("\n\033[1;35;40m=== Menu de Refrigerantes ===\033[m")
        for key, refri in self.menu_refrigerantes.items():
            print(f"{key}. {refri['nome']} - R$ {refri['preco']:.2f}")
        print('')

    def mostrar_menu_sucos(self):
        print("\n\033[1;35;40m=== Menu de Sucos Naturais ===\033[m")
        for key, suco in self.menu_sucos.items():
            print(f"{key}. {suco['nome']} - R$ {suco['preco']:.2f}")
        print('')

    def mostrar_menu_refrigerantes_2l(self):
        print("\n\033[1;35;40m=== Menu de Refrigerantes 2L ===\033[m")
        for key, refri in self.menu_refrigerantes_2l.items():
            print(f"{key}. {refri['nome']} - R$ {refri['preco']:.2f}")
        print('')

    def escolher_menu(self):
        while True:
            escolha_menu = input("\n\033[1;37;40mDeseja ver o menu de Pizzas (1) | Bebidas (2) | Seguir (3) | Sair (4)? (digite 1, 2, 3 ou 4): \033[m")
            if escolha_menu == '1':
                self.mostrar_menu('pizza')
                return 'pizza'
            elif escolha_menu == '2':
                self.mostrar_menu('bebida')
                return 'bebida'
            elif escolha_menu == '3':
                return 'seguir'
            elif escolha_menu == '4':
                print("\n\033[0;33;40mUm minuto...\033[m")
                time.sleep(2)
                print("\033[1;33;40mAtendimento Encerrado! Até Logo!\033[m")
                exit()
            else:
                print("\033[1;31;40mEscolha inválida, por favor digite 1, 2, 3 ou 4.\033[m")

    def adicionar_pedido(self):
        while True:
            tipo_menu = self.escolher_menu()
            if tipo_menu == 'seguir':
                break 

            escolha = input("\033[1;37;40mEscolha um item (digite o número ou 'sair' para finalizar):\033[m ")
            if escolha == 'sair':
                break
            
            if tipo_menu == 'pizza' and escolha in self.menu_pizzas:
                self.pedido.append(self.menu_pizzas[escolha])
                print(f"\033[1;32;40mAdicionada: {self.menu_pizzas[escolha]['nome']}\033[m")
            elif tipo_menu == 'bebida':
                if escolha == "1":  # Refrigerante
                    self.mostrar_menu_refrigerantes()
                    refri_escolha = input("\033[1;37;40mEscolha um refrigerante (digite o número):\033[m ")
                    if refri_escolha in self.menu_refrigerantes:
                        self.pedido.append(self.menu_refrigerantes[refri_escolha])
                        print(f"\033[1;32;40mAdicionada: {self.menu_refrigerantes[refri_escolha]['nome']}\033[m")
                    else:
                        print("\033[1;31;40mEscolha inválida.\033[m")
                elif escolha == "2":  # Suco Natural
                    self.mostrar_menu_sucos()
                    suco_escolha = input("\033[1;37;40mEscolha um suco (digite o número):\033[m ")
                    if suco_escolha in self.menu_sucos:
                        self.pedido.append(self.menu_sucos[suco_escolha])
                        print(f"\033[1;32;40mAdicionada: {self.menu_sucos[suco_escolha]['nome']}\033[m")
                    else:
                        print("\033[1;31;40mEscolha inválida.\033[m")
                elif escolha == "3":  # Água Mineral
                    self.pedido.append(self.menu_bebidas[escolha])
                    print(f"\033[1;32;40mAdicionada: {self.menu_bebidas[escolha]['nome']}\033[m")
                else:
                    print("\033[1;31;40mEscolha inválida, por favor digite um número válido.\033[m")

    def mostrar_resumo_pedido(self):
        print("\n\033[1;35;40m=== Resumo do Pedido ===\033[m")
        total = 0
        for item in self.pedido:
            print(f"{item['nome']} - R$ {item['preco']:.2f}")
            total += item['preco']
        print(f"Total: R$ {total:.2f}")

    def opcoes_pagamento(self):
        print("\n\033[1;35;40m=== Opções de Pagamento ===\033[m")
        print("1. Cartão de Crédito")
        print("2. Cartão de Débito")
        print("3. Dinheiro")
        pagamento = input("\033[1;37;40mEscolha a forma de pagamento (1, 2, 3):\033[m ")
        if pagamento in ["1", "2", "3"]:
            print("\n\033[1;32;40mPagamento realizado com sucesso!\033[m")
        else:
            print("\033[1;31;40mOpção de pagamento inválida.\033[m")

    def confirmar_pedido(self):
        self.mostrar_resumo_pedido()
        confirmacao = input("\033[1;37;40mDeseja confirmar o pedido? (s/n):\033[m ")
        if confirmacao.lower() == 's':
            self.opcoes_pagamento()
            print("\033[1;36;40mObrigado pelo seu pedido!\033[m")
        else:
            print("\033[1;31;40mPedido cancelado.\033[m")

def main():
    pizzaria = Pizzaria()
    pizzaria.adicionar_pedido()
    if pizzaria.pedido:
        pizzaria.confirmar_pedido()
    else:
        print("Nenhum pedido foi realizado.")

if __name__ == "__main__":
    main()