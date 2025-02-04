# Raw Data

Arquivos em formato bruto, preenchidos manualmente ou baixados diretamente de suas fontes.

## brazil-teams-jersey-price.csv

O arquivo csv presente neste diretório é o arquivo original, que dá início ao trabalho.
Este é o arquivo que deve ser alterado ao adicionar dados de uma nova equipe.

Abaixo, segue a relação dos metadados das colunas coletadas originalmente.

| Nome da coluna |   Descrição                              |
|----------------|------------------------------------------|
| team           | Nome da equipe                           |
| state          | Sigla do estado ao qual o clube pertence |
| year           | Ano de referência do preço               |
| value          | Valor, em reais, do preço encontrado     |
| access_date    | Data do acesso ao site                   |
| source         | Site onde o valor foi encontrado         |


## IPCA.csv

Arquivo obtido através do site do [IPEADATA](http://ipeadata.gov.br/Default.aspx).
Indica o valor acumulado do IPCA ao longo dos anos, entre o período de 1980 e 2024.

Os seguintes dados são disponibilizados:

| Nome da coluna |   Descrição                          |
|----------------|--------------------------------------|
| year           | Ano de referência                    |
| ipca_value     | Valor percentual acumulado do IPCA   |