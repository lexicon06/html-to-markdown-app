from flask import Flask, render_template, request, jsonify
from html_to_markdown import convert_to_markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        html = request.form.get('html_content', '')
        try:
            markdown = convert_to_markdown(html)
            return jsonify({'success': True, 'markdown': markdown})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)