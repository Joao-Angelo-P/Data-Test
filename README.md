# Data-Test (Rascunho)
<h2>Olá, Seja Bem-Vindo!</h2>
<p>Este é meu codigo-fonte para se aplicar a uma base de dados de voltametria
ciclica. Os dados apresentados aqui são livres para se baixar foi para se 
dedectar Ácido Ascórbico de um efervescente de vitamina C daqui em diante chamarei de AA.</p>
<article>
  <h2>O que seria voltametria cíclica?</h2>
  <p>A voltametria é uma técnica eletroquímica onde as informações qualitativas e quantitativas de uma espécie química são obtidas a partir do registro de curvas corrente-potencial, feitas durante a eletrólise dessa espécie em uma cela eletroquímica constituída de pelo menos dois eletrodos, sendo um deles um microeletrodo (o eletrodo de trabalho) e o outro um eletrodo de superfície relativamente grande (usualmente um eletrodo de referência). O potencial é aplicado entre os dois eletrodos em forma de varredura, isto é, variando-o a uma velocidade constante em função do tempo. O potencial e a corrente resultante são registrados simultaneamente. A curva corrente vs. potencial obtida é chamada de voltamograma.</p>
</article>

Instrumentação necessária:
<blockquote>
<div>
<p>a)potenciostato com gerador de programa de potencial;</p>
<p>b)computador para registrar os gráficos de corrente em função do
potencial</p>
<p>c)célula convencional de três eletrodos e uma solução contendo o
analito e eletrólito suporte.</p>
A voltametria cíclica é uma modificação da técnica de varredura
rápida em que se inverte a direção de varredura, segundo a
redução de interesse. Para conseguir isso se aplica uma
voltagem chamada onda triangular a célula eletrolítica.
</div>
</blockquote>

<article>
  <h2>E sobre o gráfico?</h2>
  <p>potencial de pico catódico (Epc); potencial de picoanódico (Epa); corrente de pico catódico (ipc); corrente de pico anódico (ipa). 
A corrente de pico para sistemas reversíveis é descrita pela equação de
Randles-Sevcik:
    Ip=2,69 . 10<sup>5</sup>n<sup>3/2</sup> AD<sup>1/2</sup>Cv<sup>1/2</sup></p>
</article>

Créditos e para <a href="http://www.riidfcm-cyted.fq.edu.uy/archivos/Curso_Tecnicas_aplicadas_al_desarrollo_de_metalofarmacos/presentaciones_clases/Voltametria.pdf#:~:text=A%20voltametria%20c%C3%ADclica%20compreende%20um%20grupo%20de%20m%C3%A9todos,eletrodo%20de%20trabalho%2C%20atrav%C3%A9s%20do%20uso%20de%20microeletrodos.">saber mais</a> 

<h2>Código-Fonte e arquivos</h2>
<p>Os arquivos são descritos da seguinte forma: <strong>AA(Ácido Ascórbico)(número de até quatro dígitos)(microlitro(μL/10<sup>-6</sup>L)).csv</strong></p> 
Vamos para parte da linguagem Python ou o programa: 
Primeiramente, vamos ver o arquivo principal "molde.py":
import pandas as pd
import matplotlib.pyplot as plt
