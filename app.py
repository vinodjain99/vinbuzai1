from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get("prompt", "lofi chillhop")
    # simulate music generation
    return jsonify({"status": "success", "message": f"Music generated for prompt: {prompt}"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
