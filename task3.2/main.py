from pymongo import MongoClient
from bson.objectid import ObjectId
import os

# Підключення до MongoDB через змінну середовища або дефолтний URI
MONGO_URI = os.getenv("MONGO_URI", "mongodb://root:example@localhost:27017/")
client = MongoClient(MONGO_URI)

# Вибір бази даних і колекції
db = client["cats_db"]
collection = db["cats"]

def create_cat(name, age, features):
    """Додає нового кота в базу даних."""
    try:
        cat = {"name": name, "age": age, "features": features}
        result = collection.insert_one(cat)
        print(f"Кіт {name} доданий у базу з ID {result.inserted_id}")
    except Exception as e:
        print("Помилка при додаванні кота:", e)

def read_all_cats():
    """Виводить всіх котів у базі даних."""
    try:
        cats = collection.find()
        print("\nСписок всіх котів у базі:")
        for cat in cats:
            print(cat)
    except Exception as e:
        print("Помилка при зчитуванні котів:", e)

def read_cat_by_name(name):
    """Знаходить кота за ім'ям."""
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(f"\nЗнайдено кота {name}: {cat}")
        else:
            print(f"Кота з ім'ям {name} не знайдено.")
    except Exception as e:
        print("Помилка при пошуку кота:", e)

def update_cat_age(name, new_age):
    """Оновлює вік кота за ім'ям."""
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count:
            print(f"Вік кота {name} оновлено до {new_age}.")
        else:
            print(f"Кіт {name} не знайдений або вік не змінено.")
    except Exception as e:
        print("Помилка при оновленні віку кота:", e)

def add_feature_to_cat(name, new_feature):
    """Додає нову характеристику коту за ім'ям."""
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.modified_count:
            print(f"До кота {name} додано характеристику: {new_feature}.")
        else:
            print(f"Кіт {name} не знайдений або характеристика вже існує.")
    except Exception as e:
        print("Помилка при додаванні характеристики:", e)

def delete_cat_by_name(name):
    """Видаляє кота за ім'ям."""
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print(f"Кіт {name} видалений.")
        else:
            print(f"Кіт {name} не знайдений.")
    except Exception as e:
        print("Помилка при видаленні кота:", e)

def delete_all_cats():
    """Видаляє всіх котів з бази."""
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} записів.")
    except Exception as e:
        print("Помилка при видаленні всіх котів:", e)

if __name__ == "__main__":
    # Тестування функцій: створення, читання, оновлення, видалення
    print("\nСтворення кота...")
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    
    print("\nВиведення всіх котів...")
    read_all_cats()
    
    print("\nПошук кота по імені 'barsik'...")
    read_cat_by_name("barsik")
    
    print("\nОновлення віку кота 'barsik' до 5 років...")
    update_cat_age("barsik", 5)
    
    print("\nДодавання характеристики 'любить рибу'...")
    add_feature_to_cat("barsik", "любить рибу")
    
    print("\nВиведення кота після оновлення...")
    read_cat_by_name("barsik")
    
    print("\nВидалення кота 'barsik'...")
    delete_cat_by_name("barsik")
    
    print("\nВидалення всіх котів...")
    delete_all_cats()
    
    print("\nУсі операції виконано!")
