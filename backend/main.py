from flask import Flask, jsonify

app = Flask("moregoat")

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(debug=True)

