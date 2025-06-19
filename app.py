from flask import Flask, request, send_file
from riffusion.pipeline import RiffusionPipeline
import tempfile

app = Flask(__name__)
pipeline = RiffusionPipeline.load_checkpoint()

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get("prompt", "lofi chillhop")
    audio = pipeline.run_txt2audio(prompt=prompt)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.export(temp_file.name, format="wav")
    return send_file(temp_file.name, mimetype="audio/wav")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
