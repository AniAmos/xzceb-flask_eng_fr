from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return translator.englishtofrench(textToTranslate)
    # return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    # textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    print(request)
    textToTranslate = request.args.get('textToTranslate')
    print(textToTranslate)
    return translator.frenchtoenglish(textToTranslate)
    # return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    # content = get_file('templates/index.html')
    # return Response(content, mimetype="text/html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
