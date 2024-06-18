import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    N = int(input("Введите количество паролей для генерации: "))
    K = int(input("Введите длину пароля: "))

    passwords = [generate_password(K) for _ in range(N)]

    print(f"{N} различных паролей длиной {K} символов:")
    for password in passwords:
        print(password)


if __name__ == "__main__":
    main()
