import pandas as pd

# Carregar dados
df = pd.read_csv("dados/compras.csv")

# Criar matriz usuário-produto
matriz = pd.crosstab(df['user_id'], df['product_name'])

# Calcular a similaridade entre os produtos
similaridade = matriz.T.dot(matriz)

# Função de recomendação
def recomendar_produtos(usuario_id, top_n=5):
    if usuario_id not in matriz.index:
        return "Usuário não encontrado."
    
    compras_usuario = matriz.loc[usuario_id]
    produtos_comprados = compras_usuario[compras_usuario > 0].index.tolist()
    
    recomendacoes = pd.Series(dtype=float)

    for produto in produtos_comprados:
        recomendacoes = recomendacoes.add(similaridade[produto], fill_value=0)

    for produto in produtos_comprados:
        if produto in recomendacoes:
            recomendacoes.drop(produto, inplace=True)

    return recomendacoes.sort_values(ascending=False).head(top_n).index.tolist()
