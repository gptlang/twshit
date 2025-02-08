# pyright: reportArgumentType=false
from store import Store
from twpost import add_user_to_list

if __name__ == '__main__':
   store = Store()
   users = store.get_users(500)
   for user in users:
      add_user_to_list(int(user.id), 1888327464989974886)
