from app.tasks.moderation_confession import moderate_all_confessions
from app.tasks.instagram_post import post_to_instagram
from app.db.crud_confession import generate_confessions, delete_posted_confessions


def job_generate():
    print("🕒 Running generate confessions job…")
    return generate_confessions()


def job_moderate():
    print("🕒 Running moderation job…")
    return moderate_all_confessions()


def job_post():
    print("🕒 Running post to instagram job…")
    return post_to_instagram()


def job_delete():
    print("🕒 Running delete posted confessions job…")
    return delete_posted_confessions()


