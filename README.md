# Disciplina: Lógica de Programação
# Escritório de Projetos: Fase 01.
Projeto realizado para o Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas: Full-Stack e Mobile.

## Introdução:
O projeto é individual e está organizado em duas fases. Em ambas as fases, você trabalhará com dados meteorológicos. Na primeira fase, você desenvolverá um programa que realiza análises a partir de dados informados pelo usuário. Já na segunda fase, sua implementação receberá como entrada dados vindos de um arquivo.

## Enunciado da Fase 01:
Implemente um programa que leia, valide e analise dados informados pelo usuário. Os dados são meteorológicos e referem-se aos dados de 2021 (de janeiro a dezembro) registrados em uma cidade.

Toda entrada de dados deve ser validada. No caso de valor inválido, informe ao usuário o erro e permita que ele redigite o dado.

**Seu programa deve coletar os seguintes dados:**
* Mês: use valor numérico de 1 a 12 (janeiro a dezembro) para se referir aos meses do ano.   

**Para cada mês do ano, informe:**
* Temperatura máxima do mês: devem estar em Celsius, garanta que estejam dentro de um intervalo válido para temperaturas, tal como: -60 graus à +50 graus.   

**A seguir, seu programa deve calcular e exibir:**
* Temperatura média máxima anual: exibe a média das temperaturas máximas informadas.
* Quantidade de meses escaldantes: quantidade de meses com temperaturas acima de 38  graus Celsius.
* Mês mais escaldante do ano: mês que registrou a maior temperatura máxima dentre todos os informados. O mês deve ser escrito na tela por extenso (janeiro a dezembro).
* Mês menos quente do ano: mês que registrou a menor temperatura máxima dentre todos os informados. O mês deve ser escrito na tela por extenso (janeiro a dezembro).  

**Antes de enviar, teste o seu programa com os seguintes dados:**
|Mês|Temperatura|
|---|-----------|
|1  |34,3       |
|2  |36         |
|3  |31         |
|4  |31,7       |
|5  |31         |
|6  |20         |
|7  |17         |
|8  |42,5       |
|9  |37         |
|10 |32,1       |
|11 |33         |
|12 |23         |

Garanta que funcione para os dados da tabela e para outros que viermos a inserir em seu programa. Não esqueça de testar com dados inválidos para se certificar que você implementou as validações corretamente.

**Observações gerais:**
* Use repetição para ler os dados e calcular as estatísticas solicitadas.
* Não é necessário manter os dados lidos na memória após término do programa.    
