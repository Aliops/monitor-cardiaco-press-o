import sqlite3
import pandas as pd


conn = sqlite3.connect('health_data.db')  

query = """
SELECT data_registro, pressao_sistolica, pressao_diastolica, batimentos_cardiacos
FROM dados_cardiacos
WHERE id_pessoa = ?  -- Substitua ? pelo ID específico da pessoa
ORDER BY data_registro;
"""
id_pessoa = 'ID_DA_PESSOA' 
df = pd.read_sql_query(query, conn, params=[id_pessoa])


conn.close()

df['hipertensao_subclinica'] = ((df['pressao_sistolica'] >= 120) & (df['pressao_sistolica'] < 140) |
                                (df['pressao_diastolica'] >= 80) & (df['pressao_diastolica'] < 89))

resumo = df.groupby('hipertensao_subclinica').size()

print("Resumo da Análise de Hipertensão Subclínica:")
print(resumo)
