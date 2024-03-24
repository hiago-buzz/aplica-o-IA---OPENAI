import tiktoken


def codificar(modelo, mensagem):
    codigicador = tiktoken.encoding_for_model(modelo)
    lista_tokens = codigicador.encode(mensagem)

    referencia = 1000
    custo_base = {
        "gpt-4":0.03,
        "gpt-3.5-turbo-1106": 0.001
    }

    print(f"Lista de Tokens: {lista_tokens}")
    print(f"Quantos tokens temos: {len(lista_tokens)}")
    print(f"Custo para o {modelo} é de ${len(lista_tokens)/referencia * custo_base[modelo]}")


mensagem="São Paulo, maior campeão do Brasil!"

codificar(mensagem=mensagem, modelo="gpt-4")
codificar(mensagem=mensagem, modelo="gpt-3.5-turbo-1106")