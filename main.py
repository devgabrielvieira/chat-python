from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["DEBUG"] = False  # Desligue o modo de depuração no ambiente de produção
app.config["SECRET_KEY"] = "ajuiahfa78fh9f78shfs768fgs7f6"  # Defina uma chave secreta adequada

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # socketio.run(app)  # Remova a chamada para socketio.run(), pois o Gunicorn irá gerenciar o servidor agora
