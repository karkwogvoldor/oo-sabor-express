from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_jorje_sushi = Restaurante('Jorje Sushibar', 'Japonesa')
restaurante_pimenta_loka = Restaurante('Pimenta Loka', 'Mexicana')
restaurante_pimenta_loka.alternar_estado()
restaurante_praca.receber_avaliacao('Jeronimo', 5)
restaurante_praca.receber_avaliacao('Maria', 4)
restaurante_praca.receber_avaliacao('João', 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()