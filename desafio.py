def soma_tupla(tupla):
    """
    Calcula a soma de todos os elementos de uma tupla de inteiros, com validação.

    Args:
      tupla: Uma tupla de números inteiros.

    Returns:
      A soma de todos os elementos da tupla.
    """
    return sum(tupla)

def obter_tupla_inteiros():
    """
    Solicita a entrada do usuário até que uma tupla de inteiros seja fornecida.

    Returns:
      Uma tupla de números inteiros.
    """
    while True:
        entrada = input("Digite números inteiros separados por espaços: ")
        try:
            numeros = tuple(map(int, entrada.split()))
            return numeros
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir apenas números inteiros separados por espaços.")
        except TypeError:
            print("Entrada inválida. Certifique-se de inserir apenas números inteiros separados por espaços.")
        except Exception:
          print("Entrada inválida. Certifique-se de inserir apenas números inteiros separados por espaços.")

# Obtém a tupla de inteiros do usuário
numeros = obter_tupla_inteiros()

# Calcula a soma
resultado = soma_tupla(numeros)

# Imprime o resultado
print(f"A soma dos elementos da tupla é: {resultado}")
