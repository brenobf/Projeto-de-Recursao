
import tkinter as tk
from tkinter import ttk, messagebox
from time import perf_counter
import turtle


# ==================================================
# 1. ALGORITMOS
# ==================================================

def fatorial_recursivo(n):
    if n < 0:
        raise ValueError("Número inválido")
    if n <= 1:
        return 1
    return n * fatorial_recursivo(n - 1)


def fatorial_iterativo(n):
    if n < 0:
        raise ValueError("Número inválido")

    resultado = 1

    for i in range(2, n + 1):
        resultado *= i

    return resultado


def fibonacci_recursivo(n):
    if n < 0:
        raise ValueError("Número inválido")

    if n <= 1:
        return n

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_iterativo(n):
    if n < 0:
        raise ValueError("Número inválido")

    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a


def fibonacci_memoizado(n, memoria=None):
    if n < 0:
        raise ValueError("Número inválido")

    if memoria is None:
        memoria = {}

    if n in memoria:
        return memoria[n]

    if n <= 1:
        return n

    memoria[n] = (
        fibonacci_memoizado(n - 1, memoria)
        + fibonacci_memoizado(n - 2, memoria)
    )

    return memoria[n]


def fibonacci_contador(n):
    chamadas = 0

    def calcular(k):
        nonlocal chamadas
        chamadas += 1

        if k <= 1:
            return k

        return calcular(k - 1) + calcular(k - 2)

    resultado = calcular(n)

    return resultado, chamadas


def torre_hanoi(n, origem="A", destino="C", auxiliar="B"):
    movimentos = []

    def resolver(qtd, o, d, a):
        if qtd == 1:
            movimentos.append((1, o, d))
            return

        resolver(qtd - 1, o, a, d)

        movimentos.append((qtd, o, d))

        resolver(qtd - 1, a, d, o)

    if n < 1:
        raise ValueError("Use pelo menos um disco.")

    resolver(n, origem, destino, auxiliar)

    return movimentos


def pilha_fibonacci(n):
    chamadas = []

    def rastrear(valor, nivel):
        chamadas.append((valor, nivel))

        if valor <= 1:
            return

        rastrear(valor - 1, nivel + 1)
        rastrear(valor - 2, nivel + 1)

    rastrear(n, 0)

    return chamadas


# ==================================================
# 2. TESTES DOS ALGORITMOS
# ==================================================

def executar_testes():
    assert fatorial_recursivo(5) == 120
    assert fatorial_iterativo(5) == 120

    for n in range(11):
        assert fibonacci_recursivo(n) == fibonacci_iterativo(n)
        assert fibonacci_iterativo(n) == fibonacci_memoizado(n)

    for n in range(1, 6):
        movimentos = torre_hanoi(n)
        assert len(movimentos) == 2 ** n - 1

        pinos = {
            "A": list(range(n, 0, -1)),
            "B": [],
            "C": []
        }

        for disco, origem, destino in movimentos:
            assert pinos[origem][-1] == disco

            assert (
                not pinos[destino]
                or pinos[destino][-1] > disco
            )

            pinos[origem].pop()
            pinos[destino].append(disco)

        assert pinos["C"] == list(range(n, 0, -1))

    return True


# ==================================================
# 3. INTERFACE GRÁFICA
# ==================================================

class ProjetoRecursao:

    def __init__(self, janela):

        self.janela = janela
        self.janela.title("Projeto de Recursão - Grupo 3")
        self.janela.geometry("900x650")

        ttk.Label(
            janela,
            text="PROJETO DE RECURSÃO",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        ttk.Label(
            janela,
            text="Fatorial | Fibonacci | Torre de Hanói"
        ).pack()

        self.abas = ttk.Notebook(janela)
        self.abas.pack(fill="both", expand=True, padx=10, pady=10)

        self.criar_aba_algoritmos()
        self.criar_aba_desempenho()
        self.criar_aba_pilha()
        self.criar_aba_hanoi()
        self.criar_aba_fractal()

    # ------------------------------------------------
    # ABA 1 - ALGORITMOS
    # ------------------------------------------------

    def criar_aba_algoritmos(self):

        aba = ttk.Frame(self.abas, padding=15)
        self.abas.add(aba, text="Algoritmos")

        ttk.Label(
            aba,
            text="Digite um número:"
        ).pack()

        self.numero = ttk.Entry(aba)
        self.numero.insert(0, "6")
        self.numero.pack(pady=5)

        ttk.Button(
            aba,
            text="Calcular",
            command=self.calcular
        ).pack(pady=5)

        self.resultado = tk.Text(
            aba,
            height=20,
            font=("Consolas", 11)
        )

        self.resultado.pack(fill="both", expand=True)

    def calcular(self):

        try:
            n = int(self.numero.get())

            if not 0 <= n <= 900:
                raise ValueError("Digite um número entre 0 e 900.")

            fat_r = fatorial_recursivo(n)
            fat_i = fatorial_iterativo(n)

            fib_i = fibonacci_iterativo(n)
            fib_m = fibonacci_memoizado(n)

            if n <= 35:
                fib_r = fibonacci_recursivo(n)
            else:
                fib_r = "Não calculado: custo exponencial muito alto."

            texto = f"""
RESULTADOS

FATORIAL

Recursivo: {fat_r}
Iterativo: {fat_i}

Resultados iguais: {fat_r == fat_i}


FIBONACCI

Recursivo: {fib_r}
Iterativo: {fib_i}
Memoização: {fib_m}
"""

            self.resultado.delete("1.0", tk.END)
            self.resultado.insert(tk.END, texto)

        except (ValueError, RecursionError) as erro:
            messagebox.showerror("Erro", str(erro))

    # ------------------------------------------------
    # ABA 2 - DESEMPENHO
    # ------------------------------------------------

    def criar_aba_desempenho(self):

        aba = ttk.Frame(self.abas, padding=15)
        self.abas.add(aba, text="Desempenho")

        ttk.Label(
            aba,
            text="Análise do Fibonacci",
            font=("Arial", 15, "bold")
        ).pack(pady=10)

        ttk.Button(
            aba,
            text="Executar análise",
            command=self.analisar
        ).pack()

        self.saida_desempenho = tk.Text(
            aba,
            font=("Consolas", 11)
        )

        self.saida_desempenho.pack(fill="both", expand=True, pady=10)

    def analisar(self):

        self.saida_desempenho.delete("1.0", tk.END)

        self.saida_desempenho.insert(
            tk.END,
            "CONTAGEM DE CHAMADAS\n\n"
        )

        for n in (10, 20, 30):

            valor, chamadas = fibonacci_contador(n)

            self.saida_desempenho.insert(
                tk.END,
                f"N = {n}\n"
                f"Fibonacci = {valor}\n"
                f"Chamadas = {chamadas:,}\n\n".replace(",", ".")
            )

        self.saida_desempenho.insert(
            tk.END,
            "\nCOMPARAÇÃO DE TEMPO (segundos)\n\n"
        )

        for n in (10, 20, 30):

            inicio = perf_counter()
            r = fibonacci_recursivo(n)
            tempo_r = perf_counter() - inicio

            inicio = perf_counter()
            i = fibonacci_iterativo(n)
            tempo_i = perf_counter() - inicio

            inicio = perf_counter()
            m = fibonacci_memoizado(n)
            tempo_m = perf_counter() - inicio

            assert r == i == m

            self.saida_desempenho.insert(
                tk.END,
                f"N = {n}\n"
                f"Recursivo: {tempo_r:.8f}s\n"
                f"Iterativo: {tempo_i:.8f}s\n"
                f"Memoização: {tempo_m:.8f}s\n\n"
            )

        self.saida_desempenho.insert(
            tk.END,
            "CONCLUSÃO:\n"
            "O Fibonacci recursivo simples recalcula valores.\n"
            "O iterativo evita chamadas recursivas.\n"
            "A memoização armazena resultados anteriores.\n"
            "Os tempos podem variar conforme o computador.\n"
        )

    # ------------------------------------------------
    # ABA 3 - PILHA DE CHAMADAS
    # ------------------------------------------------

    def criar_aba_pilha(self):

        aba = ttk.Frame(self.abas, padding=15)
        self.abas.add(aba, text="Pilha de chamadas")

        ttk.Label(
            aba,
            text="Visualização da recursão"
        ).pack()

        self.numero_pilha = ttk.Entry(aba)
        self.numero_pilha.insert(0, "3")
        self.numero_pilha.pack(pady=5)

        ttk.Button(
            aba,
            text="Mostrar chamadas",
            command=self.mostrar_pilha
        ).pack()

        self.saida_pilha = tk.Text(
            aba,
            font=("Consolas", 11)
        )

        self.saida_pilha.pack(fill="both", expand=True, pady=10)

    def mostrar_pilha(self):

        try:
            n = int(self.numero_pilha.get())

            if not 0 <= n <= 8:
                raise ValueError("Use números entre 0 e 8.")

            chamadas = pilha_fibonacci(n)

            self.saida_pilha.delete("1.0", tk.END)

            for valor, nivel in chamadas:

                espacos = "    " * nivel

                if valor <= 1:
                    texto = " <- CASO BASE"
                else:
                    texto = ""

                self.saida_pilha.insert(
                    tk.END,
                    f"{espacos}fib({valor}){texto}\n"
                )

            self.saida_pilha.insert(
                tk.END,
                f"\nTotal de chamadas: {len(chamadas)}"
            )

        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    # ------------------------------------------------
    # ABA 4 - TORRE DE HANOI
    # ------------------------------------------------

    def criar_aba_hanoi(self):

        aba = ttk.Frame(self.abas, padding=10)
        self.abas.add(aba, text="Torre de Hanói")

        ttk.Label(
            aba,
            text="Animação da Torre de Hanói",
            font=("Arial", 15, "bold")
        ).pack(pady=5)

        linha = ttk.Frame(aba)
        linha.pack()

        ttk.Label(
            linha,
            text="Quantidade de discos:"
        ).pack(side="left")

        self.numero_hanoi = ttk.Entry(linha, width=5)
        self.numero_hanoi.insert(0, "3")
        self.numero_hanoi.pack(side="left", padx=5)

        ttk.Button(
            linha,
            text="Resolver",
            command=self.iniciar_hanoi
        ).pack(side="left")

        self.canvas = tk.Canvas(
            aba,
            bg="white",
            height=330
        )

        self.canvas.pack(fill="both", expand=True, pady=10)

        self.status_hanoi = ttk.Label(
            aba,
            text="Mínimo de movimentos: 2ⁿ - 1"
        )

        self.status_hanoi.pack()

        self.janela.after(100, self.desenhar_inicio)

    def desenhar_inicio(self):

        self.canvas.delete("all")

        largura = max(self.canvas.winfo_width(), 600)

        self.centros = [
            largura * 0.2,
            largura * 0.5,
            largura * 0.8
        ]

        for x in self.centros:

            self.canvas.create_rectangle(
                x - 4, 80, x + 4, 290,
                fill="gray"
            )

            self.canvas.create_rectangle(
                x - 85, 290, x + 85, 300,
                fill="gray"
            )

        for i, nome in enumerate(["A", "B", "C"]):
            self.canvas.create_text(
                self.centros[i], 315,
                text=nome
            )

    def desenhar_discos(self):

        self.desenhar_inicio()

        cores = [
            "blue", "green", "orange",
            "purple", "red", "cyan"
        ]

        n = self.n_discos

        for pino in range(3):

            for nivel, disco in enumerate(self.pinos[pino]):

                largura = 30 + disco * (100 / n)
                x = self.centros[pino]
                y = 280 - nivel * 25

                self.canvas.create_rectangle(
                    x - largura / 2,
                    y - 10,
                    x + largura / 2,
                    y + 10,
                    fill=cores[(disco - 1) % len(cores)]
                )

                self.canvas.create_text(
                    x, y,
                    text=str(disco),
                    fill="white"
                )

    def iniciar_hanoi(self):

        try:
            n = int(self.numero_hanoi.get())

            if not 1 <= n <= 6:
                raise ValueError("Use entre 1 e 6 discos.")

            self.n_discos = n

            self.movimentos = torre_hanoi(n)

            self.pinos = [
                list(range(n, 0, -1)),
                [],
                []
            ]

            self.indice = 0

            self.desenhar_discos()

            self.status_hanoi.config(
                text=f"0/{len(self.movimentos)} movimentos"
            )

            self.janela.after(500, self.animar_hanoi)

        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def animar_hanoi(self):

        if self.indice >= len(self.movimentos):

            self.status_hanoi.config(
                text=f"Concluído! {2 ** self.n_discos - 1} movimentos."
            )

            return

        disco, origem, destino = self.movimentos[self.indice]

        mapa = {"A": 0, "B": 1, "C": 2}

        self.pinos[mapa[origem]].pop()
        self.pinos[mapa[destino]].append(disco)

        self.indice += 1

        self.desenhar_discos()

        self.status_hanoi.config(
            text=f"Movimento {self.indice}/{len(self.movimentos)}: "
                 f"disco {disco}, {origem} -> {destino}"
        )

        self.janela.after(650, self.animar_hanoi)

    # ------------------------------------------------
    # ABA 5 - FRACTAL
    # ------------------------------------------------

    def criar_aba_fractal(self):

        aba = ttk.Frame(self.abas, padding=15)
        self.abas.add(aba, text="Árvore fractal")

        ttk.Label(
            aba,
            text="Desafio extra: árvore fractal",
            font=("Arial", 15, "bold")
        ).pack(pady=10)

        ttk.Button(
            aba,
            text="Desenhar árvore",
            command=self.desenhar_fractal
        ).pack(pady=10)

    def desenhar_fractal(self):

        tela = turtle.Screen()
        tela.title("Árvore Fractal")

        caneta = turtle.Turtle()
        caneta.speed(0)
        caneta.color("green")
        caneta.left(90)

        caneta.penup()
        caneta.goto(0, -250)
        caneta.pendown()

        def galho(tamanho, nivel):

            if nivel == 0 or tamanho < 5:
                return

            caneta.pensize(max(1, nivel))
            caneta.forward(tamanho)

            caneta.right(30)
            galho(tamanho * 0.7, nivel - 1)

            caneta.left(60)
            galho(tamanho * 0.7, nivel - 1)

            caneta.right(30)
            caneta.backward(tamanho)

        galho(100, 9)

        caneta.hideturtle()
        tela.mainloop()


# ==================================================
# 4. INICIALIZAÇÃO
# ==================================================

if __name__ == "__main__":

    try:
        executar_testes()
        print("Todos os testes passaram!")

        janela = tk.Tk()
        app = ProjetoRecursao(janela)
        janela.mainloop()

    except AssertionError:
        print("Erro: algum teste dos algoritmos falhou.")

    except tk.TclError as erro:
        print("Não foi possível abrir a interface gráfica:", erro)
