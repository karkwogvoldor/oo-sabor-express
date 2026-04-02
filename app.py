from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_jorje_sushi = Restaurante('Jorje Sushibar', 'Japonesa')
restaurante_pimenta_loka = Restaurante('Pimenta Loka', 'Mexicana')
restaurante_pimenta_loka.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()