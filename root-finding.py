"""
Objetivo:
Este script demonstra o uso de métodos numéricos para encontrar raízes reais de funções,
utilizando as funções otimizadas da biblioteca scipy.optimize.
São abordados os métodos de Bissecção, Newton-Raphson e Secante (via newton),
além da função fsolve para demonstrar uma abordagem mais genérica e robusta.
Cada chamada de método está encapsulada em um bloco try-except para tratamento de erros individualizado,
garantindo a execução completa da demonstração mesmo em caso de falhas específicas.

Entradas:
- Uma função f(x)
- Intervalo [a, b] para bissecção ou chutes iniciais (x0, x1) para newton/fsolve
- Tolerância e número máximo de iterações (gerenciados internamente pelas funções scipy)

Saídas:
- Raiz aproximada da função
- Mensagens de erro caso um método não consiga convergir ou tenha problemas de entrada.
"""
# Instalações necessárias:
# pip install numpy scipy matplotlib

import numpy as np
from scipy.optimize import bisect, newton, fsolve
import matplotlib.pyplot as plt

# -------------------------------
# Função alvo (exemplo: f(x) = x³ - x - 2)
def f(x):
    return x**3 - x - 2

# Derivada de f(x) para o método de Newton-Raphson (opcional para newton)
def df(x):
    return 3*x**2 - 1

# -------------------------------
# Funções de Suporte (Gráfico)

def plotar_funcao(f, intervalo, raiz_encontrada=None, metodo_nome=None):
    """
    Plota a função e, opcionalmente, uma raiz encontrada.
    """
    x = np.linspace(intervalo[0], intervalo[1], 400)
    y = f(x)
    plt.figure(figsize=(10, 6))
    plt.axhline(0, color='gray', lw=1, linestyle='--')
    plt.plot(x, y, label='f(x)')
    
    if raiz_encontrada is not None:
        plt.plot(raiz_encontrada, f(raiz_encontrada), 'ro', markersize=8, label=f'Raiz Encontrada ({metodo_nome})')
        plt.axvline(raiz_encontrada, color='red', linestyle=':', lw=1)

    plt.title(f"Gráfico da função f(x) = x³ - x - 2")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

# -------------------------------
# Demonstração Prática: Usando Métodos Numéricos

print("--- Zero de Função e Aplicações (Métodos Numéricos com scipy.optimize) ---")
print("Função em análise: f(x) = x³ - x - 2")

# --- Entrada de Dados pelo Usuário ---
try:
    a_bisseccao = float(input("\nDigite o valor de 'a' (início do intervalo para Bissecção): "))
    b_bisseccao = float(input("Digite o valor de 'b' (fim do intervalo para Bissecção): "))
    x0_chute_inicial = float(input("Digite o chute inicial 'x0' para Newton-Raphson e fsolve: "))
    x1_secante_chute = float(input("Digite o segundo chute 'x1' para o Método da Secante (via newton): "))
except ValueError:
    print("\nErro: Entrada inválida. Por favor, digite números válidos.")
    exit() # Sai do programa se a entrada inicial for inválida

print("\n--- Demonstração: Métodos Numéricos (scipy.optimize) ---")
    
# --- Método da Bissecção com scipy.optimize.bisect ---
print("\n[Método da Bissecção - scipy.optimize.bisect]")
try:
    raiz_bisect_scipy = bisect(f, a_bisseccao, b_bisseccao)
    print(f"   Raiz encontrada: {raiz_bisect_scipy:.6f}")
    plotar_funcao(f, (min(a_bisseccao, b_bisseccao, raiz_bisect_scipy)-0.5, max(a_bisseccao, b_bisseccao, raiz_bisect_scipy)+0.5), raiz_bisect_scipy, "Bissecção SciPy")
except ValueError as e:
    print(f"   Erro: Falha na Bissecção. {e}")
except Exception as e:
    print(f"   Erro inesperado na Bissecção: {e}")

# --- Método de Newton-Raphson com scipy.optimize.newton ---
print("\n[Método de Newton-Raphson - scipy.optimize.newton com fprime]")
try:
    # Fornecer fprime=df garante que o método de Newton-Raphson seja usado.
    raiz_newton_scipy = newton(f, x0_chute_inicial, fprime=df)
    print(f"   Raiz encontrada: {raiz_newton_scipy:.6f}")
    plotar_funcao(f, (min(x0_chute_inicial, raiz_newton_scipy)-0.5, max(x0_chute_inicial, raiz_newton_scipy)+0.5), raiz_newton_scipy, "Newton-Raphson SciPy")
except RuntimeError as e: # Comum para falhas de convergência em newton
    print(f"   Erro: Falha na convergência do Newton-Raphson. {e}")
except ValueError as e: # Pode ocorrer se a derivada inicial for zero
    print(f"   Erro de valor no Newton-Raphson: {e}")
except Exception as e:
    print(f"   Erro inesperado no Newton-Raphson: {e}")
    
# --- Método da Secante com scipy.optimize.newton (sem fprime) ---
print("\n[Método da Secante - scipy.optimize.newton (sem fprime)]")
try:
    # Quando fprime não é fornecido, newton tenta usar o método da Secante.
    # É bom fornecer dois chutes iniciais (x0 e x1) para direcioná-lo.
    raiz_secante_scipy = newton(f, x0_chute_inicial, x1=x1_secante_chute)
    print(f"   Raiz encontrada: {raiz_secante_scipy:.6f}")
    # CORREÇÃO APLICADA AQUI:
    plotar_funcao(f, (min(x0_chute_inicial, x1_secante_chute, raiz_secante_scipy)-0.5, max(x0_chute_inicial, x1_secante_chute, raiz_secante_scipy)+0.5), raiz_secante_scipy, "Secante SciPy")
except RuntimeError as e:
    print(f"   Erro: Falha na convergência da Secante. {e}")
except ValueError as e: # Pode ocorrer se os chutes iniciais forem iguais ou causar divisão por zero
    print(f"   Erro de valor na Secante: {e}")
except Exception as e:
    print(f"   Erro inesperado na Secante: {e}")

# --- Método fsolve com scipy.optimize.fsolve ---
print("\n[Método fsolve - scipy.optimize.fsolve]")
try:
    # fsolve é muito robusto e recomendado para uso geral.
    # Ele retorna um array, então pegamos o primeiro elemento para uma única raiz.
    raiz_fsolve_scipy = fsolve(f, x0_chute_inicial)[0]
    print(f"   Raiz encontrada: {raiz_fsolve_scipy:.6f}")
    plotar_funcao(f, (min(x0_chute_inicial, raiz_fsolve_scipy)-0.5, max(x0_chute_inicial, raiz_fsolve_scipy)+0.5), raiz_fsolve_scipy, "fsolve SciPy")
except RuntimeError as e: # fsolve também pode lançar RuntimeError em caso de não convergência
    print(f"   Erro: Falha na convergência do fsolve. {e}")
except Exception as e:
    print(f"   Erro inesperado no fsolve: {e}")

# Gráfico geral da função para visualização (sem focar em uma raiz específica)
print("\nGráfico geral da função para visualização (intervalo padrão):")
plotar_funcao(f, (0, 3))