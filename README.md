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

## 📦 Dependências

- **Flask** (>=2.0): Framework web para a versão online
- **reportlab** (>=3.0): Geração de PDFs

## 🎯 Casos de Uso

### Gerador de Exercícios Kumon
- **Professores:** Criar rapidamente folhas de exercícios personalizadas
- **Pais:** Gerar atividades de reforço para crianças em casa
- **Escolas:** Produzir material didático padronizado
- **Tutores:** Criar exercícios específicos para diferentes níveis

## 📁 Estrutura do Projeto

```
Automator/
├── README.md              # Este arquivo
├── requirements.txt       # Dependências Python
├── gerador_kumon.py      # Versão terminal do gerador
├── app.py                # Versão web do gerador
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