# 💬 ChatBot com IA em Python (Streamlit)

Chatbot simples e funcional construído **inteiramente em Python**, usando **Streamlit** para o front-end e back-end e a **API da OpenAI (GPT-4o)** como motor de inteligência artificial.

## 📋 Sobre o projeto

O objetivo do projeto é mostrar como é possível criar uma interface de chat completa — com histórico de conversa incluído — usando apenas Python, sem escrever uma linha de HTML, CSS ou JavaScript.

O funcionamento é simples:

1. O usuário digita uma mensagem no campo de chat;
2. A mensagem é exibida na tela e guardada no histórico da conversa (`session_state`);
3. Todo o histórico é enviado para a API da OpenAI, que gera uma resposta com base no contexto da conversa;
4. A resposta da IA é exibida no chat e também adicionada ao histórico, mantendo a continuidade do diálogo.

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — criação da interface web (chat) com Python puro
- [OpenAI API](https://platform.openai.com/) — modelo `gpt-4o` para geração das respostas

## 📁 Estrutura do projeto

```
ChatBot-com-IA-Python-Streamlt/
├── Chatbot.py    # Aplicação principal do chatbot
└── README.md
```

## ⚙️ Como executar

### Pré-requisitos

- Python 3 instalado
- Uma [chave de API da OpenAI](https://platform.openai.com/api-keys)

### Instalação

```bash
pip install streamlit openai
```

### Configuração

Antes de rodar, abra o `Chatbot.py` e substitua pela sua chave de API:

```python
modelo_ia = OpenAI(api_key="Sua_Chave")
```

> ⚠️ **Atenção:** nunca deixe sua chave de API exposta em um repositório público. O ideal é usar variáveis de ambiente ou o recurso de [Secrets do Streamlit](https://docs.streamlit.io/develop/concepts/connections/secrets-management), por exemplo:
> ```python
> import os
> modelo_ia = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
> ```

### Execução

```bash
streamlit run Chatbot.py
```

O Streamlit vai abrir automaticamente uma aba no navegador com a interface do chat.

## 👤 Autor

Desenvolvido por [Victor Eduardo Oliveira](https://github.com/VictorEduardoOliveira).
