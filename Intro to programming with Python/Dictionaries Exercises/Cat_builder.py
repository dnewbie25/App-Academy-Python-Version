def cat_builder(name_str, color_str, age_num):
    hash = {
        'name': name_str,
        'color': color_str,
        'age': age_num,
    }

    return hash

print(cat_builder("Whiskers", "orange", 3))
print(cat_builder("Salem", "black", 100))