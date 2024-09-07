from flask import Flask, request, render_template, send_file
from markupsafe import Markup
import json
import qrcode
from comand import YouTubeDownloader, gerado_whatsapp
from static.termos.__init__ import termos_politica_html
import os
import time
import threading

app = Flask(__name__)
textos = gerado_whatsapp().get_textos()
empresa = textos['nomeSite']

def load_contador():
    try:
        with open('contadores.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

contador = load_contador()

def apagar_apos_tempo(filepath, tempo):
    print(f"Iniciando contagem para remover o arquivo {filepath} após {tempo / 60} minutos.")
    time.sleep(tempo)
    
    if os.path.exists(filepath):
        try:
            os.remove(filepath)
            print(f"Arquivo {filepath} removido com sucesso.")
        except Exception as e:
            print(f"Erro ao remover o arquivo {filepath}: {e}")
    else:
        print(f"O arquivo {filepath} não foi encontrado.")

@app.route('/')
def index():
    global contador
    contador = load_contador()
    contador_valor = f'A {empresa} já gerou mais de {contador} links'
    return render_template('./gerado_whatsapp/gerado_whats.html', contador_valor=contador_valor, empresa=empresa, **textos)

@app.route('/submit', methods=['POST'])
def submit():
    global contador
    contador += 1
    telefone = request.form.get('telefone')
    mensagem = request.form.get('mensagem')
    email = request.form.get('email')
    
    print(f'Telefone: {telefone}')
    print(f'Mensagem: {mensagem}')
    print(f'E-mail: {email}')
    print(f'Contador: {contador}')
    
    numero_completo = telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    mensagem_formatada = mensagem.replace(' ', '%20')
    
    link_whatsapp = f"https://api.whatsapp.com/send?phone=55{numero_completo}&text={mensagem_formatada}"
    
    with open('contadores.json', 'w') as f:
        json.dump(contador, f)
    
    try:
        if email:
            link_whatsapp = f"https://api.whatsapp.com/send?phone=55{numero_completo}&text={mensagem_formatada}&email={email}"

            img_qrcode = qrcode.make(link_whatsapp)
            img_path = f'./static/img/arquivos_temporarios/{numero_completo}.png'
            print(f"Salvando QR Code em: {img_path}")
            img_qrcode.save(img_path)

            # QR Code é salvo, mas a contagem para remoção será iniciada apenas quando o botão for clicado
            return render_template('./gerado_whatsapp/whats_qrcode.html', link_whatsapp=link_whatsapp, telefone=numero_completo, empresa=empresa)
        
        return render_template('./gerado_whatsapp/gerado_whats_gerado.html', link_whatsapp=link_whatsapp, telefone=numero_completo, empresa=empresa)
    
    except Exception as e:
        print(f"Erro ao gerar o QR Code ou link: {e}")
        return render_template('./gerado_whatsapp/error.html', error_message="Ocorreu um erro ao gerar o link ou QR Code.")

@app.route('/start_timer', methods=['POST'])
def start_timer():
    numero_completo = request.form.get('numero_completo')
    img_path = f'./static/img/arquivos_temporarios/{numero_completo}.png'

    if numero_completo:
        threading.Thread(target=apagar_apos_tempo, args=(img_path, 120)).start()  # Exemplo de 2 minutos (120 segundos)
        return {"status": "Contagem iniciada", "tempo": 120}
    else:
        return {"status": "Erro", "message": "Número de telefone não fornecido"}, 400

@app.route('/ytdownload', methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        video_url = request.form.get('video_url', '')
        try:
            filepath = YouTubeDownloader.download_video(video_url)
            return send_file(filepath, as_attachment=True)
        except Exception as e:
            print(f"Erro ao baixar o vídeo: {e}")
            return render_template('./youtubedownloader/downloadvideo.html', error="Não foi possível baixar o vídeo.")
    return render_template('./youtubedownloader/youtubedownloader.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', empresa=empresa, **textos)

@app.route('/inovacao')
def inovacao():
    return render_template('inovacao.html', empresa=empresa)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response_message = "Estou aqui para ajudar!"
    return {'response': response_message}

@app.route('/mensagem')
def mensagem():
    return render_template('chat.html', empresa=empresa)

@app.route('/termos')
def termos():
    termos_politica_html_markup = Markup(termos_politica_html)
    return render_template('termos.html', empresa=empresa, termos_politica_html=termos_politica_html_markup)
