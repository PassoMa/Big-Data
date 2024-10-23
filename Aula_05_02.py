import pandas as pd
# Importando a Base de Dados
endereco_dados = 'BASES\Financeira.csv'
# Criando o DataFrame 
# encoding = 'iso-8859-1'padrão da tabela portugues-Brasil(aceita as pontuações das palavras) / SEP = separador padrão do .csv(';' "," ou '-' )
df_financeira = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')

# Exibindo os Dados do DataFrame 
print('---- DADOS FINANCEIROS ----')

