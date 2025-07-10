# IC-UFRJ-Zanini
Repositório para IC com o professor Carlos Zanini

Uma das referencias é: https://keras.io/guides/transfer_learning/, também estamos usando um antigo projeto de IC do professor (botei as pastas com as fotos no .gitignore pra não pesar na hora de mandar pro github)

1) rodar o tutorial como está e eventualmente corrigir codigo desatualizado

2) Escolher arquitetura CNN (1)

2.1) Com pesos congelados na memória durante o treino. MLP recebendo penultima camada como input (1,2 e 3 camadas).
2.2) Transformando as imagens para a penultima camada do modelo. MLP recebendo penultima camada como input. (1,2 e 3 camadas)
2.3) Fazer fine tunning no modelo que performou melhor.
 
resultados:

1) acuracia treino e teste a cada iteração (grafico de linhas)
2) tempo computacional
3) acuracia eixo y e tempo da iteração no eixo x
