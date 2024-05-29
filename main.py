import pyotp
import time

# Генерация секретного ключа
secret = pyotp.random_base32()
print(f"Секретный ключ: {secret}")

# Создание объекта TOTP -- Time-based One-Time Password 
totp = pyotp.TOTP(secret)

# Генерация одноразового пароля
otp = totp.now()
print(f"Одноразовый пароль: {otp}")

# Проверка одноразового пароля
is_valid = totp.verify(otp)
print(f"Пароль верный: {is_valid}")

# Проверка одноразового пароля через некоторое время
time.sleep(30)
new_otp = totp.now()
print(f"Новый одноразовый пароль: {new_otp}")
is_new_valid = totp.verify(new_otp)
print(f"Новый пароль верный: {is_new_valid}")
