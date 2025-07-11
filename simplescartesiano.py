from fractions import Fraction
from matplotlib import pyplot as plt
import numpy as np

# Lógica enorme pra controlar todos os tipos de input
def ConverterTipo(value):
    try:
        value = float(Fraction(value))
        return True, float(value)
    except ValueError:
        if value == "":
            value = 0
            return True, float(value)
        else:
            return False, None
    
            
def PegarCoeficientes(name):
    while True:
        value = input(f"Insira o valor do coeficiente {name}: ")
        valid, converted = ConverterTipo(value)
        if valid == True:
            return converted
        else:    
            print(f"O coeficiente {name} deve ser um número real!")


def PlotarRaizes(roots, a):    # Função para mostrar o momento em que o gráfico toca o eixo X (y == 0)
    for i, x in enumerate(roots):   # Enumera a quantidade de raízes para alinhar corretamente o texto
        plt.scatter(x, 0, color="darkblue", zorder=5)  #Função da plt que gera pontos individuais no gráfico. No caso, para todas as roots (raízes da equação).
        # i == 0 é a primeira raíz, i == 1 é a segunda
        if (a > 0 and i == 0) or (a < 0 and i == 1):    # Check se a parábola é crescente ou decrescente, pois "xOne" é o valor a esquerda na parábola crescente e vice-versa.
            ha = "left" # Logo, sempre que a parábola é crescente, a raíz mais a esquerda é a 0. Então o melhor alinhamento é a esquerda do texto. O mesmo se aplica pro oposto
        else:
            ha = "right"    # Para a outra raíz, o melhor é alinhar na direita (legibilidade).
        plt.text(x, 0, f"x = {round(x, 2)}", fontsize="medium", ha=ha, va='bottom', color="darkblue")
    
    
# Uma função só, pela simplicidade da constante
def ConstanteC():
    print("A e B são iguais a 0. O gráfico é constante, onde Y = C.")
    xValues = np.linspace(-10, 10, 500)
    yValues = 0 * xValues + c
          
    # Plano cartesiano
    plt.axhline(0, color="black", linewidth=0.8) 
    plt.axvline(0, color="black", linewidth=0.8)
        
    plt.xlim(- 10, 10)
    plt.ylim(c - 2, c + 2)  # Margem de 2 para o limite do eixo Y ficar maior, cortando o desnecessário
        
    plt.plot(xValues, yValues, label=rf"$y = {c}$", color="red", linewidth=2)
    plt.title("Gráfico da Constante C")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.grid(True)
    plt.legend()
    plt.show()


# Uma função só, pela simplicidade da função do 1° grau
def PrimeiroGrau():
    print("A é igual a 0. A equação é do 1° grau e o gráfico é uma reta (função linear).")
    if c != 0:
        x = -c / b
    else:
        x = 0
         
    print(f"O valor de X para Y = 0 é: {round(x, 2)}.")
    print("A e B são iguais a 0. O gráfico é constante, onde Y = C.")
    xValues = np.linspace(int(x - 2), int(x + 2), 500)
    if c != 0:
        yValues = (b * xValues) + c # Soma C apenas se ele for diferente da string "empty", que conflita com o numpy.
    else:
        yValues = (b * xValues)
                   
    # Plano cartesiano
    plt.axhline(0, color="black", linewidth=0.8) 
    plt.axvline(0, color="black", linewidth=0.8)
        
    plt.xlim(- 10, 10)
    plt.ylim(np.min(yValues), np.max(yValues))  # Margem de 0 para todos os pontos serem mostrados.
        
    plt.plot(xValues, yValues, label=rf"$y = {b}x + {c}$", color="red", linewidth=2)
    PlotarRaizes([x], a)
    plt.title("Gráfico da Equação do Primeiro Grau")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.grid(True)
    plt.legend()
    plt.show()


def SegundoGrau():
    print(f"Delta = {b}² - 4 x {a} x {c}")
    valDelta = b ** 2 - (4 * a * c)
    print(f"O valor de Delta é: {valDelta}!")
        
    if valDelta > 0:
        xOne = (-b + valDelta ** 0.5) / (2 * a) 
        xTwo = (-b - valDelta ** 0.5) / (2 * a) 
        print("Essa equação possui duas raízes reais e distintas!")
        print(f"O valor de X₁ é: {round(xOne, 2)}.")
        print(f"O valor de X₂ é: {round(xTwo, 2)}.")
        return [xOne, xTwo]
    elif valDelta == 0:
        xOne = (-b + valDelta ** 0.5) / (2 * a) 
        print("Essa equação possui duas raízes reais e iguais!")
        print(f"O valor de X₁ é: {round(xOne, 2)}.")
        return [xOne]  
    else:
        print("Essa equação não possui raízes reais.")  

                    
def GrafSegundoGrau():
    roots = SegundoGrau()
    width = 10 if abs(a) > 1 else int(15 / abs(a))    # Se o valor de A for baixo, o gráfico será maior (maior amplitude).
    xVer = (-b) / (2 * a) if b != 0 else 0
    # xValues = range(int((xVer - 5)), int((xVer + 5)))   # Determina os possíveis valores de X da equação  
    xValues = np.linspace(int(xVer - width), int(xVer + width), 500)  # Determina os possíveis valores de X da equação
    yValues = a * (xValues ** 2) + (b * xValues) + c    # Calcula os valores da equação para todos os pontos de X
          
    # Plano cartesiano
    plt.axhline(0, color="black", linewidth=0.8) 
    plt.axvline(0, color="black", linewidth=0.8)
        
    plt.xlim(xVer - width - 5, xVer + width + 5)
    plt.ylim(np.min(yValues) - 5, np.max(yValues) + 5)  # Margem de 5 para o limite do eixo Y ficar mais dinâmico
        
    plt.plot(xValues, yValues, label=rf"$y = {a}x² + {b}x + {c}$", color="red", linewidth=2)
    
    if roots is not None:
        PlotarRaizes(roots, a)
    else:
        None        
                
    plt.title("Gráfico da Equação do Segundo Grau")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.grid(True)
    plt.legend()
    plt.show()
 
    
num = input("Calcule uma equação do 1° ou do 2° grau! Aperte N para sair ou qualquer tecla para iniciar. ").upper()

while not "N" in num:
    a, b, c = [PegarCoeficientes(v) for v in ["A", "B", "C"]] # Pega os valores de A, B e C com line comprehension.
    if (a == 0) and (b == 0):
        ConstanteC()
    elif (a == 0) and (b != 0):
        PrimeiroGrau()
    else:    
        GrafSegundoGrau()
    
    num = input("Aperte N para sair ou qualquer tecla para reiniciar. ").upper()





