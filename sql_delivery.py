import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="zakaz"
)

mycursor = mydb.cursor()


# food_types = id, name
# restaurants = id, name, address
# foods = id, name, price, description, food_type_id, restaurant_id


def addRestaurants(name, address):
    mycursor = mydb.cursor()
    sql = "INSERT INTO restaurants (idd, name, address) VALUES (NULL, %s, %s)"
    values = (name, address)
    mycursor.execute(sql, values)
    mydb.commit()


def addFoodtypes(name):
    mycursor = mydb.cursor()
    sql = "INSERT INTO food_types (idd, name) VALUES (NULL, %s)"
    values = (name,)
    mycursor.execute(sql, values)
    mydb.commit()


def addFoods(name, price, description, food_type_id, restaurant_id):
    mycursor = mydb.cursor()
    sql = "INSERT INTO foods (idd, name, price, description, restaurant_id, food_type_id) VALUES (NULL, %s, %s, %s, %s, %s)"
    values = (name, price, description, food_type_id, restaurant_id)
    mycursor.execute(sql, values)
    mydb.commit()


def getRestaurant():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM restaurants"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    return res


def getFoodtypes():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM food_types"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    return res


def getFoods():
    mycursor = mydb.cursor()
    sql = "SELECT f.idd, f.name, f.price, f.description,f.restaurant_id, f.food_type_id, r.name, r.address, ft.name FROM foods f LEFT OUTER JOIN restaurants r ON r.idd = f.restaurant_id LEFT OUTER JOIN food_types ft ON ft.idd = f.food_type_id"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    return res


def delRest(id):
    sql = "DELETE FROM restaurants WHERE idd = %s"
    values = (id,)
    mycursor.execute(sql, values)
    mydb.commit()


def delFoodTypes(id):
    sql = "DELETE FROM food_types WHERE idd = %s"
    values = (id,)
    mycursor.execute(sql, values)
    mydb.commit()


def delFoods(id):
    sql = "DELETE FROM foods WHERE idd = %s"
    values = (id,)
    mycursor.execute(sql, values)
    mydb.commit()


def uploadRest(u_name, u_address, id):
    sql = "UPDATE restaurants SET name=%s, address=%s WHERE idd=%s"
    values = (u_name, u_address, id)
    mycursor.execute(sql, values)
    mydb.commit()


def uploadFoodTypes(u_name, id):
    sql = "UPDATE food_types SET name=%s WHERE idd=%s"
    values = (u_name, id)
    mycursor.execute(sql, values)
    mydb.commit()


def uploadFood(u_name, u_price, u_description, u_restaurant_id, u_food_type_id, id):
    sql = "UPDATE food_types SET name=%s, price=%s, description=%s, restaurant_id=%s, food_type_id=%s WHERE idd=%s"
    values = (u_name, u_price, u_description, u_restaurant_id, u_food_type_id, id)
    mycursor.execute(sql, values)
    mydb.commit()


while True:
    print("[1]Добавить ресторан")
    print("[2]Добавить тип еды")
    print("[3]Добавить еду")
    print("[4]Вывести список ресторанов")
    print("[5]Вывести список типовы еды")
    print("[6]Вывести список еды")
    print("[7]Удалить ресторан")
    print("[8]Удалить тип еды")
    print("[9]Удалить еды")
    print("[10]Обновить ресторан")
    print("[11]Обновить тип еды")
    print("[12]Обновить еду")
    print("[0]EXIT")
    choice = int(input("Insert choice: "))
    if choice == 1:
        name = input("Insert restaurant name: ")
        address = input("Insert address of restaurant: ")
        addRestaurants(name, address)
    elif choice == 2:
        name = input("Insert name of types food: ")
        addFoodtypes(name)
    elif choice == 3:
        name = input("Insert name of food: ")
        price = int(input("Insert price: "))
        description = input("Insert description: ")
        restaurant_id = int(input("Insert restaurant ID: "))
        food_type_id = int(input("Insert food type ID: "))
        addFoods(name, price, description, restaurant_id, food_type_id)
    elif choice == 4:
        restaurant = getRestaurant()
        for p in restaurant:
            print(p)
    elif choice == 5:
        type = getFoodtypes()
        for p in type:
            print(p)
    elif choice == 6:
        food = getFoods()
        for p in food:
            print(p)
    elif choice == 7:
        id = int(input("Insert id: "))
        delRest(id)
    elif choice == 8:
        id = int(input("Insert id: "))
        delFoodTypes(id)
    elif choice == 9:
        id = int(input("Insert id: "))
        delFoods(id)
    elif choice == 10:
        u_name = input("Insert new name: ")
        u_address = input("Insert new addres: ")
        id = int(input("Insert id: "))
        uploadRest(u_name, u_address, id)
    elif choice == 11:
        u_name = input("Insert new name: ")
        id = int(input("Insert id: "))
        uploadFoodTypes(u_name, id)
    elif choice == 12:
        u_name = input("Insert new name: ")
        u_price = input("Insert new price: ")
        u_description = input("Insert new description: ")
        u_restaurant_id = int(input("Insert new id for restaurant id: "))
        u_food_type_id = int(input("Insert new id for food type id: "))
        id = int(input('Insert id: '))
    else:
        print("ERROR...")

# u_name, u_price, u_description, u_restaurant_id, u_food_type_id, id
