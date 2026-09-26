# Chatbot com IA Generativa

Chatbot conversacional em Python, com interface web feita em Streamlit e respostas geradas pela API da OpenAI (modelo GPT-4o).

## Funcionalidades

- Interface de chat via Streamlit
- Histórico de conversa mantido durante a sessão
- Integração com a API da OpenAI

## Como rodar o projeto

### 1. Clonar o repositório
\`\`\`bash
git clone https://github.com/VictorEduardoOliveira/ChatBot-com-IA-Python-Streamlt.git
cd ChatBot-com-IA-Python-Streamlt
\`\`\`

### 2. Instalar as dependências
\`\`\`bash
pip install streamlit openai python-dotenv
\`\`\`

### 3. Configurar a chave da API
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
\`\`\`
OPENAI_API_KEY=sua_chave_aqui
\`\`\`

> A chave nunca é exposta no código — ela é carregada via variável de ambiente com a biblioteca `python-dotenv`.

### 4. Rodar a aplicação
\`\`\`bash
streamlit run Chatbot.py
\`\`\`

## Tecnologias utilizadas

- Python
- Streamlit
- OpenAI API (GPT-4o)
- python-dotenv

## Autor

Victor Eduardo Oliveira
[LinkedIn](https://www.linkedin.com/in/victor-eduardo75/) | [GitHub](https://github.com/VictorEduardoOliveira)
