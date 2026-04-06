from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Laranja', 5.0, '500mL')
bebida_suco.aplicar_desconto()
prato_lasanha = Prato('Lasanha', 20.0, 'Lasanha à Bolonhesa')
prato_lasanha.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_lasanha)



def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()