# 🌐 Tech Inclusão

### Educação digital segura para inclusão digital e proteção de dados

Programa em modo console, desenvolvido em Python, que registra usuários fictícios em arquivos JSON e utiliza esses dados para gerar estatísticas.

**UNIP – Universidade Paulista**  
Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas  
Projeto Integrado Multidisciplinar – PIM I  
Campus São José dos Campos – SP

---

## 📖 Sobre o projeto

A Tech Inclusão é uma ONG fictícia de educação digital, criada como estudo de caso para o Projeto Integrado Multidisciplinar (PIM I). A proposta é promover o ensino de pensamento lógico, programação básica em Python e segurança digital para comunidades em situação de vulnerabilidade e estudantes de escolas públicas.

O projeto apresenta um protótipo em Python que permite cadastrar e consultar usuários fictícios, armazenar informações em arquivos JSON e realizar análises estatísticas.

Entre os conceitos aplicados estão:

- Utilização de listas e dicionários em Python;
- Leitura e gravação de arquivos JSON;
- Estruturas condicionais e de repetição;
- Validação de dados;
- Cálculos de estatística descritiva;
- Princípios de proteção de dados previstos na LGPD.

> **Observação:** todos os dados utilizados são fictícios e destinados exclusivamente à demonstração acadêmica.

---

## ✨ Funcionalidades

| Opção | Funcionalidade | Descrição |
|---|---|---|
| 1 | Cadastrar usuário | Solicita consentimento e registra os dados do usuário. |
| 2 | Listar usuários | Exibe os registros cadastrados no console. |
| 3 | Ver estatísticas | Apresenta medidas estatísticas e distribuição por faixa etária. |
| 0 | Sair | Encerra o programa. |

---

## 🚀 Como executar

### Requisitos

- Python 3.8 ou superior;
- Git instalado.

Não é necessário instalar bibliotecas adicionais, pois o programa utiliza recursos da biblioteca padrão do Python.

### Clonar o repositório

```bash
git clone https://github.com/michelydev/PIM-I_Michely_Archetti.git
cd PIM-I_Michely_Archetti
```

### Executar o programa

```bash
python tech_inclusao.py
```

No Linux ou macOS, pode ser necessário utilizar `python3` no lugar de `python`.

### Testar com dados de exemplo

O arquivo `usuarios_exemplo.json` contém 20 registros fictícios para testar as funcionalidades estatísticas.

Para utilizá-los, copie o arquivo com o nome `usuarios.json`.

**Windows:**

```cmd
copy usuarios_exemplo.json usuarios.json
```

**Linux ou macOS:**

```bash
cp usuarios_exemplo.json usuarios.json
```

Após a cópia, execute o programa e selecione a opção 3 para visualizar as estatísticas.

---

## 🖥️ Exemplo de uso

Exemplo da apresentação das estatísticas no console:

```text
=== TECH INCLUSÃO ===
1 - Cadastrar usuário
2 - Listar usuários
3 - Ver estatísticas
0 - Sair

Opção: 3
```

Os resultados apresentados incluem:

- Média, mediana e moda;
- Desvio padrão;
- Valores mínimo e máximo;
- Distribuição dos participantes por faixa etária.

---

## 🧠 Organização do programa

O programa utiliza listas e dicionários para organizar os registros dos usuários. Essas estruturas são armazenadas em arquivos JSON, permitindo que os dados sejam recuperados em execuções posteriores.

O módulo `json` é utilizado para converter os dados entre as estruturas do Python e o formato JSON.

### Principais funções

| Função | Descrição |
|---|---|
| `carregar()` | Carrega os registros armazenados no arquivo JSON. |
| `salvar()` | Salva os registros no arquivo JSON. |
| `cadastrar()` | Realiza o cadastro de um usuário. |
| `listar()` | Apresenta os usuários cadastrados. |
| `medidas()` | Calcula as medidas estatísticas. |
| `frequencia_por_faixa()` | Calcula a distribuição por faixa etária. |
| `estatisticas()` | Apresenta os resultados estatísticos. |
| `menu()` | Controla as opções do programa. |

---

## 🔐 Privacidade e proteção de dados

O projeto considera princípios da Lei Geral de Proteção de Dados Pessoais (LGPD), como:

- Solicitação de consentimento para o cadastro;
- Utilização de dados fictícios;
- Identificação dos registros por códigos;
- Armazenamento local das informações.

Por se tratar de um protótipo acadêmico, não foram implementados todos os mecanismos de segurança necessários para uma aplicação real.

---

## 📁 Estrutura do repositório

```text
PIM-I_Michely_Archetti/
│
├── tech_inclusao.py
├── usuarios_exemplo.json
└── README.md
```

- `tech_inclusao.py`: código-fonte do programa.
- `usuarios_exemplo.json`: registros fictícios utilizados nos testes.
- `README.md`: documentação do projeto.

---

## 👤 Autoria

Projeto desenvolvido individualmente por **Michely Archetti**, estudante do Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas da **UNIP (Universidade Paulista)**, campus de São José dos Campos (SP).
