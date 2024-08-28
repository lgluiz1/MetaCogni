from flask import Flask
from flask import request, render_template

app = Flask(__name__)
contador = 0

@app.route('/')
def index():
    return render_template('gerado_whats.html')
@app.route('/submit', methods=['POST'])
def submit():
    global contador
    contador += 1
    ddd = request.form.get('ddd')
    telefone = request.form.get('telefone')
    mensagem = request.form.get('mensagem')
    email = request.form.get('email')
    print(f'{ddd} {telefone} {mensagem} {email}')
    
    numero_completo = f"{ddd}{telefone}"
    mensagem_formatada = mensagem.replace(' ', '%20')
    link_whatsapp = f"https://api.whatsapp.com/send?phone=55{numero_completo}&text={mensagem_formatada}"
    
    # Renderiza o layout da página gerado_whats_gerado com o link gerado
    return render_template('gerado_whats_gerado.html', link_whatsapp=link_whatsapp)


if __name__ == '__main__':
    app.run(debug=True)
