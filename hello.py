from flask import Flask

app = Flask(__name__)

def wrap_html(message):
    html = """
        <html>
        <body>
            <div style='font-size:80px;'>
            <center>
                <image width="531" src="https://files.realpython.com/media/The-Python-Print-Function_Watermarked.26066d64ad82.jpg">
                <br>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def hello_world():
    message = 'Hello Py!'
    html = wrap_html(message)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)