
from tasks.actions_pet import *
from tasks.actions_store import *
from authentication.users_login import UsersAdmin, UsersGranted


class ThreadGroupForAdmins(UsersAdmin):
    weight = 6
    tasks = {
        update_pet: 1,
        order_store: 2,
        return_inventory: 4
    }


class ThreadGroupForUsers(UsersGranted):
    weight = 4
    tasks = {
        find_pet: 1,
        delete_order: 2
    }
