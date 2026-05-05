# Diário de Bordo de IA - Leticia O Messias P

## 2026-03-24 ----------------------------------------------
### Dificuldade encontrada
Eu gostaria de saber como eu poderia melhorar o meu código ainda mais,
colocando uma exceção para caso o usuário não digitasse um número inteiro
e sim uma string, mas gostaria que caísse em uma mensagem de erro.

### Prompt enviado para a IA
Como eu poderia fazer esse codigo cair em uma mensagem de erro caso o usuário digite algo bobo como "banana", ao invés de um número inteiro?

### Resposta da IA (Resumo)
Para evitar isso e ufazer o código cair na sa mensagem de erro (ou pedir novamente), usamos o bloco try...except. Ele serve para "tentar" executar um código e, se der erro, capturar esse erro antes de o programa fechar.

### Minha análise e aprendizado
Entendi que ao utilizando Try e Except podemos incluir exceções para os casos de o
usuário digiar algo que não corresponde ao que se pede. Ao cair em `except ValueError`
O computador já entende que houve algum erro na digitação, então volta do início e pede
que digite um comando novamente.

## 2026-04-07 ----------------------------------------------
### Dificuldade encontrada
Tive dúvidadas em relação ao uso de For i, elemento in enumerate,
mais específicamente sobre o comando `enumerate`.

### Prompt enviado para a IA
Pode me explicar como se eu fosse burra o que faz a função `enumerete` em python?
### Resposta da IA (Resumo)
Imagine que você está organizando uma fila de pessoas.

Se você usar um comando comum (um for simples), você consegue ver quem são as pessoas, mas não sabe em qual posição da fila elas estão. O enumerate é o "organizador" que passa um crachá com o número da posição para cada pessoa conforme elas passam por você.
### Minha análise e aprendizado
Compreendi que o comando `enumerate` é um contador automático que determina a posição dos elementos dentro da lista.
Portanto, nos permite numerá-los e organizá-los.

## 2026-04-17 ----------------------------------------------
### Dificuldade encontrada
Pedi ao Gemini que me ajudasse a entender onde utilizar a tupla para armazenar o histórico
de updates do meu portfólio.

### Prompt enviado para a IA
Gemini, como eu poderia acrescentar uma tupla que armazenasse o histórico de atualizações do meu portfólio? Esta tupla precisa estar dentro de umas lista.
### Resposta da IA (Resumo)
Claro! Usar tuplas para o histórico é uma excelente decisão de design. Como tuplas são imutáveis (não podem ser alteradas depois de criadas), elas funcionam como um "carimbo" ou uma foto fixa do estado do livro naquele momento, garantindo que o histórico não seja modificado acidentalmente.

A Lógica
Onde guardar: Dentro do dicionário de cada livro, teremos a chave "historico": [].

O que guardar: Antes de o usuário digitar o novo valor no UPDATE, nós pegamos os valores atuais (antigos), colocamos em uma tupla (nome, autor, resumo) e damos um .append() na lista de histórico.

Por que tupla: Porque o histórico deve ser apenas para leitura. Se você usasse uma lista dentro da lista, poderia alterar um dado antigo sem querer.

### Minha análise e aprendizado
Entendi que para usar o dicionário como um método de backup e histórico, preciso que ele armazene cada alteração em tuplas, o que as faz imutáveis depois de preenchidas.

## 2026-04-24 ----------------------------------------------
### Dificuldade encontrada
Estava com dificuldade em como eu podeeria usar funções no meu UPDATE e DELETE.
### Prompt enviado para a IA
Enviei o código a IA depois de várias tentativas fracassadas. Perguntei o motivo de as minhas funções não estarem funcionando.
### Resposta da IA (Resumo)
Analisando o código, encontrei vários problemas. Vou explicar cada um e apresentar o código corrigido.
Problemas encontrados:

procurar_livro() — A função referencia lista_cadastros mas o parâmetro se chama lista_de_cadastros. Além disso, não retorna nada nem marca encontrado.
Chamada procurar_livro() no UPDATE — É chamada sem argumentos, e o resultado não é usado.
Indentação errada no UPDATE — O backup, livro["historico"].append(...) e os if/elif de alteração estão fora do for, e o break está no lugar errado.
break em vez de continue/pass no UPDATE — Usar break ao receber opção inválida sai do while True, encerrando o programa.
print("Programa encerrado...") fora do if/elif — Está no nível do while, então é impresso a cada iteração, não só ao sair.
Variável encontrado não declarada no UPDATE — É usada no if not encontrado mas nunca inicializada nesse bloco.

### Minha análise e aprendizado
Meu código apresentava várias inconsistências, começando pelos parâmetros digitados incorretamente. Além disso, esqueci de atribuir a uma variável o resultado da procura pelo livro (None ou encontrado). Ademais, alguns erros de identação.
## 2026-04-24 ----------------------------------------------
### Dificuldade encontrada
### Prompt enviado para a IA
### Resposta da IA (Resumo)