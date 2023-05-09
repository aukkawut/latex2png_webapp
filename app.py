from flask import Flask, request, render_template
from latex_converter import latex_to_png
import os
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_data = None
    if request.method == 'POST':
        latex_code = request.form.get('latex_code', '')
        text_color = request.form.get('text_color', 'black')
        font_size = int(request.form.get('font_size', 12))
        dpi = int(request.form.get('dpi', 300))
        output_filename = 'output.png'

        latex_to_png(latex_code, output_filename, text_color, font_size, dpi)

        with open(output_filename, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')

        os.remove(output_filename)

    return render_template('index.html', image_data=image_data)

if __name__ == '__main__':
    app.run()
