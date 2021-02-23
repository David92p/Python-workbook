#Area of a Field

feet_length_of_your_farm = input("Enter the feet length of your farm ")
feet_width_of_your_farm = input("Enter the feet width of your farm ")

feet_area= float(feet_length_of_your_farm) * float(feet_width_of_your_farm)
acres_area_calculate = feet_area/43560
round_acreas = round(acres_area_calculate,2)

print('your feet area is', feet_area, 'but the acres in your farm is', round_acreas)