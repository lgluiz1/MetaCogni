from flask import Flask, request, render_template
import json

app = Flask(__name__)

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
    contador_valor = f'A MetaCogni ja gerou mais de {contador} links'
    return render_template('gerado_whats.html' , contador_valor=contador_valor)

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
    return render_template('gerado_whats_gerado.html', link_whatsapp=link_whatsapp )

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/inovacao')
def inovacao():
    return render_template('inovacao.html')

