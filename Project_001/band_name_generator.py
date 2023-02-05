# Band Name Generator
# Get city of birth
# Get pet name
# Concatenate strings to create band name
# Display generated band name

city_name = input("Name of the city you were born in:\n")
pet_name = input("Name of your pet:\n")

band_name = " ".join([city_name, pet_name])
print(f"Your band name could be * {band_name} *")
