import tempfile
from app.services.image_render import render_confession_on_image
from app.db.session import SessionLocal
from app.db.crud_confession import get_ready_confession, update_confession_to_posted
from app.services.instagram_poster import InstagramSessionManager
import os


# TODO: Integrate caption generation for posting
def render_batch_images():
    """ Create visuals for posts """
    db = SessionLocal()
    temp_files = [] # For storing the rendered images
    confession_text = [] # List of content within confessions for caption generation
    
    try:

        confessions = get_ready_confession(db)

        # TODO: After confessions are posted, when new ones are added they are not picked up

        if not confessions:
            print(f"No confessions available")
            return []

        for confession in confessions:
            confession_text.append(confession.content)
            
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                # Pass confession content (string) as input, not the entire confession object
                output_path = render_confession_on_image(confession.content)
                temp_files.append(output_path) # Store the file path for posting
            
            update_confession_to_posted(db, confession.id) # Update to posted so it doesn't keep getting re-posted
        
        # Return the list of temp files to be processed for posting
        print(f'Render successful! Here are the list of temp files: {temp_files}')
        print(f"List of confession texts created: {confession_text}")
        return temp_files, confession_text

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
        files_to_upload, confessions_text = render_batch_images()
        caption = session.create_caption(confessions_text)
        if caption:
            print(f"Caption created successfully: {caption}")
        else:
            print("Failed to create caption")

        session.post_carousel(files_to_upload, caption)
    
    except Exception as e:
        print(f"Failed to post on instagram: {str(e)}")
        return None

    finally:
        # Delete the files
        cleanup_temp_files(files_to_upload)


if __name__ == "__main__":
    post_to_instagram()