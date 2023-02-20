from flask import Flask , render_template

app = Flask(__name__)
@app.route("/") # @app.route("/網站根目錄")
def hello():
    return render_template('index.html') #開始運行：flask run

if __name__ == '__main__' :
    app.run()