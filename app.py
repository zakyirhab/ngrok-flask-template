# =[Modules dan Packages]========================
from flask import Flask,render_template
from flask_ngrok import run_with_ngrok

# =[Variabel Global]=============================
app = Flask(__name__, static_url_path='/static')

# =[Routing]=====================================
@app.route("/")
def beranda():
    return render_template('index.html')

# =[Main]========================================
if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()
