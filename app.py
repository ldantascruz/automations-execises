### Automação para gerar exercícios de matemática estilo Kumon - Versão Web com Flask

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Exercícios de Matemática estilo Kumon - Versão Web com Flask
Autor: Assistant
Descrição: Roda uma aplicação web local para gerar e baixar PDFs de exercícios de matemática.
"""

import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from datetime import datetime
import io
from flask import Flask, request, send_file, render_template_string

# --- INÍCIO DA CLASSE GERADORA (Lógica principal do seu script) ---
class GeradorExerciciosKumon:
    def __init__(self):
        self.largura, self.altura = A4
        self.margem_esquerda = 20 * mm
        self.margem_superior = 20 * mm
        self.espaco_entre_exercicios = 35 * mm
        self.espaco_entre_colunas = 60 * mm
        self.exercicios_por_linha = 3
        self.exercicios_por_coluna = 6
        self.total_exercicios = self.exercicios_por_linha * self.exercicios_por_coluna
        
    def gerar_numero(self, digitos):
        if digitos < 1: digitos = 1
        if digitos == 1: return random.randint(1, 9)
        min_val = 10 ** (digitos - 1)
        max_val = (10 ** digitos) - 1
        return random.randint(min_val, max_val)

    def desenhar_exercicio_adicao(self, c, x, y, num1, num2, indice):
        c.setFont("Helvetica", 8)
        c.drawString(x - 15, y + 5, f"{indice})")
        c.setFont("Helvetica", 14)
        c.drawRightString(x + 40, y, str(num1))
        c.drawString(x - 5, y - 15, "+")
        c.drawRightString(x + 40, y - 15, str(num2))
        c.line(x - 10, y - 25, x + 45, y - 25)
        c.setDash(1, 2)
        c.line(x - 10, y - 40, x + 45, y - 40)
        c.setDash()

    def desenhar_exercicio_subtracao(self, c, x, y, num1, num2, indice):
        if num1 < num2: num1, num2 = num2, num1
        c.setFont("Helvetica", 8)
        c.drawString(x - 15, y + 5, f"{indice})")
        c.setFont("Helvetica", 14)
        c.drawRightString(x + 40, y, str(num1))
        c.drawString(x - 5, y - 15, "-")
        c.drawRightString(x + 40, y - 15, str(num2))
        c.line(x - 10, y - 25, x + 45, y - 25)
        c.setDash(1, 2)
        c.line(x - 10, y - 40, x + 45, y - 40)
        c.setDash()

    def desenhar_exercicio_multiplicacao(self, c, x, y, num1, num2, indice):
        c.setFont("Helvetica", 8)
        c.drawString(x - 15, y + 5, f"{indice})")
        c.setFont("Helvetica", 14)
        c.drawRightString(x + 40, y, str(num1))
        c.drawString(x - 5, y - 15, "×")
        c.drawRightString(x + 40, y - 15, str(num2))
        c.line(x - 10, y - 25, x + 45, y - 25)
        c.setDash(1, 2)
        c.line(x - 10, y - 40, x + 45, y - 40)
        c.setDash()

    def desenhar_exercicio_divisao(self, c, x, y, dividendo, divisor, indice):
        c.setFont("Helvetica", 8)
        c.drawString(x - 15, y + 5, f"{indice})")
        c.setFont("Helvetica", 14)
        c.line(x + 10, y - 5, x + 50, y - 5)
        c.line(x + 10, y - 5, x + 10, y - 25)
        c.drawRightString(x + 5, y - 20, str(divisor))
        c.drawString(x + 15, y - 20, str(dividendo))
        c.setDash(1, 2)
        c.line(x + 15, y + 10, x + 45, y + 10)
        c.setDash()
        
    def gerar_pdf(self, tipo_operacao, digitos1, digitos2, num_folhas=1):
        """ Gera o PDF com uma ou mais folhas de exercícios """
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)

        for pagina in range(num_folhas):
            # --- Início da lógica de desenho da página ---
            c.setFont("Helvetica-Bold", 16)
            titulo = {'adicao': 'Exercícios de Adição', 'subtracao': 'Exercícios de Subtração',
                      'multiplicacao': 'Exercícios de Multiplicação', 'divisao': 'Exercícios de Divisão'}
            c.drawString(self.margem_esquerda, self.altura - self.margem_superior, titulo[tipo_operacao])
            c.setFont("Helvetica", 10)
            c.drawString(self.margem_esquerda, self.altura - self.margem_superior - 20, 
                           f"Data: ____/____/____    Nome: _________________________________")
            
            exercicios, gabarito = [], []
            for i in range(self.total_exercicios):
                num1, num2 = self.gerar_numero(digitos1), self.gerar_numero(digitos2)
                if tipo_operacao == 'adicao':
                    exercicios.append((num1, num2)); gabarito.append(num1 + num2)
                elif tipo_operacao == 'subtracao':
                    if num1 < num2: num1, num2 = num2, num1
                    exercicios.append((num1, num2)); gabarito.append(num1 - num2)
                elif tipo_operacao == 'multiplicacao':
                    exercicios.append((num1, num2)); gabarito.append(num1 * num2)
                elif tipo_operacao == 'divisao':
                    if num2 == 0: num2 = 1
                    dividendo = num1 * num2
                    exercicios.append((dividendo, num2)); gabarito.append(num1)

            y_inicial = self.altura - self.margem_superior - 60
            for i, (n1, n2) in enumerate(exercicios):
                linha, coluna = i // self.exercicios_por_linha, i % self.exercicios_por_linha
                x = self.margem_esquerda + 20 + (coluna * self.espaco_entre_colunas)
                y = y_inicial - (linha * self.espaco_entre_exercicios)
                
                if tipo_operacao == 'adicao': self.desenhar_exercicio_adicao(c, x, y, n1, n2, i + 1)
                elif tipo_operacao == 'subtracao': self.desenhar_exercicio_subtracao(c, x, y, n1, n2, i + 1)
                elif tipo_operacao == 'multiplicacao': self.desenhar_exercicio_multiplicacao(c, x, y, n1, n2, i + 1)
                elif tipo_operacao == 'divisao': self.desenhar_exercicio_divisao(c, x, y, n1, n2, i + 1)
            
            y_gabarito = 50 * mm
            c.setDash(3, 3)
            c.line(self.margem_esquerda - 10, y_gabarito + 10 * mm, self.largura - self.margem_esquerda + 10, y_gabarito + 10 * mm)
            c.setDash()
            c.setFont("Helvetica", 8)
            c.drawString(self.margem_esquerda, y_gabarito + 12 * mm, "✂️  Recorte aqui para separar o gabarito")
            c.setFont("Helvetica-Bold", 10)
            c.drawString(self.margem_esquerda, y_gabarito, "GABARITO:")
            c.setFont("Helvetica", 9)
            gabarito_por_coluna = 6
            x_gabarito = self.margem_esquerda
            y_gabarito_linha = y_gabarito - (5 * mm)
            for i, resposta in enumerate(gabarito):
                if i > 0 and i % gabarito_por_coluna == 0:
                    x_gabarito += 40 * mm; y_gabarito_linha = y_gabarito - (5 * mm)
                c.drawString(x_gabarito, y_gabarito_linha, f"{i + 1}) {resposta}")
                y_gabarito_linha -= 5 * mm
            # --- Fim da lógica de desenho da página ---

            # Se não for a última página, cria uma nova página em branco
            if pagina < num_folhas - 1:
                c.showPage()
        
        c.save()
        buffer.seek(0)
        return buffer

# --- FIM DA CLASSE GERADORA ---


# --- INÍCIO DA APLICAÇÃO WEB FLASK ---
app = Flask(__name__)

# O HTML da página web fica aqui dentro do script Python
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Exercícios Kumon</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Inter', sans-serif; }
        @import url('https://rsms.me/inter/inter.css');
        .form-select {
            background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e");
            background-position: right 0.5rem center;
            background-repeat: no-repeat;
            background-size: 1.5em 1.5em;
            padding-right: 2.5rem;
            -webkit-print-color-adjust: exact;
        }
    </style>
</head>
<body class="bg-slate-100 flex items-center justify-center min-h-screen">
    <div class="w-full max-w-lg p-8 space-y-6 bg-white rounded-xl shadow-lg">
        <h1 class="text-3xl font-bold text-center text-slate-800">Gerador de Exercícios</h1>
        <p class="text-center text-slate-500">Escolha as opções abaixo para criar sua folha de atividades.</p>
        
        <form action="/generate" method="post" id="exercise-form" class="space-y-6">
            <div>
                <label for="tipo_operacao" class="block text-sm font-medium text-slate-700">Tipo de Operação</label>
                <select id="tipo_operacao" name="tipo_operacao" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm appearance-none form-select">
                    <option value="adicao">Adição</option>
                    <option value="subtracao">Subtração</option>
                    <option value="multiplicacao">Multiplicação</option>
                    <option value="divisao">Divisão</option>
                </select>
            </div>

            <div id="numeros-normais">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label for="digitos1" id="label_digitos1" class="block text-sm font-medium text-slate-700">Dígitos da 1ª Parcela</label>
                        <input type="number" name="digitos1" id="digitos1" value="2" min="1" max="4" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                    </div>
                    <div>
                        <label for="digitos2" id="label_digitos2" class="block text-sm font-medium text-slate-700">Dígitos da 2ª Parcela</label>
                        <input type="number" name="digitos2" id="digitos2" value="2" min="1" max="4" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                    </div>
                </div>
            </div>

            <div>
                <label for="num_folhas" class="block text-sm font-medium text-slate-700">Quantidade de Folhas</label>
                <input type="number" name="num_folhas" id="num_folhas" value="1" min="1" max="20" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
            </div>

            <div>
                <button type="submit" class="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors">
                    Gerar PDF
                </button>
            </div>
        </form>
    </div>

    <script>
        const tipoOperacaoSelect = document.getElementById('tipo_operacao');
        const labelDigitos1 = document.getElementById('label_digitos1');
        const labelDigitos2 = document.getElementById('label_digitos2');

        const labels = {
            'adicao': ['Dígitos da 1ª Parcela', 'Dígitos da 2ª Parcela'],
            'subtracao': ['Dígitos do Minuendo', 'Dígitos do Subtraendo'],
            'multiplicacao': ['Dígitos do Multiplicando', 'Dígitos do Multiplicador'],
            'divisao': ['Dígitos do Quociente', 'Dígitos do Divisor']
        };

        tipoOperacaoSelect.addEventListener('change', (event) => {
            const operacao = event.target.value;
            const [label1, label2] = labels[operacao];
            labelDigitos1.textContent = label1;
            labelDigitos2.textContent = label2;
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """ Rota principal que exibe a página web """
    return render_template_string(HTML_TEMPLATE)

@app.route('/generate', methods=['POST'])
def generate_pdf():
    """ Rota que gera e envia o PDF para download """
    try:
        # Pega os dados do formulário web
        tipo = request.form.get('tipo_operacao')
        digitos1 = int(request.form.get('digitos1'))
        digitos2 = int(request.form.get('digitos2'))
        num_folhas = int(request.form.get('num_folhas', 1))

        # Validação simples para o número de folhas
        if not 1 <= num_folhas <= 20:
            num_folhas = 1
        
        # Cria a instância e gera o PDF em memória com o número de folhas solicitado
        gerador = GeradorExerciciosKumon()
        buffer = gerador.gerar_pdf(tipo, digitos1, digitos2, num_folhas)
        
        # Cria um nome de arquivo único
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"exercicios_{tipo}_{timestamp}.pdf"
        
        # Envia o arquivo do buffer para o navegador
        return send_file(
            buffer,
            as_attachment=True,
            download_name=nome_arquivo,
            mimetype='application/pdf'
        )
    except Exception as e:
        # Em caso de erro, retorna uma mensagem
        return f"Ocorreu um erro: {e}", 500

if __name__ == '__main__':
    # Roda a aplicação web, acessível na sua rede local
    # Use host='0.0.0.0' para tornar acessível por outros dispositivos na mesma rede
    print("="*50)
    print("Servidor do Gerador de Exercícios iniciado!")
    print("Abra o navegador em qualquer dispositivo na sua rede e acesse:")
    print("http://192.168.3.218:5001")
    print("Para encontrar o IP do seu Mac, vá em 'Ajustes do Sistema' -> 'Rede'.")
    print("Para parar o servidor, pressione CTRL+C no terminal.")
    print("="*50)
    app.run(host='0.0.0.0', port=5001, debug=False)

