from sql.meta_data import MetaData


class UserPoststByTribesMetaData(MetaData):
    user_id = 'user_id'
    user_name = 'user_name'
    license_status = 'license_status'
    tribe_name = 'tribe_name'
    user_posts_by_tribe = 'user_posts_by_tribe'
    user_posts_by_tribe_from_their_all_posts_perc = 'user_posts_by_tribe_from_their_all_posts_perc'
    user_posts_by_tribe_from_posts_from_all_users_perc = 'user_posts_by_tribe_from_posts_from_all_users_perc'
    user_posts = 'user_posts'
    user_posts_from_posts_from_all_users_perc = 'user_posts_from_posts_from_all_users_perc'
    posts_from_all_users = 'posts_from_all_users'
    user_tickets_by_tribe = 'user_tickets_by_tribe'
