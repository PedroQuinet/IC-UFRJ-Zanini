#IC-UFRJ-Zanini

Este é somente um repositório para IC com o professor Carlos T. P. Zanini 

Uma das referencias é: https://keras.io/guides/transfer_learning/, também estamos usando um antigo projeto de IC do professor (botei as pastas com as fotos no .gitignore pra não pesar na hora de mandar pro github)

Estamos usando o Python 3.12.5 e as versões das bibliotecas estão no requirements.txt

1º passo: Ler https://keras.io/guides/transfer_learning/

2º passo: Rodar o tutorial como está e eventualmente corrigir codigo desatualizado.

3º passo: Escolher arquitetura CNN (1)

3.1) Com pesos congelados na memória durante o treino. MLP recebendo penultima camada como input (1,2 e 3 camadas).
3.2) Transformando as imagens para a penultima camada do modelo. MLP recebendo penultima camada como input. (1,2 e 3 camadas)
3.3) Fazer fine tunning no modelo que performou melhor.
 
resultados:

1) acuracia treino e teste a cada iteração (grafico de linhas)
2) tempo computacional
3) acuracia eixo y e tempo da iteração no eixo x
