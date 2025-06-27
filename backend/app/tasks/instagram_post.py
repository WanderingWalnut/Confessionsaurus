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

    try:

        confessions = get_ready_confession(db)

        if not confessions:
            print(f"No confessions available")
            return []

        for confession in confessions:
            # TODO: Make sure to update status to POSTED
            update_confession_to_posted(db, confession.id) # Update to posted so it doesn't keep getting re-posted
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                # Pass confession content (string) as input, not the entire confession object
                render_confession_on_image(confession.content, output_path=tmp.name)
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
        # Delete the files
        cleanup_temp_files(files_to_upload)


if __name__ == "__main__":
    post_to_instagram()