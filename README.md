# Brazil teams Jersey Price

## Sobre




A análise está focada na versão "Torcedor"/Masculina/Adulta das camisetas oficiais das equipes.
Este modelo é o mais próximo da versão final, porém utiliza um material 
um pouco mais simples que o final. Versões femininas e infantis costumam ser mais baratas 
que a versão torcedor masculina. 
Além disso, esta análise não leva em conta a eventual adição de números ou patches nas camisas.

Infelizmente, não possível achar os valores apenas para a versão número 1 dos uniformes,
sendo assim, algumas versões contam com valores das camisetas número 2 ou 3 
lançadas pelos clubes no ano.

Em todos os valores, é possível encontrar a sua fonte de referência. 
Para demarcar o valor real de época, foi optado por buscar notícias 
do ano corrente do lançamento, afim de garantir sua real veracidade. 
Também foi tentado colocar os valores de lançamento das camisetas, no entanto, 
nem sempre foram encontradas notícias contendo o preço. 

Caso algum valor esteja incorreto, fique à vontade para abrir um PR 
e contribuir com o projeto.

## Dados Brutos

Acesse o csv com dados coletados [clicando aqui](./raw/data.csv)

## Metadata

| Nome da coluna |   Descrição                          |
|----------------|--------------------------------------|
| team           | Nome da equipe                       |
| year           | Ano de referência do preço           |
| value          | Valor, em reais, do preço encontrado |
| access_date    | Data do acesso ao site               |
| source         |  Site onde o valor foi encontrado    |

## Pré-requisitos

1. Instalar o Python
2. Instalar a lib UV

## Informações Adicionais

1. Camisa do Vasco (2013) é relatado que o valor varia entre R$177,00 e R$199,00, 
dependendo do modelo. No entanto, não foi encontrado nenhuma outra fonte comprovando.