import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('health_data.db')  # Substitua 'health_data.db' pelo caminho do seu banco de dados real

# Consultar dados cardíacos de uma pessoa específica
query = """
SELECT data_registro, pressao_sistolica, pressao_diastolica, batimentos_cardiacos
FROM dados_cardiacos
WHERE id_pessoa = ?  -- Substitua ? pelo ID específico da pessoa
ORDER BY data_registro;
"""
id_pessoa = 'ID_DA_PESSOA'  # Substitua 'ID_DA_PESSOA' pelo ID real da pessoa
df = pd.read_sql_query(query, conn, params=[id_pessoa])

# Fechar conexão com o banco de dados
conn.close()

# Análise de Dados para Hipertensão Arterial Subclínica
# Definir limites para hipertensão subclínica: pressão sistólica entre 120-139 ou diastólica entre 80-89 em várias medições
df['hipertensao_subclinica'] = ((df['pressao_sistolica'] >= 120) & (df['pressao_sistolica'] < 140) |
                                (df['pressao_diastolica'] >= 80) & (df['pressao_diastolica'] < 89))

# Resumindo os resultados
resumo = df.groupby('hipertensao_subclinica').size()

print("Resumo da Análise de Hipertensão Subclínica:")
print(resumo)
