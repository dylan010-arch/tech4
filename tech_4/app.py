from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        data = request.form

        name = data.get('name')
        age = data.get('age')
        if not name or not age:
            raise ValueError("Не все поля заполнены")
        age = int(age)  # Преобразование возраста в число


        return jsonify({'message': 'Данные успешно отправлены'})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
