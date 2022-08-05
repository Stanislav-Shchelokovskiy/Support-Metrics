update_compose:
	scp -i ~/.ssh/work_machine docker-compose.yaml stas@ubuntu-support.corp.devexpress.com:~/user_posts_statistic/.
	scp -i ~/.ssh/work_machine .env stas@ubuntu-support.corp.devexpress.com:~/user_posts_statistic/.