import os
import time
import textwrap
import uuid
from typing import Optional
from PIL import Image, ImageDraw, ImageFont

# If your handler lives in lambda_package/app/main.py, then:
#  __file__                         -> /var/task/app/main.py
#  dirname(__file__)                -> /var/task
#  dirname(dirname(__file__))       -> /var/task   ← bundle root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def render_confession_on_image(
    confession_text: str,
    bg_filename: str   = "Background.jpg",
    font_filename: str = "Fredoka-Regular.ttf",
    output_path: Optional[str] = None,
) -> str:
    """
    Expects on-disk layout under /var/task/ (the Lambda bundle root):
      • assets/Background.jpg
      • assets/fonts/Fredoka-Regular.ttf
      • app/main.py      ← this module
    Writes the result into /tmp/.
    """
    try:
        # Point at the assets folder that sits next to app/
        bg_path   = os.path.join(BASE_DIR, "assets",         bg_filename)
        font_path = os.path.join(BASE_DIR, "assets", "fonts", font_filename)

        # Lambda only lets you write under /tmp. Ensure filename uniqueness.
        if not output_path:
            millis = int(time.time() * 1000)
            unique = uuid.uuid4().hex
            output_path = os.path.join("/tmp", f"confession_{millis}_{unique}.jpg")

        # Pillow logic
        img  = Image.open(bg_path).convert("RGB")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, size=50)

        wrapped = textwrap.wrap(confession_text, width=40)
        y = 300
        for line in wrapped:
            bbox = draw.textbbox((0, 0), line, font=font)
            w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            x    = (img.width - w) / 2
            draw.text((x, y), line, font=font, fill="black")
            y += h + 20

        img.save(output_path)
        return output_path

    except IOError as e:
        print(f"File could not be found or opened: {str(e)}")
    except Image.DecompressionBombError as e:
        print(f"File is too large {str(e)}")
    except Image.UnidentifiedImageError as e:
        print(f"File isn't an image or is corrupted {str(e)}")

if __name__ == "__main__":
    dummy_confession = "Today someone told me they ate a fat burger at this weird place, was soo awkward."
    try:
        out_path = render_confession_on_image(dummy_confession)
        print("Image rendered successfully at:", out_path)
    except Exception as e:
        print("An unexpected error occurred:", e)
