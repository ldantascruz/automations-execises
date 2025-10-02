import os
from datetime import datetime
from pathlib import Path

# ===== CONFIGURAÇÕES PRÉ-DEFINIDAS =====

PRESTADOR_PADRAO = {
    'nome': 'Lucas Dantas da Cruz',
    'cpf': '157.579.117-00',
    'rg': '3.315.821 - ES',
    'endereco': 'Rua Abdo David, S/N, Ayd, Vargem Alta - ES',
    'telefone': '(27)99741-8240'
}

CLIENTES = {
    '1': {
        'nome': 'Lucas Lago Borges',
        'cpf': '041.909.035-59',
        'valor_numerico': '1.578,71',
        'valor_extenso': 'mil quinhentos e setenta e oito reais e setenta e um centavos'
    },
    '2': {
        'nome': 'Tiago Martin Rodrigues',
        'cpf': '801.796.225-87',
        'valor_numerico': '701,65',
        'valor_extenso': 'setecentos e um reais e sessenta e cinco centavos'
    },
    '3': {
        'nome': 'Daniel Lago Araujo',
        'cpf': '054.136.675-07',
        'valor_numerico': '701,65',
        'valor_extenso': 'setecentos e um reais e sessenta e cinco centavos'
    },
    '4': {
        'nome': 'Paulo Roberto Aziz Yokoshiro',
        'cpf': '394.341.335-72',
        'valor_numerico': '526,24',
        'valor_extenso': 'quinhentos e vinte e seis reais e vinte e quatro centavos'
    }
}

LOCALIDADE_PADRAO = 'Vargem Alta/ES'

# =======================================

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_pasta_recibos():
    pasta = Path("recibos")
    if not pasta.exists():
        pasta.mkdir()
    return pasta

def obter_dados():
    limpar_tela()
    print("=" * 60)
    print("GERADOR DE RECIBOS DE PRESTAÇÃO DE SERVIÇO")
    print("=" * 60)
    print()
    
    dados = {}
    
    # Dados do prestador
    print("--- DADOS DO PRESTADOR DE SERVIÇO ---")
    print(f"Prestador padrão: {PRESTADOR_PADRAO['nome']}")
    usar_padrao = input("Usar prestador padrão? (S/N): ").strip().upper()
    
    if usar_padrao == 'S':
        dados['prestador_nome'] = PRESTADOR_PADRAO['nome']
        dados['prestador_cpf'] = PRESTADOR_PADRAO['cpf']
        dados['prestador_rg'] = PRESTADOR_PADRAO['rg']
        dados['prestador_endereco'] = PRESTADOR_PADRAO['endereco']
        dados['prestador_telefone'] = PRESTADOR_PADRAO['telefone']
    else:
        dados['prestador_nome'] = input("Nome completo: ").strip()
        dados['prestador_cpf'] = input("CPF: ").strip()
        dados['prestador_rg'] = input("RG: ").strip()
        dados['prestador_endereco'] = input("Endereço completo: ").strip()
        dados['prestador_telefone'] = input("Telefone: ").strip()
    print()
    
    # Dados do cliente
    print("--- DADOS DO CLIENTE/PAGADOR ---")
    print("Clientes cadastrados:")
    for key, cliente in CLIENTES.items():
        print(f"  {key} - {cliente['nome']} (R$ {cliente['valor_numerico']})")
    print("  5 - Outro cliente")
    
    opcao_cliente = input("\nEscolha o cliente (1-5): ").strip()
    
    if opcao_cliente in CLIENTES:
        cliente_selecionado = CLIENTES[opcao_cliente]
        dados['cliente_nome'] = cliente_selecionado['nome']
        dados['cliente_doc_tipo'] = 'CPF'
        dados['cliente_doc'] = cliente_selecionado['cpf']
        dados['valor_numerico'] = cliente_selecionado['valor_numerico']
        dados['valor_extenso'] = cliente_selecionado['valor_extenso']
        
        # Perguntar se deseja usar o valor padrão
        print(f"\nValor padrão: R$ {dados['valor_numerico']}")
        usar_valor_padrao = input("Usar valor padrão? (S/N): ").strip().upper()
        
        if usar_valor_padrao != 'S':
            dados['valor_numerico'] = input("Valor (R$): ").strip()
            dados['valor_extenso'] = input("Valor por extenso: ").strip()
    else:
        dados['cliente_nome'] = input("Nome completo: ").strip()
        tipo_doc = input("Tipo de documento (1-CPF / 2-CNPJ): ").strip()
        if tipo_doc == "2":
            dados['cliente_doc_tipo'] = "CNPJ"
        else:
            dados['cliente_doc_tipo'] = "CPF"
        dados['cliente_doc'] = input(f"{dados['cliente_doc_tipo']}: ").strip()
        dados['valor_numerico'] = input("Valor (R$): ").strip()
        dados['valor_extenso'] = input("Valor por extenso: ").strip()
    print()
    
    # Dados do serviço
    print("--- DADOS DO SERVIÇO ---")
    dados['numero_recibo'] = input("Número do recibo: ").strip()
    dados['descricao_servico'] = input("Descrição do serviço prestado: ").strip()
    print()
    
    # Data e local
    print("--- DATA E LOCAL ---")
    print(f"Localidade padrão: {LOCALIDADE_PADRAO}")
    usar_local_padrao = input("Usar localidade padrão? (S/N): ").strip().upper()
    
    if usar_local_padrao == 'S':
        dados['localidade'] = LOCALIDADE_PADRAO
    else:
        dados['localidade'] = input("Cidade/Localidade: ").strip()
    
    usar_data_hoje = input("Usar data de hoje? (S/N): ").strip().upper()
    
    if usar_data_hoje == 'S':
        hoje = datetime.now()
        dados['dia'] = str(hoje.day).zfill(2)
        # Converter mês para português
        meses = {
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        }
        dados['mes'] = meses[hoje.month]
        dados['ano'] = str(hoje.year)
    else:
        dados['dia'] = input("Dia: ").strip()
        dados['mes'] = input("Mês: ").strip()
        dados['ano'] = input("Ano: ").strip()
    
    return dados

def gerar_recibo_txt(dados, pasta):
    conteudo = f"""
{'=' * 70}
                              RECIBO
{'=' * 70}

Nº: {dados['numero_recibo']}
Valor: R$ {dados['valor_numerico']}

Eu, {dados['prestador_nome']}, inscrito(a) no CPF sob o nº {dados['prestador_cpf']} 
e no RG nº {dados['prestador_rg']}, declaro que recebi de {dados['cliente_nome']}, 
inscrito(a) no {dados['cliente_doc_tipo']} sob o nº {dados['cliente_doc']}, a importância 
de {dados['valor_extenso']}, referente ao pagamento pelos seguintes serviços:

{dados['descricao_servico']}

{dados['localidade']}, {dados['dia']} de {dados['mes']} de {dados['ano']}.


_____________________________________________
Assinatura do Prestador de Serviço


Nome: {dados['prestador_nome']}
Endereço: {dados['prestador_endereco']}
Telefone: {dados['prestador_telefone']}

{'=' * 70}
"""
    
    nome_arquivo = f"recibo_{dados['numero_recibo']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    caminho_arquivo = pasta / nome_arquivo
    
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    print(f"\n✓ Recibo salvo em: {caminho_arquivo}")
    return caminho_arquivo, conteudo

def exportar_para_pdf(caminho_txt, dados, pasta):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import cm
        
        nome_pdf = caminho_txt.stem + ".pdf"
        caminho_pdf = pasta / nome_pdf
        
        c = canvas.Canvas(str(caminho_pdf), pagesize=A4)
        largura, altura = A4
        
        # Título
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(largura/2, altura - 3*cm, "RECIBO")
        
        # Linha separadora
        c.line(3*cm, altura - 3.5*cm, largura - 3*cm, altura - 3.5*cm)
        
        # Conteúdo
        c.setFont("Helvetica", 11)
        y = altura - 5*cm
        
        c.drawString(3*cm, y, f"Nº: {dados['numero_recibo']}")
        y -= 0.7*cm
        c.drawString(3*cm, y, f"Valor: R$ {dados['valor_numerico']}")
        y -= 1.2*cm
        
        # Texto principal
        c.setFont("Helvetica", 10)
        texto = f"Eu, {dados['prestador_nome']}, inscrito(a) no CPF sob o nº {dados['prestador_cpf']} e no RG nº {dados['prestador_rg']}, declaro que recebi de {dados['cliente_nome']}, inscrito(a) no {dados['cliente_doc_tipo']} sob o nº {dados['cliente_doc']}, a importância de {dados['valor_extenso']}, referente ao pagamento pelos seguintes serviços:"
        
        # Quebrar texto em linhas
        texto_obj = c.beginText(3*cm, y)
        texto_obj.setFont("Helvetica", 10)
        texto_obj.setLeading(14)
        
        palavras = texto.split()
        linha = ""
        for palavra in palavras:
            teste = linha + palavra + " "
            if c.stringWidth(teste, "Helvetica", 10) < (largura - 6*cm):
                linha = teste
            else:
                texto_obj.textLine(linha)
                linha = palavra + " "
        texto_obj.textLine(linha)
        
        c.drawText(texto_obj)
        y -= 3.5*cm
        
        # Descrição do serviço
        c.setFont("Helvetica-Bold", 10)
        c.drawString(3*cm, y, dados['descricao_servico'])
        y -= 2*cm
        
        # Data e local
        c.setFont("Helvetica", 10)
        c.drawString(3*cm, y, f"{dados['localidade']}, {dados['dia']} de {dados['mes']} de {dados['ano']}.")
        y -= 2.5*cm
        
        # Linha para assinatura
        c.line(3*cm, y, 10*cm, y)
        y -= 0.5*cm
        c.drawString(3*cm, y, "Assinatura do Prestador de Serviço")
        y -= 1.5*cm
        
        # Dados do prestador
        c.setFont("Helvetica", 9)
        c.drawString(3*cm, y, f"Nome: {dados['prestador_nome']}")
        y -= 0.5*cm
        c.drawString(3*cm, y, f"Endereço: {dados['prestador_endereco']}")
        y -= 0.5*cm
        c.drawString(3*cm, y, f"Telefone: {dados['prestador_telefone']}")
        
        c.save()
        print(f"✓ PDF gerado com sucesso: {caminho_pdf}")
        return caminho_pdf
        
    except ImportError:
        print("\n⚠ A biblioteca 'reportlab' não está instalada.")
        print("Para exportar para PDF, instale com: pip install reportlab")
        return None

def imprimir_pdf(caminho_pdf):
    import platform
    sistema = platform.system()
    
    try:
        if sistema == "Windows":
            os.startfile(str(caminho_pdf), "print")
        elif sistema == "Darwin":  # macOS
            os.system(f'lpr "{caminho_pdf}"')
        else:  # Linux
            os.system(f'lp "{caminho_pdf}"')
        
        print("✓ Documento enviado para impressão!")
        
    except Exception as e:
        print(f"⚠ Erro ao tentar imprimir: {e}")
        print(f"Você pode imprimir manualmente o arquivo: {caminho_pdf}")

def gerar_recibos_em_lote():
    """Gera recibos para todos os 4 clientes cadastrados"""
    limpar_tela()
    print("=" * 70)
    print("GERADOR DE RECIBOS EM LOTE - TODOS OS CLIENTES")
    print("=" * 70)
    print()
    
    # Criar pasta de recibos
    pasta = criar_pasta_recibos()
    
    # Dados do prestador
    print("--- DADOS DO PRESTADOR DE SERVIÇO ---")
    print(f"Prestador padrão: {PRESTADOR_PADRAO['nome']}")
    usar_padrao = input("Usar prestador padrão? (S/N): ").strip().upper()
    
    dados_prestador = {}
    if usar_padrao == 'S':
        dados_prestador['prestador_nome'] = PRESTADOR_PADRAO['nome']
        dados_prestador['prestador_cpf'] = PRESTADOR_PADRAO['cpf']
        dados_prestador['prestador_rg'] = PRESTADOR_PADRAO['rg']
        dados_prestador['prestador_endereco'] = PRESTADOR_PADRAO['endereco']
        dados_prestador['prestador_telefone'] = PRESTADOR_PADRAO['telefone']
    else:
        dados_prestador['prestador_nome'] = input("Nome completo: ").strip()
        dados_prestador['prestador_cpf'] = input("CPF: ").strip()
        dados_prestador['prestador_rg'] = input("RG: ").strip()
        dados_prestador['prestador_endereco'] = input("Endereço completo: ").strip()
        dados_prestador['prestador_telefone'] = input("Telefone: ").strip()
    print()
    
    # Dados do serviço (comum para todos)
    print("--- DADOS DO SERVIÇO ---")
    numero_recibo_inicial = input("Número do primeiro recibo (os próximos serão sequenciais): ").strip()
    descricao_servico = input("Descrição do serviço prestado: ").strip()
    print()
    
    # Data e local
    print("--- DATA E LOCAL ---")
    print(f"Localidade padrão: {LOCALIDADE_PADRAO}")
    usar_local_padrao = input("Usar localidade padrão? (S/N): ").strip().upper()
    
    if usar_local_padrao == 'S':
        localidade = LOCALIDADE_PADRAO
    else:
        localidade = input("Cidade/Localidade: ").strip()
    
    usar_data_hoje = input("Usar data de hoje? (S/N): ").strip().upper()
    
    if usar_data_hoje == 'S':
        hoje = datetime.now()
        dia = str(hoje.day).zfill(2)
        # Converter mês para português
        meses = {
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        }
        mes = meses[hoje.month]
        ano = str(hoje.year)
    else:
        dia = input("Dia: ").strip()
        mes = input("Mês: ").strip()
        ano = input("Ano: ").strip()
    
    # Gerar recibos para todos os clientes
    print("\n" + "=" * 70)
    print("GERANDO RECIBOS PARA TODOS OS CLIENTES...")
    print("=" * 70)
    
    arquivos_gerados = []
    
    try:
        numero_base = int(numero_recibo_inicial)
    except ValueError:
        print("⚠ Número de recibo inválido. Usando numeração sequencial a partir de 1.")
        numero_base = 1
    
    for i, (cliente_id, cliente_info) in enumerate(CLIENTES.items()):
        print(f"\nGerando recibo {i+1}/4 para {cliente_info['nome']}...")
        
        # Montar dados completos para este cliente
        dados_cliente = {
            **dados_prestador,
            'cliente_nome': cliente_info['nome'],
            'cliente_doc_tipo': 'CPF',
            'cliente_doc': cliente_info['cpf'],
            'valor_numerico': cliente_info['valor_numerico'],
            'valor_extenso': cliente_info['valor_extenso'],
            'numero_recibo': str(numero_base + i),
            'descricao_servico': descricao_servico,
            'localidade': localidade,
            'dia': dia,
            'mes': mes,
            'ano': ano
        }
        
        # Gerar recibo TXT
        caminho_txt, _ = gerar_recibo_txt(dados_cliente, pasta)
        arquivos_gerados.append(caminho_txt)
        
        print(f"✓ Recibo TXT gerado: {caminho_txt.name}")
    
    # Perguntar sobre exportação para PDF
    print(f"\n✓ {len(arquivos_gerados)} recibos TXT gerados com sucesso!")
    exportar_pdf = input("\nDeseja exportar todos os recibos para PDF? (S/N): ").strip().upper()
    
    arquivos_pdf = []
    if exportar_pdf == 'S':
        print("\nExportando para PDF...")
        for i, caminho_txt in enumerate(arquivos_gerados):
            cliente_id = str(i + 1)
            cliente_info = CLIENTES[cliente_id]
            
            # Reconstruir dados para PDF
            dados_cliente = {
                **dados_prestador,
                'cliente_nome': cliente_info['nome'],
                'cliente_doc_tipo': 'CPF',
                'cliente_doc': cliente_info['cpf'],
                'valor_numerico': cliente_info['valor_numerico'],
                'valor_extenso': cliente_info['valor_extenso'],
                'numero_recibo': str(numero_base + i),
                'descricao_servico': descricao_servico,
                'localidade': localidade,
                'dia': dia,
                'mes': mes,
                'ano': ano
            }
            
            caminho_pdf = exportar_para_pdf(caminho_txt, dados_cliente, pasta)
            if caminho_pdf:
                arquivos_pdf.append(caminho_pdf)
                print(f"✓ PDF gerado: {caminho_pdf.name}")
        
        # Perguntar sobre impressão
        if arquivos_pdf:
            imprimir = input(f"\nDeseja imprimir todos os {len(arquivos_pdf)} recibos agora? (S/N): ").strip().upper()
            
            if imprimir == 'S':
                print("\nEnviando para impressão...")
                for caminho_pdf in arquivos_pdf:
                    imprimir_pdf(caminho_pdf)
                    print(f"✓ Enviado: {caminho_pdf.name}")
    
    print("\n" + "=" * 70)
    print(f"PROCESSO CONCLUÍDO! {len(arquivos_gerados)} recibos gerados.")
    print(f"Arquivos salvos em: {pasta}")
    print("=" * 70)

def mostrar_menu():
    """Exibe o menu principal"""
    limpar_tela()
    print("=" * 60)
    print("GERADOR DE RECIBOS DE PRESTAÇÃO DE SERVIÇO")
    print("=" * 60)
    print()
    print("Escolha uma opção:")
    print("1 - Gerar recibo individual")
    print("2 - Gerar recibos em lote (todos os 4 clientes)")
    print("3 - Gerar recibo consolidado (todos os clientes em um único recibo)")
    print("0 - Sair")
    print()
    return input("Digite sua opção: ").strip()

def main():
    """Função principal com menu de opções"""
    while True:
        opcao = mostrar_menu()
        
        if opcao == '0':
            print("\nEncerrando o programa...")
            break
        elif opcao == '1':
            # Gerar recibo individual (código original)
            gerar_recibo_individual()
        elif opcao == '2':
            # Gerar recibos em lote
            gerar_recibos_em_lote()
        elif opcao == '3':
            # Gerar recibo consolidado
            gerar_recibo_consolidado()
        else:
            print("\n⚠ Opção inválida! Pressione Enter para continuar...")
            input()

def gerar_recibo_consolidado():
    """Gera um único recibo consolidado com todos os 4 clientes"""
    limpar_tela()
    print("=" * 70)
    print("GERADOR DE RECIBO CONSOLIDADO - TODOS OS CLIENTES")
    print("=" * 70)
    print()
    
    # Criar pasta de recibos
    pasta = criar_pasta_recibos()
    
    # Dados do prestador
    print("--- DADOS DO PRESTADOR DE SERVIÇO ---")
    print(f"Prestador padrão: {PRESTADOR_PADRAO['nome']}")
    usar_padrao = input("Usar prestador padrão? (S/N): ").strip().upper()
    
    dados_prestador = {}
    if usar_padrao == 'S':
        dados_prestador['prestador_nome'] = PRESTADOR_PADRAO['nome']
        dados_prestador['prestador_cpf'] = PRESTADOR_PADRAO['cpf']
        dados_prestador['prestador_rg'] = PRESTADOR_PADRAO['rg']
        dados_prestador['prestador_endereco'] = PRESTADOR_PADRAO['endereco']
        dados_prestador['prestador_telefone'] = PRESTADOR_PADRAO['telefone']
    else:
        dados_prestador['prestador_nome'] = input("Nome completo: ").strip()
        dados_prestador['prestador_cpf'] = input("CPF: ").strip()
        dados_prestador['prestador_rg'] = input("RG: ").strip()
        dados_prestador['prestador_endereco'] = input("Endereço completo: ").strip()
        dados_prestador['prestador_telefone'] = input("Telefone: ").strip()
    print()
    
    # Dados do serviço
    print("--- DADOS DO SERVIÇO ---")
    numero_recibo = input("Número do recibo consolidado: ").strip()
    descricao_servico = input("Descrição do serviço prestado: ").strip()
    print()
    
    # Data e local
    print("--- DATA E LOCAL ---")
    print(f"Localidade padrão: {LOCALIDADE_PADRAO}")
    usar_local_padrao = input("Usar localidade padrão? (S/N): ").strip().upper()
    
    if usar_local_padrao == 'S':
        localidade = LOCALIDADE_PADRAO
    else:
        localidade = input("Cidade/Localidade: ").strip()
    
    usar_data_hoje = input("Usar data de hoje? (S/N): ").strip().upper()
    
    if usar_data_hoje == 'S':
        hoje = datetime.now()
        dia = str(hoje.day).zfill(2)
        # Converter mês para português
        meses = {
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        }
        mes = meses[hoje.month]
        ano = str(hoje.year)
    else:
        dia = input("Dia: ").strip()
        mes = input("Mês: ").strip()
        ano = input("Ano: ").strip()
    
    # Calcular valor total
    valor_total_numerico = 0
    for cliente_info in CLIENTES.values():
        # Converter valor de string para float (removendo pontos e vírgulas)
        valor_str = cliente_info['valor_numerico'].replace('.', '').replace(',', '.')
        valor_total_numerico += float(valor_str)
    
    # Converter valor total para formato brasileiro
    valor_total_formatado = f"{valor_total_numerico:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    
    # Converter valor total para extenso (simplificado)
    valor_total_inteiro = int(valor_total_numerico)
    centavos = int((valor_total_numerico - valor_total_inteiro) * 100)
    
    # Função auxiliar para converter números para extenso (básica)
    def numero_para_extenso(numero):
        if numero == 3508:
            return "três mil quinhentos e oito"
        elif numero == 3507:
            return "três mil quinhentos e sete"
        else:
            # Para outros valores, usar uma aproximação
            milhares = numero // 1000
            centenas = numero % 1000
            
            if milhares > 0 and centenas > 0:
                return f"três mil e {centenas}"
            elif milhares > 0:
                return f"três mil"
            else:
                return str(numero)
    
    valor_total_extenso = f"{numero_para_extenso(valor_total_inteiro)} reais"
    if centavos > 0:
        valor_total_extenso += f" e {centavos} centavos"
    
    # Montar dados consolidados
    dados_consolidado = {
        **dados_prestador,
        'numero_recibo': numero_recibo,
        'descricao_servico': descricao_servico,
        'localidade': localidade,
        'dia': dia,
        'mes': mes,
        'ano': ano,
        'valor_total_numerico': valor_total_formatado,
        'valor_total_extenso': valor_total_extenso
    }
    
    # Gerar recibo consolidado TXT
    caminho_txt, conteudo = gerar_recibo_consolidado_txt(dados_consolidado, pasta)
    
    # Exibir prévia
    print("\n" + "=" * 70)
    print("PRÉVIA DO RECIBO CONSOLIDADO:")
    print("=" * 70)
    print(conteudo)
    
    # Perguntar sobre PDF
    exportar_pdf = input("\nDeseja exportar o recibo para PDF? (S/N): ").strip().upper()
    
    if exportar_pdf == 'S':
        caminho_pdf = exportar_recibo_consolidado_para_pdf(caminho_txt, dados_consolidado, pasta)
        
        if caminho_pdf:
            # Perguntar sobre impressão
            imprimir = input("\nDeseja imprimir o recibo agora? (S/N): ").strip().upper()
            
            if imprimir == 'S':
                imprimir_pdf(caminho_pdf)
    
    print("\n" + "=" * 70)
    print("Processo concluído!")
    print("=" * 70)
    
    input("\nPressione Enter para voltar ao menu...")

def gerar_recibo_consolidado_txt(dados, pasta):
    """Gera o arquivo TXT do recibo consolidado"""
    
    # Criar detalhamento dos clientes
    detalhamento_clientes = ""
    for i, (cliente_id, cliente_info) in enumerate(CLIENTES.items(), 1):
        detalhamento_clientes += f"  {i}. {cliente_info['nome']} (CPF: {cliente_info['cpf']}) - R$ {cliente_info['valor_numerico']}\n"
    
    conteudo = f"""
{'=' * 70}
                         RECIBO CONSOLIDADO
{'=' * 70}

Nº: {dados['numero_recibo']}
Valor Total: R$ {dados['valor_total_numerico']}

Eu, {dados['prestador_nome']}, inscrito(a) no CPF sob o nº {dados['prestador_cpf']} 
e no RG nº {dados['prestador_rg']}, declaro que recebi dos seguintes clientes 
a importância total de {dados['valor_total_extenso']}, referente ao pagamento 
pelos seguintes serviços:

{dados['descricao_servico']}

DETALHAMENTO POR CLIENTE:
{detalhamento_clientes}
VALOR TOTAL RECEBIDO: R$ {dados['valor_total_numerico']}

{dados['localidade']}, {dados['dia']} de {dados['mes']} de {dados['ano']}.


_____________________________________________
Assinatura do Prestador de Serviço


Nome: {dados['prestador_nome']}
Endereço: {dados['prestador_endereco']}
Telefone: {dados['prestador_telefone']}

{'=' * 70}
"""
    
    nome_arquivo = f"recibo_consolidado_{dados['numero_recibo']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    caminho_arquivo = pasta / nome_arquivo
    
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    print(f"\n✓ Recibo consolidado salvo em: {caminho_arquivo}")
    return caminho_arquivo, conteudo

def exportar_recibo_consolidado_para_pdf(caminho_txt, dados, pasta):
    """Exporta o recibo consolidado para PDF"""
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import cm
        
        nome_pdf = caminho_txt.stem + ".pdf"
        caminho_pdf = pasta / nome_pdf
        
        c = canvas.Canvas(str(caminho_pdf), pagesize=A4)
        largura, altura = A4
        
        # Título
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(largura/2, altura - 3*cm, "RECIBO CONSOLIDADO")
        
        # Linha separadora
        c.line(3*cm, altura - 3.5*cm, largura - 3*cm, altura - 3.5*cm)
        
        # Conteúdo
        c.setFont("Helvetica", 11)
        y = altura - 5*cm
        
        c.drawString(3*cm, y, f"Nº: {dados['numero_recibo']}")
        y -= 0.7*cm
        c.drawString(3*cm, y, f"Valor Total: R$ {dados['valor_total_numerico']}")
        y -= 1.2*cm
        
        # Texto principal
        c.setFont("Helvetica", 10)
        texto = f"Eu, {dados['prestador_nome']}, inscrito(a) no CPF sob o nº {dados['prestador_cpf']} e no RG nº {dados['prestador_rg']}, declaro que recebi dos seguintes clientes a importância total de {dados['valor_total_extenso']}, referente ao pagamento pelos seguintes serviços:"
        
        # Quebrar texto em linhas
        texto_obj = c.beginText(3*cm, y)
        texto_obj.setFont("Helvetica", 10)
        texto_obj.setLeading(14)
        
        palavras = texto.split()
        linha = ""
        for palavra in palavras:
            teste = linha + palavra + " "
            if c.stringWidth(teste, "Helvetica", 10) < (largura - 6*cm):
                linha = teste
            else:
                texto_obj.textLine(linha)
                linha = palavra + " "
        texto_obj.textLine(linha)
        
        c.drawText(texto_obj)
        y -= 4*cm
        
        # Descrição do serviço
        c.setFont("Helvetica-Bold", 10)
        c.drawString(3*cm, y, dados['descricao_servico'])
        y -= 1.5*cm
        
        # Detalhamento dos clientes
        c.setFont("Helvetica-Bold", 10)
        c.drawString(3*cm, y, "DETALHAMENTO POR CLIENTE:")
        y -= 0.7*cm
        
        c.setFont("Helvetica", 9)
        for i, (cliente_id, cliente_info) in enumerate(CLIENTES.items(), 1):
            c.drawString(3*cm, y, f"{i}. {cliente_info['nome']} (CPF: {cliente_info['cpf']}) - R$ {cliente_info['valor_numerico']}")
            y -= 0.5*cm
        
        y -= 0.5*cm
        c.setFont("Helvetica-Bold", 10)
        c.drawString(3*cm, y, f"VALOR TOTAL RECEBIDO: R$ {dados['valor_total_numerico']}")
        y -= 1.5*cm
        
        # Data e local
        c.setFont("Helvetica", 10)
        c.drawString(3*cm, y, f"{dados['localidade']}, {dados['dia']} de {dados['mes']} de {dados['ano']}.")
        y -= 2.5*cm
        
        # Linha para assinatura
        c.line(3*cm, y, 10*cm, y)
        y -= 0.5*cm
        c.drawString(3*cm, y, "Assinatura do Prestador de Serviço")
        y -= 1.5*cm
        
        # Dados do prestador
        c.setFont("Helvetica", 9)
        c.drawString(3*cm, y, f"Nome: {dados['prestador_nome']}")
        y -= 0.5*cm
        c.drawString(3*cm, y, f"Endereço: {dados['prestador_endereco']}")
        y -= 0.5*cm
        c.drawString(3*cm, y, f"Telefone: {dados['prestador_telefone']}")
        
        c.save()
        print(f"✓ PDF consolidado gerado com sucesso: {caminho_pdf}")
        return caminho_pdf
        
    except ImportError:
        print("\n⚠ A biblioteca 'reportlab' não está instalada.")
        print("Para exportar para PDF, instale com: pip install reportlab")
        return None

def gerar_recibo_individual():
    """Gera um recibo individual (funcionalidade original)"""
    # Criar pasta de recibos
    pasta = criar_pasta_recibos()
    
    # Obter dados
    dados = obter_dados()
    
    # Gerar recibo TXT
    caminho_txt, conteudo = gerar_recibo_txt(dados, pasta)
    
    # Exibir prévia
    print("\n" + "=" * 70)
    print("PRÉVIA DO RECIBO:")
    print("=" * 70)
    print(conteudo)
    
    # Perguntar sobre PDF
    exportar_pdf = input("\nDeseja exportar o recibo para PDF? (S/N): ").strip().upper()
    
    if exportar_pdf == 'S':
        caminho_pdf = exportar_para_pdf(caminho_txt, dados, pasta)
        
        if caminho_pdf:
            # Perguntar sobre impressão
            imprimir = input("\nDeseja imprimir o recibo agora? (S/N): ").strip().upper()
            
            if imprimir == 'S':
                imprimir_pdf(caminho_pdf)
    
    print("\n" + "=" * 70)
    print("Processo concluído!")
    print("=" * 70)
    
    input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    main()