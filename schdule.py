from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='python manage.py get_all_orders')
job.minute.every(1)

print('command running every 1 min')

