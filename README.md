# Luna AI - Assistente de Voz

Luna AI é uma assistente virtual desenvolvida para interagir com usuários através de comandos de voz. Inspirada por assistentes populares como Alexa, a Luna AI pode realizar uma série de tarefas, incluindo responder perguntas, informar a hora e tocar músicas diretamente do YouTube. O projeto foi desenvolvido como parte do curso Técnico em Informática do Senac Aparecida de Goiânia.

## Funcionalidades

- **Reconhecimento de voz**: Converte comandos de voz em texto usando a biblioteca `SpeechRecognition`.
- **Síntese de fala**: Converte texto em fala, permitindo que Luna responda de forma natural usando `Pyttsx3`.
- **Tocar músicas no YouTube**: Usa a biblioteca `PyWhatKit` para tocar músicas solicitadas pelos usuários.
- **Respostas rápidas**: Pode responder perguntas simples como "Quem foi [pessoa]?" através da integração com a Wikipedia.

## Tecnologias Utilizadas

- **[Flask](https://flask.palletsprojects.com/)** - Microframework usado para hospedar a aplicação web.
- **[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)** - Biblioteca Python para reconhecimento de voz.
- **[Pyttsx3](https://pypi.org/project/pyttsx3/)** - Biblioteca Python para conversão de texto em fala.
- **[PyWhatKit](https://pypi.org/project/pywhatkit/)** - Biblioteca para tocar músicas no YouTube com base em comandos de voz.
- **HTML/CSS** - Interface web para interação com o usuário.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.6 ou superior
- Pip para gerenciamento de pacotes

### Passos para executar o projeto:

1. Clone o repositório:

    ```bash
    git clone https://github.com/caiocrv/LunaAI.git
    cd LunaAI
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

    - Para Linux/macOS:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - Para Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o servidor Flask:

    ```bash
    python luna.py
    ```

5. Acesse a interface web no navegador:

    ```plaintext
    https://localhost:5000
    ```

## Estrutura do Projeto

- **luna.py**: Arquivo principal que executa a lógica do assistente de voz.
- **index.html**: Página HTML que contém a interface de usuário.
- **requirements.txt**: Lista de dependências do projeto.

## Possíveis Atualizações Futuras

- **Multilinguismo**: Adicionar suporte a múltiplos idiomas.
- **Integração com outros serviços**: Incorporar integração com APIs externas para funcionalidades adicionais.
- **Aprendizado de Máquina**: Melhorar o reconhecimento de voz e geração de respostas usando modelos de aprendizado de máquina.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um [issue](https://github.com/caiocrv/LunaAI/issues) ou enviar um pull request.
