df_cisp_roubo = df_ocorrencias[['cisp','roubo_veiculo']]

# Exibindo a base de dados financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_ocorrencias.head())
print(df_cisp_roubo.head())

#Criando DataFrame Roubo de Veículos
df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]
#reset.index = ordem alfabetica ou crescente / groupby = agrupar
df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index() 
print('\n---- OBTENDO DADOS SOBRE ROUBOS DE VEÍCULOS ----')
print(df_roubo_veiculo.head())