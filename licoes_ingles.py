# -*- coding: utf-8 -*-
"""
Gerador de Lições de Inglês com IA (Gemini)
Autor: Assistant
Descrição: Gera PDFs com lições de inglês personalizadas sobre qualquer tópico.
"""

import logging
logging.getLogger('absl').setLevel(logging.ERROR)
import os
import google.generativeai as genai
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import navy, black
from dotenv import load_dotenv

def configurar_api_gemini():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Erro: A chave da API do Gemini não foi encontrada.")
        print("Por favor, crie um arquivo '.env' e adicione a linha: GEMINI_API_KEY='SUA_CHAVE_API_AQUI'")
        return None
    genai.configure(api_key=api_key)
    listar_modelos_disponiveis()
    try:
        return genai.GenerativeModel('gemini-2.5-pro')
    except Exception as e:
        print(f"Erro ao carregar gemini-2.5-pro: {e}")
        print("Tentando modelo alternativo: gemini-2.5-flash")
        return genai.GenerativeModel('gemini-2.5-flash')

def listar_modelos_disponiveis():
    """
    Lista os modelos disponíveis na API do Gemini.
    """
    try:
        models = genai.list_models()
        print("Modelos disponíveis:")
        for model in models:
            print(f"- {model.name} (Supported methods: {', '.join(model.supported_generation_methods)})")
    except Exception as e:
        print(f"Erro ao listar modelos: {e}")

def gerar_conteudo_licao(model, topic):
    """
    Usa o modelo Gemini para gerar o conteúdo da lição com base em um tópico.
    """
    print(f"🤖 Gerando conteúdo para a lição sobre '{topic}' com a IA... Aguarde.")
    
    prompt = f"""
    Você é um professor de inglês didático e seu aluno é um falante de português brasileiro.
    Crie uma lição completa sobre o tópico: '{topic}'.
    A lição deve ser estruturada exatamente no seguinte formato, usando os títulos em português:

    ### Explicação Simples:
    (Uma explicação clara e concisa do tópico em português, com no máximo 2 parágrafos.)

    ### Exemplos de Aplicação:
    (Pelo menos 3 frases de exemplo em inglês com a tradução em português ao lado.)

    ### Como Usar (Frases Simples):
    (Mostre a estrutura de frases afirmativas, negativas e interrogativas, se aplicável, com exemplos.)

    ### Como Fica a Fala (Pronúncia):
    (Dê dicas de pronúncia e mencione contrações comuns, explicando como se fala de forma simples, como "fala-se: uórks".)

    ### Exercícios:
    (Crie 5 exercícios de completar a frase para praticar o tópico. Use ___ para o espaço a ser preenchido.)

    ### Gabarito:
    (Apresente as respostas corretas para os 5 exercícios.)

    Certifique-se de que o conteúdo seja adequado para um aluno de nível básico a intermediário.
    Não adicione formatação adicional, como tabelas ou cabeçalhos além dos solicitados com '###'. Use texto simples e claro para facilitar a geração de PDF.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API do Gemini: {e}")
        return None

def criar_pdf_licao(topic, content):
    """
    Cria um arquivo PDF formatado com o conteúdo da lição gerado pela IA.
    """
    # Sanitiza o nome do arquivo
    file_name = f"licao_ingles_{topic.replace(' ', '_').lower()}.pdf"
    print(f"📄 Formatando e criando o arquivo PDF: {file_name}")

    doc = SimpleDocTemplate(file_name, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    
    # Estilos personalizados
    styles.add(ParagraphStyle(name='TitleStyle', fontName='Helvetica-Bold', fontSize=18, textColor=navy, spaceAfter=12))
    styles.add(ParagraphStyle(name='HeadingStyle', fontName='Helvetica-Bold', fontSize=14, textColor=black, spaceBefore=12, spaceAfter=6))
    styles.add(ParagraphStyle(name='BodyStyle', fontName='Helvetica', fontSize=11, leading=14, alignment=4)) # Justificado

    story = []
    
    # Adiciona o Título da Lição
    story.append(Paragraph(f"Lição de Inglês: {topic.title()}", styles['TitleStyle']))
    story.append(Spacer(1, 0.5*cm))

    # Processa o conteúdo gerado pela IA
    lines = content.split('\n')
    for line in lines:
        if line.startswith('### '):
            # É um título de seção
            heading_text = line.replace('### ', '').strip()
            story.append(Paragraph(heading_text, styles['HeadingStyle']))
        elif line.strip():
            # É um parágrafo de conteúdo
            # Substitui `*` por `•` para listas
            line = line.replace('*', '•')
            story.append(Paragraph(line, styles['BodyStyle']))
            
    # Gera o PDF
    try:
        doc.build(story)
        print(f"✅ PDF gerado com sucesso: {file_name}")
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o PDF: {e}")


def main():
    """
    Função principal que orquestra a interação com o usuário.
    """
    print("=" * 60)
    print("      GERADOR DE LIÇÕES DE INGLÊS COM INTELIGÊNCIA ARTIFICIAL")
    print("=" * 60)
    
    model = configurar_api_gemini()
    if not model:
        return # Encerra se a API não pôde ser configurada

    while True:
        topic = input("\n> Qual tópico de inglês você gostaria de aprender hoje?\n  (Ex: Verbo To Be, Simple Present, Prepositions of time)\n> Digite o tópico: ")
        
        if not topic.strip():
            print("Por favor, digite um tópico válido.")
            continue
            
        content = gerar_conteudo_licao(model, topic)
        
        if content:
            criar_pdf_licao(topic, content)
            
        continuar = input("\nDeseja gerar outra lição? (s/n): ").lower()
        if continuar != 's':
            print("Até a próxima e bons estudos!")
            break

if __name__ == "__main__":
    main()
