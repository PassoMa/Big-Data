import pandas as pd

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
print('\n---- OBTENDO DADOS GERIAS SOBRE OCORRÊNCIAS----')
print(df_ocorrencias.head())

#Criando DataFrame Roubo de Veículos
df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]
#reset.index = ordem alfabetica ou crescente / groupby = agrupar
df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index() 
print('\n---- OBTENDO DADOS SOBRE ROUBOS DE VEÍCULOS ----')
print(df_roubo_veiculo.head())

#Criando DataFrame Homicídio doloso por ano
df_ano_homic_dolosos = df_ocorrencias[['ano','hom_doloso']]
df_ano_homic_dolosos = df_ano_homic_dolosos.groupby(['ano']).sum(['hom_doloso']).reset_index() 
print('\n---- OBTENDO DADOS SOBRE HOMICÍDIOS DOLOSOS ----')
print(df_ano_homic_dolosos.head())

#Criando DataFrame Homicídio doloso e Culposos por Delegacia
df_homic_doloso_culposo = df_ocorrencias[['cisp','hom_doloso','hom_culposo']]
df_homic_doloso_culposo = df_homic_doloso_culposo.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index() 
print('\n---- OBTENDO DADOS SOBRE HOMICÍDIOS DOLOSOS e CULPOSOS por DELEGACIA----')
print(df_homic_doloso_culposo.head())