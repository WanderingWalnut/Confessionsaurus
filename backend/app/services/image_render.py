from PIL import Image, ImageDraw, ImageFont
import textwrap
import time

def render_confession_on_image(confession_text, bg_path="/Users/naveed/confessionsaurus/backend/assets/Background.jpg", output_path=None, font_path="/Users/naveed/confessionsaurus/backend/assets/fonts/Fredoka-Regular.ttf"):
    if output_path is None:
        timestamp = int(time.time())
        output_path = f"/Users/naveed/confessionsaurus/backend/output/confession_{timestamp}.jpg"
    try:
        img = Image.open(bg_path).convert("RGB")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, size=50)

        wrapped = textwrap.wrap(confession_text, width=40)
        y = 300

        for line in wrapped:
            # Use modern Pillow methods - textbbox returns (left, top, right, bottom)
            bbox = draw.textbbox((0, 0), line, font=font)
            line_width = bbox[2] - bbox[0]  # right - left
            line_height = bbox[3] - bbox[1]  # bottom - top
            x = (img.width - line_width) / 2
            draw.text((x,y), line, font=font, fill="black")
            y += line_height + 20
        
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
