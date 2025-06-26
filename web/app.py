from flask import Flask, request, render_template, jsonify
import os
import json

app = Flask(__name__)
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'Data')


def find_item_data(item_id):
    results = []
    for filename in os.listdir(DATA_DIR):
        if not filename.endswith('.json'):
            continue
        file_path = os.path.join(DATA_DIR, filename)
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            for entry in data:
                if entry.get('item_id') == item_id:
                    results.append(entry)
        except Exception:
            continue
    return results


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    item_id = request.form.get('item_id', '')
    results = find_item_data(item_id)
    return render_template('result.html', item_id=item_id, results=results)


@app.route('/item/<item_id>')
def api_item(item_id):
    results = find_item_data(item_id)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
