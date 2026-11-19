from senha import senha_valida, MINIMO


def test_senha_com_limite_caracteres_e_aceita():
    # Arrange
    senha = "a" * MINIMO

    # Act
    resultado = senha_valida(senha)

    # Assert
    assert resultado is True


def test_senha_com_menos_de_limite_e_rejeitada():
    # Arrange
    senha = "a" * (MINIMO - 1)

    # Act
    resultado = senha_valida(senha)

    # Assert
    assert resultado is False


def test_senha_vazia_e_rejeitada():
    # Arrange
    senha = ""

    # Act
    resultado = senha_valida(senha)

    # Assert
    assert resultado is False
