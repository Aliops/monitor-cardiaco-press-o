import sqlite3
import random
import time


conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()


c.execute('''
CREATE TABLE IF NOT EXISTS health_monitoring (
    timestamp DATETIME,
    blood_pressure_systolic INTEGER,
    blood_pressure_diastolic INTEGER,
    heart_rate INTEGER
)
''')


def generate_and_insert_data():
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    blood_pressure_systolic = random.randint(100, 140)  # Valores de exemplo
    blood_pressure_diastolic = random.randint(60, 90)  # Valores de exemplo
    heart_rate = random.randint(60, 100)  # Valores de exemplo
    
    c.execute('''
    INSERT INTO health_monitoring (timestamp, blood_pressure_systolic, blood_pressure_diastolic, heart_rate)
    VALUES (?, ?, ?, ?)
    ''', (timestamp, blood_pressure_systolic, blood_pressure_diastolic, heart_rate))
    
    conn.commit()


try:
    while True:
        generate_and_insert_data()
        print("Dados inseridos no banco de dados.")
        time.sleep(10)  # Pausa de 10 segundos antes de gerar mais dados
except KeyboardInterrupt:
    print("Programa interrompido.")

conn.close()
