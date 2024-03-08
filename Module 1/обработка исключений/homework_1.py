class WrongCharacterError(Exception):
    pass


class FirstCharacterError(Exception):
    pass

def check_username(username):
    if  not username.isalnum() :
        raise WrongCharacterError('username может содержать только буквы и цифры')
    if username[0].isdigit():
        raise FirstCharacterError('username не может начинаться с цифры')



try:
    username = input()
    check_username(username)
except WrongCharacterError as e:
    print(e)
except FirstCharacterError as e:
    print(e)
else:
    print('OK')



