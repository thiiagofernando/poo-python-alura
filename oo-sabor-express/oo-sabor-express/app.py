from modelos.restaurante import  Restaurante

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_mexicano = Restaurante('Mexican Food','Comida Mexicana')
restaurante_japones = Restaurante('Japa','Comida Japonesa')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()