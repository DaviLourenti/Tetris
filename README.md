# Tetris
Um dia eu tava entediado e sem internet, então eu fiz um tetris no papel, fiz uma versão pré-historica no computador (que só roda no terminal), 
e finalmente depois de tomar coragem eu fiz um joguinho do tetris de verdade, só tenho que atualizar/adicionar algumas coisas e corrigir alguns bugs.

## Controles:

**[seta para cima]** _faz o player girar_

**[seta para baixo]** _faz o player descer mais rapido_

**[seta para direita]** _se move para direita_

**[seta para esquerda]** _se move para esquerda_

**[espaço]** _ativa uma função especial extra_ 

### Video demonstrativo haha 😆:

![ezgif com-optimize](https://user-images.githubusercontent.com/96353013/229895466-544be0b6-26a9-4f04-9e21-27b146ab4e40.gif)

## Sistema de pontos:

Cada segundo no jogo adiciona um ponto ao jogador.
Ao limpar uma linha o player ganha o equivalente a dez pontos.
Precionando espaço o player ganha 6 pontos.

## Sistema de dificuldade:

Quanto mais pontos o player ter, mais rapido sua peça descera ao chão.
Eventualmente o placar de peças diminui até você não saber qual sera a proxima peça.
O ciclo de peças, ou seja, de quanto em quato tempo todas as peças serão repetidas sera maior,
isso significa que o player pode ficar por um bom tempo sem ver alguma peça em especifico.

## Sistema de punição:

Se o player precionar espaço em mais de três peças doferentes ele automaticamente recebe uma punição aleatoria.
As punições são acumulativas e irreversiveis, 
então chega num ponto que o player só se lasca a ponto de não conseguir jogar por muito mais tempo.
Aceitamos sugestões para punições inucitadas.

## Ranking 

Por enquanto os pontos serão guardados em um json local.
Futuramente adicionarei um ranking conectado a internet referente a esse repositorio, sera um ranking unico.
Porem mais futuramente ainda pretendo adicionar um sistema de convite e criação de rankings propios para os jogadores poderem interagir mais entre si e terem mais privacidade.
Sendo assim, três tipos de rankings, o local, o "global", e o ranking fechado (somente para convidados)

## Placar 

O placar que aparece Durante o jogo é responsavel por demonstar a quantidades de pontos acomulados,
desmonstrar as proximas peças que serão usadas pelo player, e indicar o nivel de dificuldade em que o jogador se encontra.
Além disso, talvez eu adicione um sistema que compara a posição do player em relação 
aos potos do player ao ranking local em tempo real.