# AI Image – FLUX.1‑schnell

**Generate a cohesive cinematic storyboard** – This script uses the FLUX.1‑schnell model to create a series of 40+ widescreen (1344×768) images, following a true‑crime documentary narrative. Outputs are ready for video editing or presentations.

![Example output](docs/thumbnail_sample.png)  
<img width="1344" height="768" alt="ch5_04" src="https://github.com/user-attachments/assets/942514e6-4c5d-4f0f-8dab-99b1b9e220e4" />
<img width="1344" height="768" alt="ch4_07" src="https://github.com/user-attachments/assets/32d491ae-f2fb-45f8-8cd4-4aa514bc657f" />
<img width="1344" height="768" alt="ch1_07" src="https://github.com/user-attachments/assets/a69d81c5-1781-45bc-9058-010c053648dd" />
<img width="1344" height="768" alt="ch5_08" src="https://github.com/user-attachments/assets/8c11bc9d-ec06-462d-b95d-c6200181c5af" />
<img width="1344" height="768" alt="ch3_05" src="https://github.com/user-attachments/assets/34dfe08a-9ebe-441a-b665-6c9d9e6419ec" />



## ✨ Features
- **Consistent style anchors** – character descriptions and mood presets (e.g., “cinematic, photorealistic, 35mm film grain”).
- **40‑shot story** – organised into 5 chapters (The Fortress, The Recon, The Heist, The Fatigue, The Ashes).
- **Widescreen format** – 1344×768 (ideal for 16:9 video).
- **Auto‑retry & rate‑limit handling** – waits 15 minutes when free tier limits are hit, skips already downloaded images.
- **Customisable prompts** – easily swap characters, scenes, or entire story.

## 📦 Requirements

- Python 3.8+
- A [Hugging Face account](https://huggingface.co/join) (free)
- A Hugging Face **access token** (see below)

## 🔑 Get a Hugging Face token
Sign up / log in at huggingface.co

`1.` **Go to Settings → Access Tokens**

`2.` **Click New token, select read (or write if you prefer), copy the token.**

`3.` **Do NOT hardcode the token in the script. Use environment variables.**

### Python packages

Install with pip:

```bash
pip install huggingface-hub Pillow
