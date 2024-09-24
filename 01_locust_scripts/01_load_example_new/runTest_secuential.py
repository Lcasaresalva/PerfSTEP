from tasks.actions_user import ActionsOnUser
from authentication.users_login import UsersAdmin


class ThreadGroupForAdmins(UsersAdmin):
    tasks = {
        ActionsOnUser.delete_user: 6,
        ActionsOnUser.modify_user: 4,
        ActionsOnUser.create_user: 2,
    }
