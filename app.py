from flask import Flask, request, render_template , send_file
import json
from comand import YouTubeDownloader ,nome_do_site

app = Flask(__name__)
empresa = nome_do_site
# Carrega o contador do arquivo JSON
def load_contador():
    try:
        with open('contadores.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0  # Define o contador como 0 se o arquivo não for encontrado ou estiver vazio

contador = load_contador()

@app.route('/')
def index():
    global contador
    contador = load_contador()
    contador_valor = f'A {empresa} ja gerou mais de {contador} links'
    return render_template('./gerado_whatsapp/gerado_whats.html' , contador_valor=contador_valor , empresa=empresa)

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
    
    # Formata o número de telefone e a mensagem
    numero_completo = telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    mensagem_formatada = mensagem.replace(' ', '%20')
    
    link_whatsapp = f"https://api.whatsapp.com/send?phone=55{numero_completo}&text={mensagem_formatada}"
    
    # Atualiza o contador no arquivo JSON
    with open('contadores.json', 'w') as f:
        json.dump(contador, f)
    
    # Renderiza a página com o link gerado
    return render_template('./gerado_whatsapp/gerado_whats_gerado.html', link_whatsapp=link_whatsapp , empresa=empresa)


## YoutubeDownloader
@app.route('/ytdownload', methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        video_url = request.form.get('video_url', '')
        try:
            # Baixa o vídeo no servidor
            filepath = YouTubeDownloader.download_video(video_url)
            # Envia o vídeo baixado ao cliente            return send_file(filepath, as_attachment=True)
        except Exception as e:
            print(f"Erro ao baixar o vídeo: {e}")
            return render_template('./youtubedownloader/downloadvideo.html', error="Não foi possível baixar o vídeo.")
    return render_template('./youtubedownloader/youtubedownloader.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html' , empresa=empresa)

@app.route('/inovacao')
def inovacao():
    return render_template('inovacao.html' , empresa=empresa)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response_message = "Estou aqui para ajudar!"
    return {'response': response_message}

@app.route('/mensagem')
def mensagem():
    return render_template('chat.html' , empresa=empresa)