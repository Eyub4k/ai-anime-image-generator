from flask import Flask, render_template, request, send_file, jsonify
import torch
from diffusers import StableDiffusionPipeline
from io import BytesIO


app = Flask(__name__, static_folder='static')

# Configuration du modèle
model_id = "hakurei/waifu-diffusion"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialisation du pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)
pipe = pipe.to(device)

# Activer l'attention séquentielle pour économiser la mémoire
pipe.enable_attention_slicing()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        user_prompt = data.get('prompt', '')
        
        # Amélioration du prompt pour de meilleurs résultats anime
        prompt = f"Masterpiece, best quality, highly detailed, anime style, (safe and elegant composition:1.3), (artistic lighting:1.2), (detailed background:1.1), (no nudity, no suggestive content:1.5), {user_prompt}"
        
        # Paramètres de génération optimisés pour waifu-diffusion
        image = pipe(
            prompt,
            num_inference_steps=28,
            guidance_scale=11,
            width=512,
            height=512
        ).images[0]
        
        # Sauvegarde en PNG
        img_io = BytesIO()
        image.save(img_io, 'PNG', quality=95)
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
    
    except Exception as e:
        print(f"Erreur de génération: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)