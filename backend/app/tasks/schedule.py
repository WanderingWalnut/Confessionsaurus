# Manages background execution
from apscheduler.schedulers.blocking import BlockingScheduler
from app.tasks.moderation_confession import moderate_all_confessions
from app.tasks.instagram_post import post_to_instagram
from app.db.crud_confession import generate_confessions, delete_posted_confessions

def run_moderation_job():
    print("🕒 Running moderation job…")
    moderate_all_confessions()

def run_post_to_instagram_job():
    print("🕒 Running post to instagram job…")
    post_to_instagram()

def run_generate_confessions_job():
    print("🕒 Running generate confessions job…")
    generate_confessions()

def run_delete_posted_confessions_job():
    print("🕒 Running delete posted confessions job…")
    delete_posted_confessions()

if __name__ == "__main__":
    scheduler = BlockingScheduler() 

    scheduler.add_job(generate_confessions, 'interval', minutes = 1, id='generate')

    # Run every hour
    scheduler.add_job(run_moderation_job, 'interval', minutes = 2, id="moderate")

    # Run every 2 hours
    scheduler.add_job(run_post_to_instagram_job, 'interval', minutes=3, id="post")

    scheduler.add_job(delete_posted_confessions, 'interval', minutes=1, id='delete')


    print("Scheduler Started...")
    scheduler.start()

# TODO: Make sure to check while FastAPI is running and new confessions are coming via the front end