#PASSO1: Importar a base de dados
import pandas

tabela = pandas.read_csv("cancelamentos.csv") #importando a base de dados

#PASSO2: Visualizar a base de dados
tabela = tabela.drop("CustomerID", axis=1) #retirando informação irrelevante na análise
print(tabela)

#PASSO3: Tratamento de erros
print(tabela.info())
tabela = tabela.dropna() #tratando valores vazios

#PASSO4: Análise inicial dos erros (entender como estão os cancelamentos)
print(tabela["cancelou"].value_counts()) #contando valores diferentes (1 cancelou, 0 não cancelou)
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format)) #mostrando em porcentagem

print(tabela["duracao_contrato"].value_counts()) #contando valores diferentes
print(tabela["duracao_contrato"].value_counts(normalize=True).map("{:.2%}".format)) #mostrando em porcentagem

print(tabela.groupby("duracao_contrato").count())

#retirando contrato mensal da tabela
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]

#analisando novamente apos retirar contrato mensal
print(tabela["cancelou"].value_counts()) 
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

#PASSO5: Análise profunda da base de dados
import plotly.express as px #ferramenta de graficos interativos

for coluna in tabela.columns: #gerando grafico para cada coluna na tabela
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()

#retirando ligacoes call center a partir de 5 ligacoes
tabela = tabela[tabela["ligacoes_callcenter"] < 5]

#retirando dias de atraso a partir de 21 dias
tabela = tabela[tabela["dias_atraso"] <= 20]

print(tabela["cancelou"].value_counts()) 
print(tabela["cancelou"].value_counts(normalize=True))