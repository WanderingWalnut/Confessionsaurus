from app.jobs.run_jobs import job_post


def handler(event, context):
    return {"ok": True, "result": job_post()}


