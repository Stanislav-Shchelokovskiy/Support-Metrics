update_compose:
	scp -i ~/.ssh/work_machine docker-compose.yaml stas@support.corp.com:~/support_metrics/.
	scp -i ~/.ssh/work_machine .env stas@support.corp.com:~/support_metrics/.

copy_db:
	sudo scp -i ~/.ssh/work_machine stas@support.corp.com:~/support_metrics/db ~/code/support_metrics/data