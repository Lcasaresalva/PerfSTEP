"""


"""
# Example in command line with autoquit to avoid the usage of ctrl+c:
# locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -r 2 -t 20 --processes 4 --autostart --autoquit 3


from tasks.actions_pet import ActionsOnPet
from tasks.actions_store import ActionsOnStore
from tasks.actions_user import ActionsOnUser
from authentication.users_login import UsersAdmin, UsersGranted


class ThreadGroupForAdmins(UsersAdmin):
    weight = 5
    UsersAdmin.tasks = {
        ActionsOnStore.return_inventory: 2,
        ActionsOnUser.modify_user: 2,
        ActionsOnStore.order_store: 1,
    }


class ThreadGroupForUsers(UsersGranted):
    weight = 5
    UsersGranted.tasks = {
        ActionsOnUser.create_user: 2,
        ActionsOnPet.update_pet: 2,
        ActionsOnPet.find_pet: 2,
        ActionsOnStore.delete_order: 2
    }
