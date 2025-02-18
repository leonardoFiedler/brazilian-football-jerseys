# Processed Data

Dados enriquecidos a partir dos raw datas, processados por meio de scripts Python.

## brazil-teams-jersey-price-processed.csv

Arquivo processado com base no original criado e nas ligações com dados
de salário mínimo, inflação, outros.

Os seguintes dados são disponibilizados:

| Nome da Coluna         |  Descrição                                                                                            |
|------------------------|-------------------------------------------------------------------------------------------------------|
| team                   | Nome popular da equipe                                                                                |
| state                  | Sigla do estado ao qual o clube pertence                                                              |
| year                   | Ano do registro da camiseta                                                                           |
| value                  | Valor original encontrado na fonte                                                                    |
| value_int              | Valor em formato inteiro (sem os centavos), conforme encontrado na fonte                              |
| supplier               | Nome da empresa que fornece o material exportivo                                                      |
| value_add_05           | Valor inteiro com adição de 5%                                                                        |
| value_add_10           | Valor inteiro com adição de 10%                                                                       |
| value_add_15           | Valor inteiro com adição de 15%                                                                       |
| value_sub_05           | Valor inteiro com desconto de 5%                                                                      |
| value_sub_10           | Valor inteiro com desconto de 10%                                                                     |
| value_sub_15           | Valor inteiro com desconto de 15%                                                                     |
| wage_value             | Valor máximo do salário mínimo no ano do registro                                                     |
| wage_value_percent     | Percentual do valor inteiro da camiseta com relação ao salário mínimo (arredondamento de 2 casas)     |
| wage_value_percent_int | Percentual do valor inteiro da camiseta com relação ao salário mínimo (Inteiro)                       |
| ipca_value             | Valor acumulado anual do IPCA para o ano do registro                                                  |
| access_date            | Data de acesso a fonte                                                                                |
| source                 | Fonte original de onde o dado foi extraído                                                            |

## minimum_wage_historical.csv

Arquivo baixado e processado do IPEADATA com base no script `app/minimum_wage/minimum_wage.py`.

Os seguintes dados são disponibilizados:

| Nome da coluna |   Descrição                          |
|----------------|--------------------------------------|
| year           | Ano corrente                         |
| wage_value     | Máximo valor do salário mínimo no ano|