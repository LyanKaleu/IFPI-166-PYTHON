# 04. Um alienígena chamado Zob precisa de ajuda para converter anos terrestres em anos espaciais! Sabendo que 1 ano
# terrestre equivale a meio ano espacial, calcule e imprima uma idade inserida pelo usuário em anos espaciais.

# Importa a função 'floor' do módulo 'math'. A função 'floor' retorna o maior número inteiro menor ou igual a um dado
# número
from math import floor


# Esta função recebe a idade em anos terrestres como entrada
def converter_ano(ano_terrestre):

    # Calcula a idade em anos espaciais multiplicando a idade terrestre por 0,5
    ano_espacial = 0.5 * ano_terrestre

    # Usa a função 'floor' para arredondar para baixo e retorna a idade em anos espaciais
    return floor(ano_espacial)


# Essa função é o programa principal
def main():

    # Pede ao usupario que insira sua idade em anos terrestres, chamando a função 'converter_ano()' com a idade
    # inserida como argumento
    ano_espacial = converter_ano(int(input("Digite sua idade: ").strip()))

    # Arredonda a idade espacial usando 'round()'
    ano_espacial = round(ano_espacial)

    # Imprime a idade espacial na tela
    print(f"\n\n-> SUA IDADE EM ANOS ESPACIAIS: {ano_espacial} ANOS!")


# Verifica se o script está sendo executado diretamente(não importado como um módulo em outro script)
if __name__ == '__main__':
    main()
