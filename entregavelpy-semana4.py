
# ENTREGÁVEL DE DESENVOLVIMENTO EM PYTHON - SEMANA 04 (SPRINT 4)
produtos = []

print("=== CADASTRO DE PRODUTOS ===")
quantidade_produtos = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade_produtos):
    print(f"\nProduto {i + 1}:")
    nome = input("Digite o nome do produto: ").strip()
    preco = float(input("Digite o preço do produto (R$): "))
    categoria = input("Digite a categoria do produto: ").strip().capitalize()
    

    produto = {
        "nome": nome,
        "preco": preco,
        "categoria": categoria
    }
    produtos.append(produto)



print("\n" + "=" * 40)
print("=== FILTRAGEM POR PREÇO ===")
valor_corte = float(input("Informe o valor limite para filtragem (R$): "))

produtos_acima = [p for p in produtos if p["preco"] > valor_corte]
produtos_abaixo = [p for p in produtos if p["preco"] <= valor_corte]

print(f"\nProdutos com preço ACIMA de R$ {valor_corte:.2f}:")
for p in produtos_acima:
    print(f" - {p['nome']} (R$ {p['preco']:.2f})")

print(f"\nProdutos com preço ABAIXO ou IGUAL a R$ {valor_corte:.2f}:")
for p in produtos_abaixo:
    print(f" - {p['nome']} (R$ {p['preco']:.2f})")



print("\n" + "=" * 40)
print("=== ORDENAÇÃO DE PRODUTOS ===")


produtos_decrescente = sorted(produtos, key=lambda p: p["preco"], reverse=True)


produtos.sort(key=lambda p: p["preco"])



categorias_unicas = set(p["categoria"] for p in produtos)

precos = [p["preco"] for p in produtos]

menor_preco = min(precos)
maior_preco = max(precos)
media_preco = sum(precos) / len(precos)


estatisticas = (menor_preco, maior_preco, media_preco)


print("\n" + "=" * 40)
print("=== RELATÓRIO FINAL DO SISTEMA DE PRODUTOS ===")

print("\n[1] Lista de Produtos Ordenados por Preço (Crescente - sort()):")
for p in produtos:
    print(f"  • {p['nome']:<20} | Categoria: {p['categoria']:<15} | Preço: R$ {p['preco']:>8.2f}")

print("\n[2] Lista de Produtos Ordenados por Preço (Decrescente - sorted()):")
for p in produtos_decrescente:
    print(f"  • {p['nome']:<20} | Preço: R$ {p['preco']:>8.2f}")

print("\n[3] Categorias Únicas Cadastradas (set):")
print(f"  • Categorias: {', '.join(categorias_unicas)}")

print("\n[4] Tupla de Estatísticas de Preços:")
print(f"  • Menor Preço : R$ {estatisticas[0]:.2f}")
print(f"  • Maior Preço : R$ {estatisticas[1]:.2f}")
print(f"  • Média Preços: R$ {estatisticas[2]:.2f}")

print("=" * 40)