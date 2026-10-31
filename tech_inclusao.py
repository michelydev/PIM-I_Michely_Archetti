"""Tech Inclusão - programa em modo console (PIM I - ADS / UNIP).

Cadastra usuários fictícios de uma plataforma de educação digital,
salva os dados em disco no formato JSON e calcula estatísticas básicas.

Estruturas de dados utilizadas:
  - dicionário (dict): representa um usuário (chave -> valor);
  - lista (list): reúne todos os usuários cadastrados.

Uso: python tech_inclusao.py
"""
import json
import statistics
from pathlib import Path

ARQUIVO = Path("usuarios.json")

FAIXAS = [
    ("< 18", 0, 17),
    ("18-25", 18, 25),
    ("26-35", 26, 35),
    ("36-45", 36, 45),
    ("46+", 46, 200),
]


def carregar(arquivo=ARQUIVO):
    """Lê o arquivo JSON e devolve uma lista de dicionários."""
    if not Path(arquivo).exists():
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar(usuarios, arquivo=ARQUIVO):
    """Grava a lista de dicionários no arquivo JSON."""
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=2)


def ler_inteiro(mensagem, minimo, maximo):
    """Pede um número inteiro ao usuário até receber um valor válido."""
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"Digite um valor entre {minimo} e {maximo}.")


def cadastrar(usuarios):
    """Cadastra um usuário. Só coleta dados com consentimento (LGPD)."""
    resposta = input("O participante autoriza o uso dos dados para fins "
                     "educacionais e estatísticos? (s/n): ").strip().lower()
    if resposta != "s":
        print("Cadastro cancelado: sem consentimento não há coleta de dados.")
        return
    usuario = {
        "id": f"U{len(usuarios) + 1:03d}",  # identificador, sem nome real
        "idade": ler_inteiro("Idade: ", 5, 120),
        "acessos_mes": ler_inteiro("Acessos no mês: ", 0, 500),
        "tempo_medio_min": ler_inteiro("Tempo médio por acesso (min): ", 0, 600),
        "modulos_concluidos": ler_inteiro("Módulos concluídos (0 a 3): ", 0, 3),
        "consentimento": True,
    }
    usuarios.append(usuario)
    salvar(usuarios)
    print(f"Usuário {usuario['id']} cadastrado.")


def listar(usuarios):
    """Mostra todos os usuários da lista."""
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print(f"{'ID':<6}{'Idade':>6}{'Acessos':>9}{'Tempo':>7}{'Módulos':>9}")
    for u in usuarios:
        print(f"{u['id']:<6}{u['idade']:>6}{u['acessos_mes']:>9}"
              f"{u['tempo_medio_min']:>7}{u['modulos_concluidos']:>9}")


def medidas(valores):
    """Devolve um dicionário com as medidas descritivas de uma lista."""
    return {
        "media": statistics.mean(valores),
        "mediana": statistics.median(valores),
        "moda": statistics.multimode(valores),
        "desvio_padrao": statistics.stdev(valores),  # amostral
        "minimo": min(valores),
        "maximo": max(valores),
    }


def frequencia_por_faixa(usuarios):
    """Conta quantos usuários há em cada faixa etária."""
    contagem = {nome: 0 for nome, _, _ in FAIXAS}
    for u in usuarios:
        for nome, minimo, maximo in FAIXAS:
            if minimo <= u["idade"] <= maximo:
                contagem[nome] += 1
    return contagem


def estatisticas(usuarios):
    """Imprime o relatório estatístico (exige ao menos 2 usuários)."""
    if len(usuarios) < 2:
        print("São necessários ao menos 2 usuários para calcular estatísticas.")
        return
    campos = [("idade", "Idade (anos)"),
              ("acessos_mes", "Acessos no mês"),
              ("tempo_medio_min", "Tempo médio (min)")]
    for chave, titulo in campos:
        m = medidas([u[chave] for u in usuarios])
        moda = ", ".join(str(x) for x in m["moda"])
        print(f"\n{titulo}")
        print(f"  média={m['media']:.2f}  mediana={m['mediana']:.2f}  "
              f"moda={moda}  desvio padrão={m['desvio_padrao']:.2f}  "
              f"mín={m['minimo']}  máx={m['maximo']}")
    print("\nParticipantes por faixa etária:")
    total = len(usuarios)
    for faixa, qtd in frequencia_por_faixa(usuarios).items():
        print(f"  {faixa:<6} {qtd:>3}  ({100 * qtd / total:.1f}%)")


def menu():
    usuarios = carregar()
    opcoes = {"1": ("Cadastrar usuário", cadastrar),
              "2": ("Listar usuários", listar),
              "3": ("Ver estatísticas", estatisticas)}
    while True:
        print("\n=== TECH INCLUSÃO ===")
        for numero, (texto, _) in opcoes.items():
            print(f"{numero} - {texto}")
        print("0 - Sair")
        escolha = input("Opção: ").strip()
        if escolha == "0":
            print("Até logo!")
            break
        if escolha in opcoes:
            opcoes[escolha][1](usuarios)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
