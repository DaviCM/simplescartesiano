# simplescartesiano

Um script simples para visualizar gráficos de equações do 1° e do 2° grau com python e matplotlib!

# Como Instalar:

Existem duas formas de rodar o simplescartesiano:

1. A primeira é clicando em "simplescartesiano.exe" ou no arquivo zip e instalando diretamente na sua máquina. Ele é portátil e roda no terminal do Windows, e o zip pode ser descompactado por qualquer descompactador de arquivos.
   
2. A segunda é compilando o arquivo "simplescartesiano.py" você mesmo, com um programa dedicado. Eu utilizei a biblioteca "pyinstaller" para compilar, mas existem outras.

# Uso:

Muito intuitivo, com todas as instruções no terminal. Caso você digite um valor inválido, o aplicativo avisará e pedirá a reinserção do mesmo. Após visualizar o gráfico, feche-o pelo menu do próprio Windows.

# IMPORTANTE: 
É necessário fechar o gráfico antes de iniciar outra operação, pois os terminais dos sistemas operacionais (CMD, Powershell, ZSH, Konsole etc.) usam um buffer para inputs do usuário. Isso significa que, mesmo sem nenhum indício visual, os dados digitados estão sendo armazenados em uma "tabela", e serão processados pelos inputs assim que eles estiverem disponíveis, por ordem de digitação. Na prática, se você digitar ou pressionar "Enter" enquanto o gráfico ainda está aberto, essas ações ficarão "em espera" e serão executadas em sequência assim que o gráfico for fechado — o que causará saltos inesperados entre etapas do programa.


