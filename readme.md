# Zero de Função e Aplicações: Métodos Numéricos com `scipy.optimize`

Este repositório contém um script Python que demonstra a aplicação de métodos numéricos para encontrar raízes de funções reais, utilizando exclusivamente as funcionalidades otimizadas da biblioteca `scipy.optimize`. O foco é na praticidade e robustez que as ferramentas de alto nível oferecem para problemas de cálculo numérico.

---

## O que o Código Faz

O script `root-finding.py` explora o conceito de "zero de função" (ou raiz da função), que é o valor de `x` para o qual `f(x) = 0`. Ele utiliza as seguintes funções da biblioteca `scipy.optimize`:

* **`scipy.optimize.bisect`**: Implementa o Método da Bissecção, um algoritmo robusto e garantido para encontrar raízes em um intervalo definido.
* **`scipy.optimize.newton`**: Pode se comportar como o Método de Newton-Raphson (se a derivada for fornecida) ou o Método da Secante (sem derivada ou com dois chutes iniciais).
* **`scipy.optimize.fsolve`**: Uma ferramenta mais genérica e poderosa, capaz de resolver sistemas de equações não lineares, mas também adequada para encontrar a raiz de uma única função.

O código também inclui:

* **Tratamento de Erros**: Blocos `try-except` individuais para cada chamada de método, garantindo que o script continue a execução e reporte erros específicos sem interrupções.
* **Visualização Gráfica**: Utiliza `matplotlib` para plotar a função e a raiz encontrada.

---

## Como Rodar o Código (Windows)

### 1. Pré-requisitos

Certifique-se de ter o Python instalado. Se não tiver, baixe e instale do [site oficial do Python](https://www.python.org). Recomenda-se a versão 3.8 ou superior.

### 2. Instalar as Bibliotecas Necessárias

Abra o Prompt de Comando ou o terminal do VS Code e execute:

```bash
python -m pip install --upgrade pip
pip install numpy scipy matplotlib
```

### 3. Baixar o Código

Clone este repositório ou baixe o arquivo `root-finding.py` para uma pasta local, por exemplo:
`C:\MeusProjetos\CalculoNumerico`.

### 4. Rodar o Script

#### Opção A: Rodar no VS Code

1. Abra o VS Code.
2. Vá em **File > Open Folder...** e selecione a pasta.
3. Abra o arquivo `root-finding.py`.
4. Clique com o botão direito no código e selecione **Run Python File in Terminal**, ou use o atalho `Ctrl+Alt+N` (com Code Runner instalado).

#### Opção B: Rodar no Terminal

1. Abra o Prompt de Comando.
2. Navegue até a pasta com o script:

```bash
cd C:\MeusProjetos\CalculoNumerico
```

3. Execute o script:

```bash
python root-finding.py
```

---

## Cenários de Teste e Saídas Esperadas

A função usada nos testes é `f(x) = x³ - x - 2`, cuja raiz real é aproximadamente `1.521380`.

---

### Cenário 1: Convergência Padrão (Todos os Métodos Funcionam)

Valores para digitar no terminal:

```
Digite o valor de 'a' (início do intervalo para Bissecção): 1
Digite o valor de 'b' (fim do intervalo para Bissecção): 2
Digite o chute inicial 'x0' para Newton-Raphson e fsolve: 1.5
Digite o segundo chute 'x1' para o Método da Secante (via newton): 2
```

Saída Esperada:

```
--- Zero de Função e Aplicações (Apenas Métodos Automatizados) ---
Função em análise: f(x) = x³ - x - 2

--- Demonstração: Métodos Automatizados (scipy.optimize) ---

[Método da Bissecção - scipy.optimize.bisect]
  Raiz encontrada: 1.521380

[Método de Newton-Raphson - scipy.optimize.newton com fprime]
  Raiz encontrada: 1.521380

[Método da Secante - scipy.optimize.newton (sem fprime)]
  Raiz encontrada: 1.521380

[Método fsolve - scipy.optimize.fsolve]
  Raiz encontrada: 1.521380

Gráfico geral da função para visualização (intervalo padrão):
(Quatro gráficos serão exibidos para as raízes encontradas e um gráfico geral da função.)
```

---

### Cenário 2: Intervalo Inválido para Bissecção (bisect deve falhar)

Valores para digitar no terminal:

```
Digite o valor de 'a' (início do intervalo para Bissecção): 0
Digite o valor de 'b' (fim do intervalo para Bissecção): 0.5
Digite o chute inicial 'x0' para Newton-Raphson e fsolve: 1.5
Digite o segundo chute 'x1' para o Método da Secante (via newton): 2
```

Saída Esperada:

```
--- Zero de Função e Aplicações (Apenas Métodos Automatizados) ---
Função em análise: f(x) = x³ - x - 2

--- Demonstração: Métodos Automatizados (scipy.optimize) ---

[Método da Bissecção - scipy.optimize.bisect]
  Erro: Falha na Bissecção. f(a) and f(b) must have different signs

[Método de Newton-Raphson - scipy.optimize.newton com fprime]
  Raiz encontrada: 1.521380

[Método da Secante - scipy.optimize.newton (sem fprime)]
  Raiz encontrada: 1.521380

[Método fsolve - scipy.optimize.fsolve]
  Raiz encontrada: 1.521380

Gráfico geral da função para visualização (intervalo padrão):
(Três gráficos serão exibidos para as raízes encontradas e um gráfico geral da função.)
```

---

### Cenário 3: Chute Inicial Problemático para Newton-Raphson e fsolve

Valores para digitar no terminal:

```
Digite o valor de 'a' (início do intervalo para Bissecção): 1
Digite o valor de 'b' (fim do intervalo para Bissecção): 2
Digite o chute inicial 'x0' para Newton-Raphson e fsolve: 0.577
Digite o segundo chute 'x1' para o Método da Secante (via newton): 2
```

Saída Esperada:

```
--- Zero de Função e Aplicações (Apenas Métodos Automatizados) ---
Função em análise: f(x) = x³ - x - 2

--- Demonstração: Métodos Automatizados (scipy.optimize) ---

[Método da Bissecção - scipy.optimize.bisect]
  Raiz encontrada: 1.521380

[Método de Newton-Raphson - scipy.optimize.newton com fprime]
  Erro: Falha na convergência do Newton-Raphson. Failed to converge after 50 iterations, value is -1.5478637351847992.

[Método da Secante - scipy.optimize.newton (sem fprime)]
  Raiz encontrada: 1.521380

[Método fsolve - scipy.optimize.fsolve]
<SeuArquivo>/root-finding.py:125: RuntimeWarning: The iteration is not making good progress...
  Raiz encontrada: 0.571277

Gráfico geral da função para visualização (intervalo padrão):
(Três gráficos serão exibidos para as raízes encontradas e um gráfico geral da função. O gráfico para fsolve mostrará a raiz em 0.571277.)
```

---

### Cenário 4: Chutes Iniciais Muito Próximos para a Secante (newton sem fprime pode falhar)

Valores para digitar no terminal:

```
Digite o valor de 'a' (início do intervalo para Bissecção): 1
Digite o valor de 'b' (fim do intervalo para Bissecção): 2
Digite o chute inicial 'x0' para Newton-Raphson e fsolve: 1.5
Digite o segundo chute 'x1' para o Método da Secante (via newton): 1.5000000000000001
```

Saída Esperada:

```
--- Zero de Função e Aplicações (Apenas Métodos Automatizados) ---
Função em análise: f(x) = x³ - x - 2

--- Demonstração: Métodos Automatizados (scipy.optimize) ---

[Método da Bissecção - scipy.optimize.bisect]
  Raiz encontrada: 1.521380

[Método de Newton-Raphson - scipy.optimize.newton com fprime]
  Raiz encontrada: 1.521380

[Método da Secante - scipy.optimize.newton (sem fprime)]
  Erro de valor na Secante: x1 and x0 must be different

[Método fsolve - scipy.optimize.fsolve]
  Raiz encontrada: 1.521380

Gráfico geral da função para visualização (intervalo padrão):
(Três gráficos serão exibidos para as raízes encontradas e um gráfico geral da função.)
```

## Link para Apresentação

Você pode acessar a apresentação associada a este projeto pelo link abaixo:

🔗 [Apresentação do Projeto - Zero de Função e Métodos Numéricos](https://gamma.app/docs/Metodos-Numericos-para-Busca-de-Raizes-ugteo5lc4q1giur)

---

Ao executar esses cenários, você poderá observar a robustez das funções da `scipy.optimize` e como o tratamento de erros individualizado permite que o programa continue mesmo em caso de falha de um método específico.
