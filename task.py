import csv


def read_file(filename: str) -> list[dict]:
    houses = []

    with open(filename, "r", encoding="UTF-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            house = {
                "area_id": row["area_id"],
                "house_address": row["house_address"],
                "floor_count": int(row["floor_count"]),
                "heating_house_type": row["heating_house_type"],
                "heating_value": float(row["heating_value"]),
                "area_residential": float(row["area_residential"]),
                "population": int(row["population"])
            }
            houses.append(house)

    return houses


def classify_house(floor_count: int) -> str:
    if not isinstance(floor_count, int):
        raise TypeError("Количество этажей должно быть целочисленным значением.")
    if floor_count <= 0:
        raise ValueError("Количество этажей должно быть положительным числом.")

    if floor_count <= 5:
        return "Малоэтажный"
    elif 6 <= floor_count <= 16:
        return "Среднеэтажный"
    else:
        return "Многоэтажный"

def get_classify_houses(houses: list[dict]) -> list[str]:
    categories = []
    for house in houses:
        floor_count = house.get("floor_count")
        if floor_count is not None:
            category = classify_house(floor_count)
            categories.append(category)
    return categories


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    count_dict = {}
    for category in categories:
        count_dict[category] = count_dict.get(category, 0) + 1
    return count_dict


def min_area_residential(houses: list[dict]) -> str:
    min_area_per_resident = float('inf')
    min_address = ""

    for house in houses:
        area_residential = house.get("area_residential")
        population = house.get("population")
        if area_residential is not None and population is not None and population != 0:
            area_per_resident = area_residential / population
            if area_per_resident < min_area_per_resident:
                min_area_per_resident = area_per_resident
                min_address = house.get("house_address", "")

    return min_address

houses_data = read_file("housing_data.csv")

# Классифицирует дом на основе количества этажей
house = classify_house(int(6))

# Классификация домов на основе количества этажей
classified_houses = get_classify_houses(houses_data)

# Подсчет количества домов в каждой категории
count_categories = get_count_house_categories(classified_houses)

# Нахождение дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца
min_address = min_area_residential(houses_data)

# Печать результатов
print("Классификация дома на основе количества этажей:", house)
print("Классификация домов на основе количества этажей:")
for category, count in count_categories.items():
    print(f"{category}: {count} домов")

print()
print(f"Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца: {min_address}")
