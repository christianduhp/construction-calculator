# Calculadora de Lajes e Forro

Este é um repositório que contém o código-fonte de uma calculadora de lajes e forro para um comércio, escrita em Python.

## Sobre o projeto
A calculadora de lajes é um programa de computador desenvolvido para auxiliar no cálculo de lajes de concreto em projetos de construção civil. O objetivo deste projeto é oferecer uma ferramenta simples e eficiente para calcular a quantidade de material necessário para a construção de uma laje.

O código é uma aplicação em tkinter para calcular a quantidade de placas de forro ou laje necessárias para cobrir uma área determinada, de acordo com a largura e comprimento informados. As imagens usadas na aplicação e os cálculos para obter as sugestões de quantidade de placas e a área total necessária são definidos no código.

A função "forro" é responsável pelos cálculos e retornar o resultado a ser exibido na janela. A variável "text_forro" é um rótulo vazio que será preenchido com o resultado do cálculo. A variável "forro" é um cálculo da quantidade de placas de forro necessárias por metro, considerando uma largura padrão de 0.2m. A variável "sugestao" é a quantidade de placas necessárias para cobrir uma faixa de largura determinada pela variável "lim" (inicialmente 1), considerando a largura e comprimento informados. A variável "lim" aumenta em 1 a cada iteração, até um limite máximo de 6, e é usada para determinar o número de faixas necessárias para cobrir toda a área. Os valores de "sugestao", "lim" e "area" são adicionados a listas correspondentes para cada iteração, e a quantidade de itens nas listas determina quantas sugestões de quantidade de placas serão exibidas na janela.

Os valores nas listas são usados para formatar uma string que exibe as sugestões de quantidade de placas e a área total necessária. A variável "text_output" é preenchida com essa string, que é exibida na janela. O número de sugestões exibidas depende da quantidade de itens na lista de sugestões. Se houver apenas uma sugestão, apenas uma linha será exibida. Se houver mais de uma sugestão, cada sugestão será exibida em uma linha separada.

## Como utilizar
Para utilizar a calculadora de lajes, siga os seguintes passos:

1. Certifique-se de ter o Python 3 instalado em sua máquina. Caso não tenha, faça o download <a href="https://www.python.org/downloads/">aqui</a> 

2. Faça o clone deste repositório em sua máquina usando o seguinte comando: 'git clone https://github.com/christianduhp/calculadora-laje-forro.git'

3. Execute o arquivo calculadora_lajes.py usando o seguinte comando: 'python calculadora_lajes.py'

Siga as instruções exibidas na tela para informar as dimensões da laje a ser calculada.

## Contribuindo
Este é um projeto de código aberto e, portanto, contribuições são bem-vindas! Se você tiver alguma sugestão de melhoria ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está sob a licença MIT. Para mais informações, consulte o arquivo LICENSE.
