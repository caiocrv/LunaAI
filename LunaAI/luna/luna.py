from flask import Flask, request, jsonify, render_template
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

app = Flask(__name__)

audio = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comando', methods=['POST'])
def comando_voz_usuario():
    data = request.json
    comando = data.get('comando', '').lower()
    response = ""

    def falar(texto):
        luna = pyttsx3.init()
        luna.say(texto)
        luna.runAndWait()

    if 'quem é você' in comando:
        identidade = ('Sou uma inteligência artificial desenvolvida por alunos do curso Técnico em Informática do Senac Aparecida de Goiânia. '
                      'Fui criada a partir de um projeto solicitado pelo professor Elivan.')
        response = identidade
        falar(response)

    elif 'o que você pode fazer' in comando or 'o que você faz' in comando or 'o que você é capaz' in comando:
        capacidade = ('Posso te informar que horas são, consigo fazer uma pesquisa e tocar música.')
        response = capacidade
        falar(response)

    elif 'oi luna' in comando:
        saudacao = ('Olá! O que posso fazer por você hoje?')
        response = saudacao
        falar(response)

    elif 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        response = f'Agora são {hora}'
        falar(response)

    elif 'tocar' in comando or 'torre' in comando or 'toque' in comando or 'toca' in comando:
        musica = comando.replace('toque', '').replace('tocar', '').replace('torre', '').replace('toca', '').strip()
        pywhatkit.playonyt(musica)
        response = f'Tocando música'
        falar(response)

    elif any(keyword in comando for keyword in ['procure', 'quem é', 'quando foi', 'procura', 'pesquise', 'pesquisa']):
        wikipedia.set_lang('pt')
        pesquisa = comando.replace('procure', '').replace('quem é', '').replace('quando foi', '').replace('procura', '').replace('pesquise', '').replace('pesquisa', '').strip()
        if pesquisa:
            try:
                resultado = wikipedia.summary(pesquisa, sentences=1)
                response = resultado
                falar(response)
            except wikipedia.exceptions.DisambiguationError as e:
                response = 'Sua pesquisa é ambígua. Por favor, seja mais específico.'
                falar(response)
            except wikipedia.exceptions.PageError:
                response = 'Não encontrei nada relacionado à sua pesquisa.'
                falar(response)
        else:
            response = 'Não entendi sua pesquisa. Por favor, diga novamente.'
    else:
        response = ('Desculpa, isso não está no meu banco de dados.')
        falar(response)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='192.168.100.56', port=500, debug=True, ssl_context=('cert.pem', 'key.pem'))
