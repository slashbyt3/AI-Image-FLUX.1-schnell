import os
import time
from huggingface_hub import InferenceClient

HF_TOKEN = "paste_your_huggingface_token_here"
client = InferenceClient("black-forest-labs/FLUX.1-schnell", token=HF_TOKEN)

# STYLE ANCHORS - Ensures visual continuity
STYLE = "Cinematic, photorealistic, 8k, true-crime documentary, 35mm film grain, moody blue and red lighting."
ARTHUR = "45-year-old Chinese man, exhausted, wire-rimmed glasses, blue corporate shirt, black lanyard."
HACKER = "19-year-old Russian male, pale, sharp jawline, messy blonde curls, black oversized hoodie."

# 40-SHOT EXPANDED LIST
shots = {
    # CHAPTER 1
    "ch1_01.png": f"Wide shot. {ARTHUR} walking down a dark blue server room aisle.",
    "ch1_02.png": f"Close up. {ARTHUR} staring at scrolling code reflecting in his glasses.",
    "ch1_03.png": "Macro. Fingers typing rapidly on a glowing backlit keyboard.",
    "ch1_04.png": "Macro. A metal YubiKey hanging from a black lanyard on a desk.",
    "ch1_05.png": "Close up. A smartphone displaying a 2FA spinning timer in the dark.",
    "ch1_06.png": "Exterior. A glass skyscraper at night with glowing blue windows.",
    "ch1_07.png": f"Medium shot. {ARTHUR} rubbing his eyes in an empty office at 2AM.",
    "ch1_08.png": "Close up. A hand clicking a mouse showing a 'Secure' padlock icon.",
    # CHAPTER 2
    "ch2_01.png": f"Medium shot. {HACKER} in a dark room staring at a bright laptop.",
    "ch2_02.png": "POV monitor. A mouse clicking on Arthur's blurry LinkedIn photo.",
    "ch2_03.png": "Graphic. A neon purple spiderweb overlaid on a dark world map.",
    "ch2_04.png": "Wide. A messy room with empty cans and multiple glowing monitors.",
    "ch2_05.png": "Macro. Scrolling through a corporate org chart on a dark screen.",
    "ch2_06.png": "A grainy candid photo of Arthur and coworkers in a breakroom.",
    "ch2_07.png": "A dark wall with sticky notes and red string connecting photos.",
    "ch2_08.png": "Close up. A hand holding a flashlight over a printed company directory.",
    # CHAPTER 3
    "ch3_01.png": "Macro. A smartphone screen showing 'INCOMING CALL' in the dark.",
    "ch3_02.png": f"Close up. {HACKER} speaking into a headset with a calm smirk.",
    "ch3_03.png": "Graphic. A red digital audio waveform pulsing on a black screen.",
    "ch3_04.png": "Macro. A fake corporate ID badge lying next to a keyboard.",
    "ch3_05.png": "Wide. A brightly lit IT helpdesk with a stressed worker in a headset.",
    "ch3_06.png": "Close up. Helpdesk worker's hands typing frantically on a keyboard.",
    "ch3_07.png": "POV monitor. A progress bar reaching 100% with 'ACCESS GRANTED'.",
    "ch3_08.png": f"Medium. {HACKER} leaning back, illuminated by the screen, victory.",
    # CHAPTER 4
    "ch4_01.png": "Macro. A phone on a nightstand vibrating violently in the dark.",
    "ch4_02.png": "Close up. 50 overlapping push notifications on a phone screen.",
    "ch4_03.png": f"Medium. {ARTHUR} sitting up in bed, looking stressed by his phone.",
    "ch4_04.png": "Slow motion macro. A thumb pressing 'Approve' on a phone screen.",
    "ch4_05.png": "POV monitor. A terminal window typing 'creating shadow_admin'.",
    "ch4_06.png": "Close up. A black USB drive being inserted into a server port.",
    "ch4_07.png": "Graphic. A digital tree of AWS accounts being highlighted in red.",
    "ch4_08.png": f"Macro. {HACKER}'s eyes reflecting hundreds of terminal windows.",
    # CHAPTER 5
    "ch5_01.png": "Wide. An empty corporate hallway with flickering red emergency lights.",
    "ch5_02.png": "Wide. A server room where every rack is blinking red 'ERROR'.",
    "ch5_03.png": "POV monitor. A black screen with a red cat logo: 'RANSOMWARE'.",
    "ch5_04.png": "Wide. A Las Vegas casino floor with every screen turned pitch black.",
    "ch5_05.png": "Close up. A hand swiping a hotel keycard that flashes red 'DENIED'.",
    "ch5_06.png": "Macro. A digital counter showing 'Losses: $100,000,000'.",
    "ch5_07.png": f"Wide. Silhouette of {ARTHUR} looking out a window at a dark city.",
    "ch5_08.png": f"Close up profile. {ARTHUR} looking down in absolute defeat.",
    "Thumbnail1.png": f"Cinematic YouTube thumbnail, true-crime documentary style. A devastated IT administrator holding his head in his hands in front of a dark, blinking red server rack. Above him, massive, bold, glowing white and red typography that reads exactly '100M MISTAKE'. High contrast, moody neon red and blue lighting, 35mm film grain, photorealistic, 8k.",
    "Thumbnail2.png": f"Cinematic YouTube thumbnail, true-crime documentary style. A pale 19-year-old hacker in a dark hoodie looking directly at the camera with a sinister, confident smirk, illuminated by harsh blue screen light. Next to him, huge bold red typography that reads exactly 'YOU ARE NEXT'. Photorealistic, 8k, dramatic lighting, high tension, heavy vignette.",
    "Thumbnail3.png": f"Cinematic YouTube thumbnail, true-crime documentary style. A dark, completely blacked-out Las Vegas casino floor. In the foreground, a single glowing slot machine screen displaying a bright red warning symbol. Across the top, massive, bold, glowing neon text reading exactly 'VEGAS HACKED'. Photorealistic, 35mm film grain, highly engaging, dark shadows."
}

def generate_images():
    print("📸 Starting Image Batch with Auto-Retry (Widescreen Mode)...")
    
    for filename, prompt in shots.items():
        # 1. Skip if already exists (Continuity Protection)
        if os.path.exists(filename):
            continue
            
        success = False
        while not success:
            try:
                print(f"🚀 Attempting: {filename}")
                # ADDED width and height to fix the 'broadened' look
                img = client.text_to_image(f"{prompt} {STYLE}", width=1344, height=768)
                img.save(filename)
                print(f"✅ Success! Saved {filename}")
                success = True
                time.sleep(5) 
            except Exception as e:
                if "402" in str(e) or "429" in str(e):
                    print(f"⏳ Rate limit hit at {filename}. Waiting 15 minutes to refresh credits...")
                    time.sleep(900) 
                else:
                    print(f"❌ Permanent Error: {e}")
                    break

if __name__ == "__main__":
    generate_images()
