# Calculadora Python

Calculadora simples com interface gráfica feita em Python com Tkinter, toda em um único arquivo (`main.py`).

## Requisitos

- Python 3.8 ou superior
- Tkinter (já incluído na instalação padrão do Python no Windows e no macOS; no Linux pode ser necessário instalar o pacote `python3-tk`)

Nenhuma dependência externa é necessária.

## Como executar

```bash
python main.py
```

## Funcionalidades

- Operações básicas: soma (`+`), subtração (`-`), multiplicação (`×`) e divisão (`÷`)
- Resto da divisão (`%`): `10%3` resulta em `1`
- Inversão de sinal (`±`)
- Apagar o último caractere (`⌫`) e limpar tudo (`C`)
- Respeita a precedência dos operadores: `2+3×4` resulta em `14`
- Mostra a expressão calculada acima do resultado
- Exibe "Erro" em divisões por zero e expressões inválidas

## Atalhos de teclado

| Tecla | Ação |
|---|---|
| `0`–`9`, `.` | Digitar números |
| `+` `-` `*` `/` `%` | Operadores |
| `(` `)` | Parênteses (disponíveis apenas pelo teclado) |
| `Enter` | Calcular (`=`) |
| `Backspace` | Apagar o último caractere |
| `Esc` | Limpar tudo |

## Segurança

As expressões são calculadas com um avaliador próprio baseado no módulo `ast`, sem usar `eval`. Somente números e operadores aritméticos são aceitos.
