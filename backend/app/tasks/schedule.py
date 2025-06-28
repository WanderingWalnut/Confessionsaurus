# Manages background execution
from apscheduler.schedulers.blocking import BlockingScheduler
from app.tasks.moderation_confession import moderate_all_confessions
from app.tasks.instagram_post import post_to_instagram

def run_moderation_job():
    print("🕒 Running moderation job…")
    moderate_all_confessions()

def run_post_to_instagram_job():
    print("🕒 Running post to instagram job…")
    post_to_instagram()


if __name__ == "__main__":
    scheduler = BlockingScheduler() 

    # Run every hour
    scheduler.add_job(run_moderation_job, 'interval', minutes = 5, id="moderate")

    # Run every 2 hours
    scheduler.add_job(run_post_to_instagram_job, 'interval', minutes=10, id="post")

    print("Scheduler Started...")
    scheduler.start()

# TODO: Make sure to check while FastAPI is running and new confessions are coming via the front end