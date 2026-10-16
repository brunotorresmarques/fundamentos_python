# Fundamentos em Python

Repositório com exemplos e exercícios introdutórios para aprender os fundamentos da linguagem Python. O conteúdo está organizado em uma sequência de arquivos `.py` e notebooks Jupyter, com demonstrações curtas que podem ser executadas e modificadas durante os estudos.

## Conteúdo

| Arquivo | Tópicos |
| --- | --- |
| [`01 - helloworld.py`](<01 - helloworld.py>) | Primeiro programa: `Hello World` |
| [`01 - introducao.ipynb`](<01 - introducao.ipynb>) | Introdução ao Python e execução de um primeiro código |
| [`02 - variaveis_python.ipynb`](<02 - variaveis_python.ipynb>) | Variáveis, tipos primitivos, nomes, conversões e entrada de dados |
| [`03 - Operadores.ipynb`](<03 - Operadores.ipynb>) | Conversão de valores e operações aritméticas |
| [`04 - listas.ipynb`](<04 - listas.ipynb>) | Criação, acesso e manipulação de listas |
| [`05 - condicionais.py`](<05 - condicionais.py>) | Decisões com `if` e `else` |
| [`06 - for.py`](<06 - for.py>) | Laços `for`, `range`, `enumerate` e iteração em dicionários |
| [`07 - while.py`](<07 - while.py>) | Laços `while` e encerramento com `break` |
| [`08 - funcoes.py`](<08 - funcoes.py>) | Funções, argumentos, valores padrão, retorno e recursividade |
| [`09 - args e kwargs.py`](<09 - args e kwargs.py>) | Argumentos variáveis com `*args` e `**kwargs` |
| [`10 - funcao lambda.py`](<10 - funcao lambda.py>) | Funções lambda, `filter` e ordenação com `sorted` |

## Como usar

1. Instale o [Python 3](https://www.python.org/downloads/).
2. Clone este repositório ou baixe seus arquivos.
3. Execute um exemplo no terminal:

   ```bash
   python "05 - condicionais.py"
   ```

   Substitua o nome do arquivo pelo exemplo que deseja executar. Alguns programas solicitam dados pelo terminal.

### Notebooks

Os arquivos `.ipynb` podem ser abertos no Jupyter Notebook, JupyterLab ou em uma ferramenta compatível, como o Visual Studio Code com suporte a notebooks. Execute as células em ordem para acompanhar os exemplos.

### Dependências

O arquivo [`requirements.txt`](requirements.txt) registra versões específicas de pacotes Python para configurar o ambiente do repositório. Para instalá-los em um ambiente virtual, use:

```bash
python -m venv .venv
```

Ative o ambiente virtual e instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Os exemplos introdutórios em arquivos `.py` usam recursos da biblioteca padrão do Python.
