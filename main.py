from recomendador import recomendar_produtos

if __name__ == "__main__":
    usuario_id = 1020
    recomendacoes = recomendar_produtos(usuario_id)
    print(f"Recomendações para o usuário {usuario_id}:")
    print(recomendacoes)
