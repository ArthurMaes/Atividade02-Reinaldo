import pandas as pd

# 1. Ler o arquivo CSV
df = pd.read_csv("Jogadores.csv", sep=";")

# -------------------------
# CONSULTA 1
# Jogadores com salário acima de R$ 20.000,00
# -------------------------
print("\n1) Jogadores com salário acima de R$ 20.000,00:")
print(df[df["salario_do_jogador"] > 20000][["nome_do_jogador", "nome_time_jogador"]])


# -------------------------
# CONSULTA 2
# Nome e salário dos jogadores dos times de Minas Gerais
# -------------------------
print("\n2) Jogadores de Minas Gerais:")
print(df[df["nome_estado_jogador"] == "MG"][["nome_do_jogador", "salario_do_jogador"]])


# -------------------------
# CONSULTA 3
# Jogadores cujo nome contém a letra 'u'
# -------------------------
print("\n3) Jogadores cujo nome contém a letra 'u':")
print(df[df["nome_do_jogador"].str.contains("u", case=False, na=False)][["nome_do_jogador", "nome_time_jogador"]])


# -------------------------
# CONSULTA 4
# Jogadores ordenados pelo salário (decrescente)
# -------------------------
print("\n4) Ordenados por salário (decrescente):")
print(df.sort_values(by="salario_do_jogador", ascending=False)[["nome_do_jogador", "salario_do_jogador", "nome_time_jogador"]])


# -------------------------
# CONSULTA 5
# Ordenados pelo nome do time (crescente) e pelo salário (decrescente)
# -------------------------
print("\n5) Ordenados por time e salário:")
print(df.sort_values(by=["nome_time_jogador", "salario_do_jogador"], ascending=[True, False])[["nome_do_jogador", "salario_do_jogador", "nome_time_jogador"]])


# -------------------------
# CONSULTA 6
# Quantidade de jogadores por time
# -------------------------
print("\n6) Quantidade de jogadores por time:")
print(df.groupby("nome_time_jogador")["nome_do_jogador"].count())


# -------------------------
# CONSULTA 7
# Média salarial por time
# -------------------------
print("\n7) Média salarial por time:")
print(df.groupby("nome_time_jogador")["salario_do_jogador"].mean())
