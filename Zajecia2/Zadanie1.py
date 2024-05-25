import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect('census.sqlite')
cursor = conn.cursor()

# 1. Nazwy stanów występujące w bazie
cursor.execute("SELECT DISTINCT state FROM census")
states = cursor.fetchall()

# Wyświetlenie wyników
print("Nazwy stanów występujące w bazie:")
for state in states:
    print(state[0])

print("\n")

# 2. Populacja w stanie Alaska oraz New York w 2000 oraz 2008 roku
cursor.execute("""
    SELECT state, year, population 
    FROM census 
    WHERE state IN ('Alaska', 'New York') AND year IN (2000, 2008)
""")
population_data = cursor.fetchall()

# Wyświetlenie wyników
print("Populacja w stanie Alaska oraz New York w 2000 oraz 2008 roku:")
for record in population_data:
    print(f"Stan: {record[0]}, Rok: {record[1]}, Populacja: {record[2]}")

print("\n")

# 3. Liczba kobiet oraz mężczyzn w stanie New York w 2008 roku
cursor.execute("""
    SELECT sex, SUM(population) 
    FROM census 
    WHERE state='New York' AND year=2008 
    GROUP BY sex
""")
ny_gender_population = cursor.fetchall()

# Wyświetlenie wyników
print("Liczba kobiet oraz mężczyzn w stanie New York w 2008 roku:")
for record in ny_gender_population:
    print(f"Płeć: {record[0]}, Populacja: {record[1]}")

# Zamknięcie połączenia
conn.close()
