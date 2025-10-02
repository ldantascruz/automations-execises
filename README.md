# 🤖 Automator - Repositório de Automações

Este repositório contém uma coleção de automações úteis para o dia a dia. Cada automação foi desenvolvida para resolver problemas específicos e pode ser facilmente reutilizada quando necessário.

## 📚 Automações Disponíveis

### 1. 📝 Gerador de Exercícios de Matemática (Estilo Kumon)

**Arquivos:** `gerador_kumon.py` e `app.py`

Uma automação completa para gerar exercícios de matemática no estilo Kumon, disponível em duas versões:

#### 🖥️ Versão Terminal (`gerador_kumon.py`)
- **Descrição:** Aplicação interativa de linha de comando que gera PDFs com exercícios de matemática
- **Funcionalidades:**
  - Gera exercícios de adição, subtração, multiplicação e divisão
  - Permite configurar a quantidade de dígitos para cada número
  - Gera múltiplas folhas de exercícios (1-20 folhas)
  - Inclui gabarito destacável em cada folha
  - Organiza arquivos em pastas por tipo de operação
  - Integração com impressora (macOS)
  - Interface interativa no terminal

#### 🌐 Versão Web (`app.py`)
- **Descrição:** Aplicação web Flask com interface moderna para gerar exercícios
- **Funcionalidades:**
  - Interface web responsiva e moderna (Tailwind CSS)
  - Mesmas operações matemáticas da versão terminal
  - Download direto do PDF pelo navegador
  - Acessível por qualquer dispositivo na rede local
  - Labels dinâmicos que se adaptam ao tipo de operação selecionada

#### ⚙️ Características Técnicas
- **Layout:** Formato A4 com 18 exercícios por folha (3 colunas x 6 linhas)
- **Gabarito:** Incluído em cada folha com linha de recorte
- **Validações:** Garante resultados positivos e divisões exatas
- **Organização:** Numeração sequencial e espaçamento adequado para resolução

### 2. 🧾 Gerador de Recibos de Prestação de Serviço

**Arquivo:** `gerar_recibo.py`

Uma automação completa para gerar recibos de prestação de serviços com formatação profissional, disponível em modo individual ou em lote.

#### 📋 Funcionalidades Principais
- **Geração Individual:** Cria recibos personalizados para clientes específicos
- **Geração em Lote:** Gera automaticamente recibos para todos os 4 clientes cadastrados
- **Geração Consolidada:** Cria um único recibo com todos os 4 clientes e valor total
- **Clientes Pré-cadastrados:** Base de dados com 4 clientes e seus respectivos valores
- **Prestador Padrão:** Configuração pré-definida do prestador de serviços
- **Numeração Sequencial:** Sistema automático de numeração de recibos
- **Múltiplos Formatos:** Exportação em TXT e PDF
- **Impressão Automática:** Integração com sistema de impressão (macOS)

#### 👥 Clientes Cadastrados
1. **Lucas Lago Borges** - CPF: 041.909.035-59 - R$ 1.578,71
2. **Tiago Martin Rodrigues** - CPF: 801.796.225-87 - R$ 701,65
3. **Daniel Lago Araujo** - CPF: 054.136.675-07 - R$ 701,65
4. **Paulo Roberto Aziz Yokoshiro** - CPF: 394.341.335-72 - R$ 526,24

#### ⚙️ Características Técnicas
- **Formato TXT:** Recibo em texto simples com formatação estruturada
- **Formato PDF:** Layout profissional usando ReportLab
- **Validação de Dados:** Verificação automática de CPF e valores
- **Organização:** Arquivos salvos em pasta dedicada com timestamp
- **Flexibilidade:** Permite personalização de todos os campos

## 🚀 Como Usar

### Pré-requisitos
```bash
# Instalar dependências
pip install -r requirements.txt
```

### Versão Terminal
```bash
# Executar o gerador interativo
python gerador_kumon.py
```

### Versão Web
```bash
# Iniciar servidor web
python app.py

# Acessar no navegador:
# http://localhost:5001
# ou
# http://[SEU_IP]:5001 (para acesso na rede local)
```

### Gerador de Recibos
```bash
# Executar o gerador de recibos
python gerar_recibo.py

# Opções disponíveis:
# 1 - Gerar recibo individual
# 2 - Gerar recibos em lote (todos os 4 clientes)
# 3 - Gerar recibo consolidado (todos os clientes em um único recibo)
```

## 📦 Dependências

- **Flask** (>=2.0): Framework web para a versão online
- **reportlab** (>=3.0): Geração de PDFs

## 🎯 Casos de Uso

### Gerador de Exercícios Kumon
- **Professores:** Criar rapidamente folhas de exercícios personalizadas
- **Pais:** Gerar atividades de reforço para crianças em casa
- **Escolas:** Produzir material didático padronizado
- **Tutores:** Criar exercícios específicos para diferentes níveis

### Gerador de Recibos
- **Prestadores de Serviço:** Gerar recibos profissionais rapidamente
- **Freelancers:** Documentar pagamentos de clientes recorrentes
- **Pequenas Empresas:** Automatizar emissão de recibos para clientes fixos
- **Contadores:** Auxiliar clientes na geração de comprovantes de renda
- **Consultores:** Documentar prestações de serviços de forma padronizada
- **Consultores:** Recibos consolidados para projetos com múltiplos participantes

## 📁 Estrutura do Projeto

```
Automator/
├── README.md              # Este arquivo
├── requirements.txt       # Dependências Python
├── gerador_kumon.py      # Versão terminal do gerador de exercícios
├── app.py                # Versão web do gerador de exercícios
├── gerar_recibo.py       # Gerador de recibos de prestação de serviço
└── .gitignore           # Arquivos ignorados pelo Git
```

## 🔄 Adicionando Novas Automações

Para adicionar uma nova automação ao repositório:

1. **Crie o arquivo da automação** com nome descritivo
2. **Documente no README.md** seguindo o padrão:
   - Nome e descrição da automação
   - Funcionalidades principais
   - Como usar
   - Casos de uso
3. **Adicione dependências** no `requirements.txt` se necessário
4. **Teste a automação** antes de commitar

## 📝 Padrão de Documentação

Cada nova automação deve incluir:
- **Descrição clara** do que faz
- **Lista de funcionalidades**
- **Instruções de uso**
- **Exemplos práticos**
- **Casos de uso reais**

## 🤝 Contribuições

Sinta-se à vontade para adicionar novas automações úteis seguindo o padrão estabelecido!