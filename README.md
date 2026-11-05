# 🌐 Tech Inclusão
### Educação digital segura para inclusão digital e proteção de dados

Programa em modo console, desenvolvido em Python, que registra usuários fictícios em arquivos JSON e utiliza os dados para gerar estatísticas.

**UNIP – Universidade Paulista**  
Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas  
Projeto Integrado Multidisciplinar – PIM I  
Campus São José dos Campos – SP

---

## 📖 Sobre o projeto

A Tech Inclusão é uma ONG fictícia de educação digital, criada como estudo de caso para o Projeto Integrado Multidisciplinar (PIM I). A proposta é promover o ensino de pensamento lógico, programação básica em Python e segurança digital para comunidades em situação de vulnerabilidade e estudantes de escolas públicas.

Este repositório contém o protótipo desenvolvido para representar algumas das funcionalidades da proposta. O programa demonstra como:

- Representar os dados de um usuário por meio de um dicionário (`dict`);
- Organizar os registros em uma lista (`list`);
- Armazenar os dados em arquivos no formato JSON;
- Realizar cálculos de estatística descritiva;
- Considerar o consentimento e os princípios de proteção de dados previstos na LGPD.

> **Aviso:** todos os dados utilizados no projeto são fictícios. Nenhuma informação de pessoas reais foi coletada. O programa é um protótipo acadêmico e não deve ser utilizado para armazenar dados reais sem a implementação de medidas adicionais de segurança.

---

## ✨ Funcionalidades

| Opção | Funcionalidade | Descrição |
|---|---|---|
| 1 | Cadastrar usuário | Solicita consentimento e registra idade, acessos, tempo de uso e módulos concluídos. |
| 2 | Listar usuários | Exibe os registros cadastrados em uma tabela no console. |
| 3 | Ver estatísticas | Calcula média, mediana, moda, desvio padrão, mínimo e máximo, além da distribuição por faixa etária. |
| 0 | Sair | Encerra a execução do programa. |

---

## 🚀 Como executar

### Requisitos

- Python 3.8 ou superior;
- Git instalado para clonar o repositório.

Não é necessário instalar bibliotecas adicionais, pois o programa utiliza recursos da biblioteca padrão do Python.

### Clonagem do repositório

Abra o terminal e execute os comandos:

```bash
git clone https://github.com/michelydev/PIM-I_Michely_Archetti.git
cd PIM-I_Michely_Archetti
```

### Execução do programa

```bash
python tech_inclusao.py
```

No Linux ou macOS, pode ser necessário utilizar `python3` no lugar de `python`.

### 🧪 Teste com dados de exemplo

O arquivo `usuarios_exemplo.json` contém 20 registros fictícios para testar o funcionamento das estatísticas.

Para utilizar esses registros, copie o arquivo de exemplo com o nome `usuarios.json`.

**Linux / macOS:**

```bash
cp usuarios_exemplo.json usuarios.json
```

**Windows (Prompt de Comando):**

```cmd
copy usuarios_exemplo.json usuarios.json
```

Depois, execute o programa e selecione a opção 3 para visualizar os resultados estatísticos.

---

## 🖥️ Exemplo de uso

Abaixo está uma representação da saída apresentada pelo programa ao selecionar a opção de estatísticas:

```text
=== TECH INCLUSÃO ===
1 - Cadastrar usuário
2 - Listar usuários
3 - Ver estatísticas
0 - Sair

Opção: 3

Idade (anos)
  média=30.10  mediana=27.00  moda=27
  desvio padrão=12.19  mín=15  máx=61

Acessos no mês
  média=15.40  mediana=16.50
  moda=18, 15, 17, 19
  desvio padrão=5.21  mín=5  máx=24

Tempo médio (min)
  média=31.15  mediana=31.50
  moda=30, 35
  desvio padrão=5.89  mín=20  máx=41

Participantes por faixa etária:
  < 18     2  (10.0%)
  18-25    6  (30.0%)
  26-35    7  (35.0%)
  36-45    3  (15.0%)
  46+      2  (10.0%)
```

---

## 🧠 Como funciona

### Fluxo do programa

O funcionamento do programa segue as etapas representadas no fluxograma:

```mermaid
flowchart TD
    A([Início]) --> B[Carrega usuarios.json
