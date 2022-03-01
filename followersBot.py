from instapy import InstaPy
from instapy import smart_run
import schedule
import time



username = ""
password = ""

target_users = ""

# def follow():
session =  InstaPy(
        username = username,
        password = password,
        headless_browser = True
        )

with smart_run(session):
        session.set_skip_users(skip_private=False)        
        session.follow_user_followers(
            target_users,
            amount=100,
            randomize=True
        )
        
session.end()
        
# schedule.every().day.at("10:00").do(follow)
# schedule.every().day.at("19:33").do(follow)

# while True:
#     schedule.run_pending()
#     time.sleep(10)



# with smart_run(session):
#     session.set_relationship_bounds(
#         enabled=True,
#         delimit_by_numbers=True,
#         max_followers=500,
#         min_followers=30,
#         min_following=50
#         )
#     session.set_do_follow(True,percentage=100)
# session.login()

# # session.set_relationship_bounds(enabled= True, max_followers= 200)

# # session.set_do_follow(True,percentage=100)
# # session.follow_by_locations["perrieedwards"]
# session.follow_user_followers([""],amount=200,randomize= True)
# session.end()
