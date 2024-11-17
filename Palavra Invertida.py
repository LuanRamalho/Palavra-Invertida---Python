def main():
    # Solicita ao usuário que insira uma palavra
    palavra = input("Digite uma palavra: ")
    
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    
    # Exibe a palavra invertida
    print("A palavra invertida é:", palavra_invertida)

    #Termina o programa
    input()

# Executa o programa principal
if __name__ == "__main__":
    main()
