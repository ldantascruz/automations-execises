## Gerador de Exercícios de Matemática estilo Kumon

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Exercícios de Matemática estilo Kumon
Autor: Assistant
Descrição: Gera PDFs com exercícios de matemática para prática, com opção de gerar múltiplas folhas.
"""

import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from datetime import datetime
import os
import subprocess
import sys
import time

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
        """Gera um número aleatório com a quantidade especificada de dígitos"""
        if digitos < 1:
            digitos = 1
        if digitos == 1:
            return random.randint(1, 9)
        else:
            min_val = 10 ** (digitos - 1)
            max_val = (10 ** digitos) - 1
            return random.randint(min_val, max_val)
    
    def desenhar_exercicio_adicao(self, c, x, y, num1, num2, indice):
        """Desenha um exercício de adição"""
        # Número do exercício
        c.setFont("Helvetica", 8)
        c.drawString(x - 15, y + 5, f"{indice})")
        
        # Primeiro número
        c.setFont("Helvetica", 14)
        c.drawRightString(x + 40, y, str(num1))
        
        # Sinal de mais
        c.drawString(x - 5, y - 15, "+")
        
        # Segundo número
        c.drawRightString(x + 40, y - 15, str(num2))
        
        # Linha
        c.line(x - 10, y - 25, x + 45, y - 25)
        
        # Espaço para resposta (pontilhado)
        c.setDash(1, 2)
        c.line(x - 10, y - 40, x + 45, y - 40)
        c.setDash()
        
    def desenhar_exercicio_subtracao(self, c, x, y, num1, num2, indice):
        """Desenha um exercício de subtração"""
        # Garantir que num1 >= num2
        if num1 < num2:
            num1, num2 = num2, num1
            
        # Número do exercício
        c.setFont("Helvetica", 8)
        c.drawString(x - 15, y + 5, f"{indice})")
        
        # Primeiro número
        c.setFont("Helvetica", 14)
        c.drawRightString(x + 40, y, str(num1))
        
        # Sinal de menos
        c.drawString(x - 5, y - 15, "-")
        
        # Segundo número
        c.drawRightString(x + 40, y - 15, str(num2))
        
        # Linha
        c.line(x - 10, y - 25, x + 45, y - 25)
        
        # Espaço para resposta (pontilhado)
        c.setDash(1, 2)
        c.line(x - 10, y - 40, x + 45, y - 40)
        c.setDash()
        
    def desenhar_exercicio_multiplicacao(self, c, x, y, num1, num2, indice):
        """Desenha um exercício de multiplicação"""
        # Número do exercício
        c.setFont("Helvetica", 8)
        c.drawString(x - 15, y + 5, f"{indice})")
        
        # Multiplicando (em cima)
        c.setFont("Helvetica", 14)
        c.drawRightString(x + 40, y, str(num1))
        
        # Sinal de vezes
        c.drawString(x - 5, y - 15, "×")
        
        # Multiplicador (embaixo)
        c.drawRightString(x + 40, y - 15, str(num2))
        
        # Linha
        c.line(x - 10, y - 25, x + 45, y - 25)
        
        # Espaço para resposta (pontilhado)
        c.setDash(1, 2)
        c.line(x - 10, y - 40, x + 45, y - 40)
        c.setDash()
        
    def desenhar_exercicio_divisao(self, c, x, y, dividendo, divisor, indice):
        """Desenha um exercício de divisão"""
        # Número do exercício
        c.setFont("Helvetica", 8)
        c.drawString(x - 15, y + 5, f"{indice})")
        
        c.setFont("Helvetica", 14)
        
        # Desenhar a chave de divisão
        # Linha horizontal
        c.line(x + 10, y - 5, x + 50, y - 5)
        # Linha vertical
        c.line(x + 10, y - 5, x + 10, y - 25)
        
        # Divisor (à esquerda da chave)
        c.drawRightString(x + 5, y - 20, str(divisor))
        
        # Dividendo (dentro da chave)
        c.drawString(x + 15, y - 20, str(dividendo))
        
        # Espaço para quociente (acima da linha horizontal)
        c.setDash(1, 2)
        c.line(x + 15, y + 10, x + 45, y + 10)
        c.setDash()
        
    def gerar_pdf(self, tipo_operacao, digitos1, digitos2, nome_arquivo="exercicios_kumon.pdf"):
        """Gera o PDF com os exercícios"""
        c = canvas.Canvas(nome_arquivo, pagesize=A4)
        
        # Título
        c.setFont("Helvetica-Bold", 16)
        titulo = {
            'adicao': 'Exercícios de Adição',
            'subtracao': 'Exercícios de Subtração',
            'multiplicacao': 'Exercícios de Multiplicação',
            'divisao': 'Exercícios de Divisão'
        }
        c.drawString(self.margem_esquerda, self.altura - self.margem_superior, titulo[tipo_operacao])
        
        # Data e nome
        c.setFont("Helvetica", 10)
        c.drawString(self.margem_esquerda, self.altura - self.margem_superior - 20, 
                       f"Data: ____/____/____    Nome: _________________________________")
        
        # Gerar exercícios e gabarito
        exercicios = []
        gabarito = []
        
        for i in range(self.total_exercicios):
            num1 = self.gerar_numero(digitos1)
            num2 = self.gerar_numero(digitos2)
            
            if tipo_operacao == 'adicao':
                exercicios.append((num1, num2))
                gabarito.append(num1 + num2)
            elif tipo_operacao == 'subtracao':
                # Garantir que o resultado seja positivo
                if num1 < num2:
                    num1, num2 = num2, num1
                exercicios.append((num1, num2))
                gabarito.append(num1 - num2)
            elif tipo_operacao == 'multiplicacao':
                exercicios.append((num1, num2))
                gabarito.append(num1 * num2)
            elif tipo_operacao == 'divisao':
                # Garantir divisão exata e que o divisor não seja zero
                if num2 == 0: num2 = 1
                dividendo = num1 * num2
                exercicios.append((dividendo, num2))
                gabarito.append(num1)
        
        # Desenhar exercícios
        y_inicial = self.altura - self.margem_superior - 60
        
        for i, (n1, n2) in enumerate(exercicios):
            linha = i // self.exercicios_por_linha
            coluna = i % self.exercicios_por_linha
            
            x = self.margem_esquerda + 20 + (coluna * self.espaco_entre_colunas)
            y = y_inicial - (linha * self.espaco_entre_exercicios)
            
            if tipo_operacao == 'adicao':
                self.desenhar_exercicio_adicao(c, x, y, n1, n2, i + 1)
            elif tipo_operacao == 'subtracao':
                self.desenhar_exercicio_subtracao(c, x, y, n1, n2, i + 1)
            elif tipo_operacao == 'multiplicacao':
                self.desenhar_exercicio_multiplicacao(c, x, y, n1, n2, i + 1)
            elif tipo_operacao == 'divisao':
                self.desenhar_exercicio_divisao(c, x, y, n1, n2, i + 1)
        
        # Linha de recorte
        y_gabarito = 50 * mm
        c.setDash(3, 3)
        c.line(self.margem_esquerda - 10, y_gabarito + 10 * mm, self.largura - self.margem_esquerda + 10, y_gabarito + 10 * mm)
        c.setDash()
        
        # Texto indicando recorte
        c.setFont("Helvetica", 8)
        c.drawString(self.margem_esquerda, y_gabarito + 12 * mm, "✂️  Recorte aqui para separar o gabarito")
        
        # Gabarito
        c.setFont("Helvetica-Bold", 10)
        c.drawString(self.margem_esquerda, y_gabarito, "GABARITO:")
        
        c.setFont("Helvetica", 9)
        # Organiza o gabarito em colunas para melhor visualização
        gabarito_por_coluna = 6
        x_gabarito = self.margem_esquerda
        y_gabarito_linha = y_gabarito - (5 * mm)

        for i, resposta in enumerate(gabarito):
            if i > 0 and i % gabarito_por_coluna == 0:
                x_gabarito += 40 * mm
                y_gabarito_linha = y_gabarito - (5 * mm)

            texto_resposta = f"{i + 1}) {resposta}"
            c.drawString(x_gabarito, y_gabarito_linha, texto_resposta)
            y_gabarito_linha -= 5 * mm
        
        c.save()
        return nome_arquivo

def main():
    print("=" * 50)
    print("GERADOR DE EXERCÍCIOS DE MATEMÁTICA - ESTILO KUMON")
    print("=" * 50)
    
    gerador = GeradorExerciciosKumon()
    
    while True:
        print("\nEscolha o tipo de operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")
        
        opcao = input("\nDigite sua opção: ")
        
        if opcao == '0':
            print("Encerrando o programa...")
            break
            
        if opcao not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue
        
        tipo_map = {
            '1': 'adicao',
            '2': 'subtracao',
            '3': 'multiplicacao',
            '4': 'divisao'
        }
        
        tipo = tipo_map[opcao]
        
        try:
            # Solicitar quantidade de dígitos
            if tipo == 'divisao':
                print("\nPara divisão:")
                digitos_divisor = int(input("Quantos dígitos para o DIVISOR? (1-3): "))
                digitos_quociente = int(input("Quantos dígitos para o QUOCIENTE? (1-3): "))
                digitos1 = digitos_quociente
                digitos2 = digitos_divisor
            else:
                nomes = {
                    'adicao': ('primeira parcela', 'segunda parcela'),
                    'subtracao': ('minuendo', 'subtraendo'),
                    'multiplicacao': ('multiplicando', 'multiplicador')
                }
                
                nome1, nome2 = nomes[tipo]
                
                digitos1 = int(input(f"\nQuantos dígitos para o {nome1}? (1-4): "))
                digitos2 = int(input(f"Quantos dígitos para o {nome2}? (1-4): "))
            
            # NOVO: Perguntar quantas folhas gerar
            num_folhas = int(input("\nQuantas folhas você deseja gerar? (1-20): "))
            if not 1 <= num_folhas <= 20:
                print("Número de folhas inválido. Por favor, insira um valor entre 1 e 20.")
                continue

        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
            continue

        # Gerar os PDFs
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        arquivos_gerados = []

        pasta_principal = "exercicios"
        pasta_operacao = os.path.join(pasta_principal, tipo)
        os.makedirs(pasta_operacao, exist_ok=True) # Cria as pastas se não existirem

        # Gerar os PDFs
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        arquivos_gerados = []

        print(f"\nGerando arquivos na pasta '{pasta_operacao}'...")
        for i in range(num_folhas):
            nome_base_arquivo = f"exercicios_{tipo}_{timestamp}_folha{i + 1}.pdf"
            caminho_completo_arquivo = os.path.join(pasta_operacao, nome_base_arquivo)
            
            arquivo = gerador.gerar_pdf(tipo, digitos1, digitos2, caminho_completo_arquivo)
            arquivos_gerados.append(arquivo)

        print(f"\n✅ {len(arquivos_gerados)} folha(s) de exercícios gerada(s) com sucesso!")
        print(f"📄 Os arquivos foram salvos em: {os.path.abspath(pasta_operacao)}")

        if sys.platform == "darwin": # Verifica se o sistema operacional é macOS
            imprimir = input("\nDeseja imprimir os arquivos gerados? (s/n): ").lower()
            if imprimir == 's':
                print("\nEnviando arquivos para a impressora padrão...")
                for arquivo in arquivos_gerados:
                    try:
                        # Usa o comando 'lp' do macOS para imprimir
                        subprocess.run(['lp', arquivo], check=True)
                        print(f" -> '{os.path.basename(arquivo)}' enviado para a fila de impressão.")
                        time.sleep(2) # Pausa para não sobrecarregar a fila da impressora
                    except FileNotFoundError:
                        print(f"Erro: O comando 'lp' não foi encontrado. A impressão não é possível.")
                        break
                    except subprocess.CalledProcessError as e:
                        print(f"Erro ao tentar imprimir o arquivo {arquivo}: {e}")
                        break
                print("\n✅ Concluído. Verifique a fila da sua impressora.")
        
        continuar = input("\nDeseja gerar mais exercícios? (s/n): ")
        if continuar.lower() != 's':
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    main()
