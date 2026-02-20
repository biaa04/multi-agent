# Ferramenta de multiagentes para conversão de temperaturas e de metros

Este projeto implementa agentes de IA utilizando LangChain integrado ao Ollama (modelo Llama 3.2) para realizar conversões de temperatura e da unidade de medida metros, o projeto ultiliza a arquitetura supervisor de multiagentes
Conversões realizadas:
- Celsius ↔ Fahrenheit
- Celsius ↔ Kelvin
- KM ↔ M
- M ↔ C

O agente orquestrador solicita que o agente especialista realize a tarefa solicita pelo usuário

## Tecnologias Utilizadas

- LangChain
- Python
- Ollama
- Modelo: Llama3.2

## Como Executar o Projeto

### Instalar o Ollama

Para executar o programa é necessário que você tenha o [Ollama](https://ollama.com/download/windows) instalado em sua máquina para que seja possível usar o modelo de linguagem.

Após instalar, baixe o modelo:
```
ollama pull llama3.2
```

### Criar Ambiente Virtual

```
python -m venv venv
venv\Scripts\activate
```

### Instalar Dependências

Execute:
```
pip install langchain
ollama pull llama3.2
```

### Executar o Projeto

```
python main.py
```

### Autora

Beatriz Andrade

Linkedin : https://www.linkedin.com/in/beatriz-andrade-94b38b233/
