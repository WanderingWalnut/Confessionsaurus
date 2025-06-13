import tempfile
from app.services.image_render import render_confession_on_image
from app.db.session import SessionLocal
from app.db.crud_confession import get_ready_confession
from app.services.instagram_poster import InstagramSessionManager
import os


def render_batch_images():
    db = SessionLocal()
    temp_files = [] # For storing the rendered images

    try:

        confessions = get_ready_confession(db)

        if not confessions:
            print(f"No confessions available")
            return []

        for confession in confessions:
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                # Pass temp file as output path
                render_confession_on_image(confession, output_path=tmp.name)
                temp_files.append(tmp.name) # Store the file path for posting
        
        # Return the list of temp files to be processed for posting
        print(f'Render successful! Here are the list of temp files: {temp_files}')
        return temp_files

    except Exception as e:
        print(f"Failed to render images for confessions: {str(e)}")
    
    finally:
        db.close()


def cleanup_temp_files(file_paths):
    for path in file_paths:
        try:
            os.remove(path)
            print(f"Deleted temp file: {path}")
        except Exception as e:
            print(f"Failed to delete temp file: {str(e)}")
    

def post_to_instagram():
    """ Post carousel to instagram """

    # Init instagram session
    session = InstagramSessionManager()
    
    try:
        files_to_upload = render_batch_images()
        session.post_carousel(files_to_upload)
    
    except Exception as e:
        print(f"Failed to post on instagram: {str(e)}")
        return None

    finally:
        cleanup_temp_files()


if __name__ == "__main__":
    post_to_instagram()