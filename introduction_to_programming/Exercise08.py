#Widgets and Gizmos

widgets = int(input('Enter the total widget ---> '))
gizmos = int(input('Enter the total gizmos ---> '))

widget_weighs = 0.75 * widgets
gizmo_weighs = 1.12 * gizmos 
total = widget_weighs + gizmo_weighs
total = round(total,2)

print('''The total weight of the widgets is''', widget_weighs,
'''\nThe total weight of the gizmos is''', gizmo_weighs,
'''\nTotal weight is''', total, 'grams')