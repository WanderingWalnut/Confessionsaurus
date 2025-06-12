from app.services.moderation import moderate_confession
from app.db.session import SessionLocal
from app.db.crud_confession import get_unmoderated_confessions, update_confession_status_ready, update_confession_status_pending


def moderate_all_confessions():
    db = SessionLocal()

    try:
        confessions = get_unmoderated_confessions(db)

        if confessions:
            for confession in confessions:
                print(f"Moderating the following confession: {confession}")
                moderated_confession = moderate_confession(confession.content)
                
                # If the confession is flagged
                if moderated_confession.flagged:
                    update_confession_status_pending(db, confession)
                # If it is not flagged, stage as READY
                else:
                    update_confession_status_ready(db, confession)
        else:
            return []
    
    except Exception as e:
        print(f"Failed to moderate confessions: {str(e)}")
        db.rollback()
        return []

    finally:
        db.close()
