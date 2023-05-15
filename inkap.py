class MyException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message}, код ошибки: {self.error_code}"

class ValueTooLargeException(MyException):
    def __init__(self, message, error_code, max_value):
        super().__init__(message, error_code)
        self.max_value = max_value

    def __str__(self):
        return f"{self.message}, код ошибки: {self.error_code}, максимальное допустимое значение: {self.max_value}"

class Login:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    def authenticate(self, entered_password):
        try:
            if entered_password != self.__password:
                raise MyException("Неверный пароль", 1)
            else:
                print("Аутентификация прошла успешно")
        except MyException as e:
            print(f"Произошла ошибка: {e}")

    def change_password(self, new_password):
        try:
            if len(new_password) > 20:
                raise ValueTooLargeException("Слишком длинный пароль", 2, 20)
            else:
                self.__password = new_password
                print("Пароль изменен")
        except MyException as e:
            print(f"Произошла ошибка: {e}")

login = Login("user123", "qwerty")
login.authenticate("12345")
login.change_password("new_super_duper_password_that_is_way_too_long")

