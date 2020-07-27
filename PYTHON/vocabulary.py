#  alien_0 = {'color': 'Blue', 'points': '5 xp'}
# print(alien_0['color'] + ' - ' + alien_0['points'])

# new_point = alien_0['points']
# print(f"You earned {new_point}!")

# alien = {'color': 'Blue', 'points': '5 xp'}
# del alien['points']
# print(alien)

# alien = {}
# alien['x_position'] = '0'
# alien['y_position'] = '25'
# alien['speed'] = 'medium'
# print(f"Original position: {alien['x_position']}")


# if alien['speed'] == 'slow':
#     x_increment = '1'
# elif alien['speed'] == 'medium':
#     x_increment = '2'
# else:
#     x_increment = '3'

# alien['x_position'] = int(alien['x_position']) + int(x_increment)
# print(f"New position: {alien['x_position']}")

# print(alien['x_position'] ,':', type(alien['x_position']))
# print(x_increment ,':', type(x_increment))

# or

# if alien['speed'] == 'slow':
#     x_increment = 1
# elif alien['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien['x_position'] = int(alien['x_position']) + x_increment
# print(f"New position: {alien['x_position']}")

# favorite_language = {
# 'janis': 'java',
# 'rich': 'js',
# 'ron': 'dotnet',
# 'bogdan': 'react',
# 'santa': 'python',
# }

# language = favorite_language['rich'].title()
# print(f"Rich's favorite language is {language}.")