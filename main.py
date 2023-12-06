import Database
import Order
import Product
import User 
db = Database('shop.db')


def register_user():
    print("Регистрация пользователя")
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    role = input("Введите роль пользователя (например, 'customer' или 'admin'): ")
    user = User(None, username, password, role)
    db.add_user(user)
    print("Пользователь успешно зарегистрирован!")


def place_order():
    print("Сделать заказ")
    user_id = int(input("Введите ваш ID (из регистрации): "))
    product_id = int(input("Введите ID продукта: "))
    quantity = int(input("Введите количество: "))
    order = Order(None, user_id, product_id, quantity)
    db.add_order(order)
    print("Заказ успешно размещен!")


def cancel_order():
    print("Отменить заказ")
    order_id = int(input("Введите ID заказа для отмены: "))
    db.c.execute("DELETE FROM orders WHERE id=?", (order_id,))
    db.conn.commit()
    print("Заказ успешно отменен!")
def main():
    print("Добро пожаловать в магазин!")
    print("1.Зарегистрироваться")
    print("2.Сделать заказ")
    print("3.Отменить заказ")
    res = int(input())
    match res:
        case 1:
            register_user()
            pass
        case 2:
            place_order()
            pass
        case 3:
            cancel_order()
            pass
        case _:
            print("Невеврный выбор.")
    print("Неверный выбор")

main()






# Добавление пользователей
#db.add_user(User(1, 'user1', 'password1', 'client'))
#db.add_user(User(2, 'user2', 'password2', 'employee'))
#db.add_user(User(3, 'user3', 'password3', 'admin'))

# Добавление товаров
#db.add_product(Product(1, 'product1', 100, 10))
#db.add_product(Product(2, 'product2', 200, 20))

# Добавление заказов
#db.add_order(Order(1, 1, 1, 2))
#db.add_order(Order(2, 2, 2, 3))

# Получение данных
#print(db.get_users())
#print(db.get_products())
#print(db.get_orders())

db.close()