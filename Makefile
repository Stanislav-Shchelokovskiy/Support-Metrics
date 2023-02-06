update_compose:
	scp -i ~/.ssh/work_machine docker-compose.yaml stas@ubuntu-support.corp.devexpress.com:~/support_analytics/.
	scp -i ~/.ssh/work_machine .env stas@ubuntu-support.corp.devexpress.com:~/support_analytics/.

copy_db:
	sudo scp -i ~/.ssh/work_machine stas@ubuntu-support.corp.devexpress.com:~/support_analytics/db ~/support_analytics/data