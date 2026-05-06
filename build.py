import os
import subprocess
import sys

def build():
    print("Building fonts from UFO sources...")
    sources_dir = "sources"
    out_dir = os.path.join("fonts", "ttf")
    os.makedirs(out_dir, exist_ok=True)
    
    try:
        import ufo2ft
    except ImportError:
        print("Installing ufo2ft...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ufo2ft"])
        import ufo2ft
        
    from defcon import Font
    
    for ufo in os.listdir(sources_dir):
        if ufo.endswith(".ufo"):
            ufo_path = os.path.join(sources_dir, ufo)
            print(f"Compiling {ufo}...")
            font = Font(ufo_path)
            ttf = ufo2ft.compileTTF(font)
            out_path = os.path.join(out_dir, ufo.replace(".ufo", ".ttf"))
            ttf.save(out_path)
            print(f"Saved {out_path}")

if __name__ == "__main__":
    build()
