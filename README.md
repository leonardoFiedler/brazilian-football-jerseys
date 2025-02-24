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

## Acesso aos dados

Acesse os [dados processados aqui](./data/processed/brazil-teams-jersey-price-processed.csv).
Todas as informações sobre as colunas podem ser encontradas [aqui](./data/processed/README.md)

Caso queira contribuir com o projeto, deve-se realizar a adição de 
novos dados no [arquivo de dados brutos](./data/raw/brazil-teams-jersey-price.csv).
Todas as informações sobre as colunas que devem ser preenchidas podem 
ser encontradas [aqui](./data/raw/README.md).

Caso queira explorar os dados por meio de um notebook, 
os dados também estão 
[publicados no Kaggle](https://www.kaggle.com/datasets/leonardofiedler/brazil-teams-jersey-price).

## Dados Disponíveis

Atualmente o dataset contempla 4 clubes de maneira total e 8 de forma parcial.
9 clubes possuem apenas um único registro.

### Completo

* Flamengo
* Vasco
* Corinthians
* Palmeiras
* Grêmio
* Internacional
* Botafogo
* Fluminense
* Atlético-MG
* Cruzeiro
* São Paulo
* Santos

### Parcial

* Fortaleza

### Apenas um registro

* Athletico-PR
* Sport
* Bragantino
* Coritiba
* Ceará
* Bahia
* Goiás
* Atlético-GO

## Pré-requisitos

1. Instalar o Python
2. Instalar a [lib UV](https://docs.astral.sh/uv/)
3. Instalar o make

## Informações Adicionais

1. Camisa do Vasco (2013) é relatado que o valor varia entre R$177,00 e R$199,00, 
dependendo do modelo. No entanto, não foi encontrado nenhuma outra fonte comprovando.
2. Camisa do Cruzeiro (2013) foi encontrado apenas um comentário no site [Camisa de Futebol](https://camisadefutebol.wordpress.com/2013/01/31/nova-camisa-do-cruzeiro-201314/) relatando seu preço de lançamento.

## Como executar os scripts?

1. Utilize o comando `make create_venv` para criar a virtual environment
2. Ative a venv com o comando `source .venv/bin/activate`
3. Com a venv ativada, baixe os pacotes usando o comando: `uv sync`
4. Para testar se a geração está funcionando, basta executar: `make gen_data`