from emporio import scheduler, db, ServiceCollaborator
from datetime import datetime, time
from dateutil.relativedelta import relativedelta


@scheduler.task('cron', id='purge_job', hour='23')
def purge_job():
    print("Iniciando scheduler...")
    date = datetime.combine(datetime.now() - relativedelta(months=2), time.max)
    with db.app.app_context():
        db.session.execute(
            db.delete(ServiceCollaborator)
            .where(ServiceCollaborator.service_collaborator_date <= date)
        )
        db.session.commit()
    print("Finalizando scheduler...")
