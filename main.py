"""Calculadora simples com interface gráfica (Tkinter)."""

import ast
import operator
import tkinter as tk

OPERADORES = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def avaliar(expressao: str) -> float:
    """Avalia uma expressão aritmética de forma segura (sem usar eval)."""

    def _avaliar(no):
        if isinstance(no, ast.Expression):
            return _avaliar(no.body)
        if isinstance(no, ast.Constant) and isinstance(no.value, (int, float)):
            return no.value
        if isinstance(no, ast.BinOp) and type(no.op) in OPERADORES:
            return OPERADORES[type(no.op)](_avaliar(no.left), _avaliar(no.right))
        if isinstance(no, ast.UnaryOp) and type(no.op) in OPERADORES:
            return OPERADORES[type(no.op)](_avaliar(no.operand))
        raise ValueError("Expressão inválida")

    expressao = expressao.replace("×", "*").replace("÷", "/").replace(",", ".")
    return _avaliar(ast.parse(expressao, mode="eval"))


def formatar(valor: float) -> str:
    if isinstance(valor, float) and valor.is_integer():
        valor = int(valor)
    return str(round(valor, 10) if isinstance(valor, float) else valor)


class Calculadora(tk.Tk):
    BOTOES = [
        ["C", "⌫", "%", "÷"],
        ["7", "8", "9", "×"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["±", "0", ".", "="],
    ]

    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.resizable(False, False)
        self.configure(bg="#202020")

        self.expressao = tk.StringVar(value="")
        self.historico = tk.StringVar(value="")

        tk.Label(self, textvariable=self.historico, anchor="e", bg="#202020",
                 fg="#9a9a9a", font=("Segoe UI", 12)).grid(
            row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=(10, 0))
        tk.Label(self, textvariable=self.expressao, anchor="e", bg="#202020",
                 fg="white", font=("Segoe UI", 28, "bold"), width=12).grid(
            row=1, column=0, columnspan=4, sticky="ew", padx=10, pady=(0, 10))

        for i, linha in enumerate(self.BOTOES):
            for j, texto in enumerate(linha):
                if texto == "=":
                    cor = "#4c8bf5"
                elif texto in "÷×-+%":
                    cor = "#3a3a3a"
                elif texto in ("C", "⌫", "±"):
                    cor = "#5a3a3a"
                else:
                    cor = "#2d2d2d"
                tk.Button(self, text=texto, font=("Segoe UI", 16), width=4, height=2,
                          bg=cor, fg="white", activebackground="#555",
                          activeforeground="white", relief="flat", bd=0,
                          command=lambda t=texto: self.clicar(t)).grid(
                    row=i + 2, column=j, padx=3, pady=3, sticky="nsew")

        self.bind("<Key>", self.tecla)
        self.bind("<Return>", lambda e: self.clicar("="))
        self.bind("<KP_Enter>", lambda e: self.clicar("="))
        self.bind("<BackSpace>", lambda e: self.clicar("⌫"))
        self.bind("<Escape>", lambda e: self.clicar("C"))

    def clicar(self, texto: str):
        atual = self.expressao.get()
        if atual == "Erro":
            atual = ""

        if texto == "C":
            self.expressao.set("")
            self.historico.set("")
        elif texto == "⌫":
            self.expressao.set(atual[:-1])
        elif texto == "=":
            if not atual:
                return
            try:
                resultado = formatar(avaliar(atual))
                self.historico.set(atual + " =")
                self.expressao.set(resultado)
            except ZeroDivisionError:
                self.historico.set("Divisão por zero")
                self.expressao.set("Erro")
            except (ValueError, SyntaxError, TypeError, OverflowError):
                self.expressao.set("Erro")
        elif texto == "±":
            if atual.startswith("-(") and atual.endswith(")"):
                self.expressao.set(atual[2:-1])
            elif atual:
                self.expressao.set(f"-({atual})")
        else:
            self.expressao.set(atual + texto)

    def tecla(self, evento):
        mapa = {"*": "×", "/": "÷"}
        caractere = evento.char
        if caractere in "0123456789.+-%()" and caractere:
            self.clicar(caractere)
        elif caractere in mapa:
            self.clicar(mapa[caractere])


if __name__ == "__main__":
    Calculadora().mainloop()
