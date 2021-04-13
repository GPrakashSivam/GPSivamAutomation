from flask import Flask, render_template, request, send_file
import CamarillaCalc as calc
import CommonUtility as common

app = Flask(__name__)

@app.route('/') 
def index(): 
    return render_template('index.html') 

@app.route('/camarilla_result', methods = ['POST', 'GET']) 
def camarilla_result(): 
    if request.method == 'POST': 
        calc.GetCamarillaCalc()
        return render_template("download_file.html")

@app.route('/download')
def download_file():
    path = common.exportPDFFileName
    return send_file(path, as_attachment=True)

if __name__ == '__main__': 
    app.run()
