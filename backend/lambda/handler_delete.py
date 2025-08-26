from app.jobs.run_jobs import job_delete


def handler(event, context):
    return {"ok": True, "result": job_delete()}


