class User:
    def __init__(self, ID, name, access_level="user"):
        # Атрибуты защищаются от прямого доступа
        self.__name = name
        self.__ID = ID
        self.__access_level = access_level

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise ValueError("Имя должно быть строкой")

    @property
    def ID(self):
        return self.__ID

    @property
    def access_level(self):
        return self.__access_level

    def __repr__(self):
        return f"{self.__class__.__name__}(ID пользователя = {self.ID}, имя пользователя = '{self.name}', уровень доступа = '{self.access_level}')"

class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name, access_level="admin")

    # Список пользователей хранится в переменной класса
    users = []

    def add_user(self, user):
        if not isinstance(user, User):
            raise TypeError("Можно добавить только объект типа User")
        Admin.users.append(user)
        print(f"Пользователь {user.name} добавлен.")

    def remove_user(self, user_id):
        for index, user in enumerate(Admin.users):
            if user.ID == user_id:
                del Admin.users[index]
                print(f"Пользователь с ID {user_id} удалён.")
                break
        else:
            print(f"Пользователь с ID {user_id} не найден.")

def main():
    # Создание администратора
    admin = Admin(ID=1, name="AdminUser")

    # Добавление пользователей
    user1 = User(ID=2, name="Василий")
    user2 = User(ID=3, name="Анна")

    admin.add_user(user1)
    admin.add_user(user2)

    # Вывод всех пользователей
    print("Текущие пользователи:")
    for user in Admin.users:
        print(user)

    # Удаление пользователя
    admin.remove_user(2)

    # Вывод всех пользователей после удаления
    print("Пользователи после удаления:")
    for user in Admin.users:
        print(user)

if __name__ == "__main__":
    main()