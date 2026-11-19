MINIMO = 11  # TROQUE pelo seu LIMITE


def senha_valida(senha):
    if not senha:
        return False
    return len(senha) >= MINIMO
