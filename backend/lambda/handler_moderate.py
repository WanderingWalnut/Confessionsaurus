from app.jobs.run_jobs import job_moderate


def handler(event, context):
    return {"ok": True, "result": job_moderate()}


