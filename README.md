# Brazil Teams Jersey Price

## Objetivo

O objetivo deste repositório é compartilhar dados públicos sobre a evolução dos preços das 
camisas dos clubes brasileiros. A ideia é coletar informações sobre os preços das camisas 
dos principais times do Brasil e analisar sua evolução, contrastando-a com outros aspectos, 
como o salário mínimo, o momento da equipe e outros indicadores sociais e econômicos.

A análise inicial está focada na versão "Torcedor"/Masculina/Adulta das camisetas
oficiais das equipes. 
Este modelo é o mais próximo da versão usada em campo, porém utiliza um material um pouco mais 
simples que o das camisas dos jogadores. Versões femininas e infantis costumam ser mais baratas 
que a versão torcedor masculina. Além disso, esta análise não leva em conta a eventual adição 
de números ou patches nas camisas.

Infelizmente, não foi possível encontrar os valores apenas para a versão número 1 dos uniformes. 
Sendo assim, em alguns casos, os valores correspondem às camisetas número 2 ou 3 lançadas pelos clubes no ano.

Todos os valores apresentados possuem uma fonte de referência. Para garantir a precisão dos 
valores de época, optou-se por buscar notícias do ano de lançamento das camisas. Também 
foi priorizado o uso dos valores de lançamento das camisetas, mas nem sempre foi possível 
encontrar esses preços.

Caso você encontre algum erro, fique à vontade para abrir um PR e contribuir com o projeto.

## Dados Brutos

Acesse o csv com dados coletados [clicando aqui](./data/raw).

## Dados Disponíveis

Atualmente o dataset contempla 4 clubes de maneira total e 8 de forma parcial.
9 clubes possuem apenas um único registro.

### Completo

* Flamengo
* Vasco
* Corinthians
* Palmeiras

### Parcial

* Botafogo
* Fluminense
* Grêmio
* Internacional
* Atlético-MG
* Cruzeiro
* São Paulo
* Santos

### Apenas um registro

* Athletico-PR
* Sport
* Bragantino
* Fortaleza
* Coritiba
* Ceará
* Bahia
* Goiás
* Atlético-GO

## Pré-requisitos

1. Instalar o Python
2. Instalar a [lib UV](https://docs.astral.sh/uv/)

## Informações Adicionais

1. Camisa do Vasco (2013) é relatado que o valor varia entre R$177,00 e R$199,00, 
dependendo do modelo. No entanto, não foi encontrado nenhuma outra fonte comprovando.