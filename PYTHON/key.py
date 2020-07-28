# user = {
# 'username': 'efermi',
# 'first': 'enrico',
# 'last': 'fermi',
# }
# for key, value in user.items():
#         print(f"\nKey: {key}")
#         print(f"Value: {value}")

# favorite_language = {
# 'janis': 'java',
# 'rich': 'js',
# 'ron': 'dotnet',
# 'bogdan': 'react',
# 'santa': 'python',
# }

# friends = ['bogdan', 'rich']
# for name in favorite_language.keys():
#     print(name.title())

#     if  name in friends:
#         language = favorite_language[name].title()
#         print(f"\t{name.title()}, i see you love {language}")

#     if 'erin' not in favorite_language.keys():
#         print("Erin, please take our poll!")

# for name, language in favorite_language.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# user = {
#  'username': 'efermi',
#  'first': 'enrico',
#  'last': 'fermi',
#  }

# for key, value in user.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# favorite_language = {
# 'janis': 'java',
# 'rich': 'js',
# 'ron': 'dotnet',
# 'bogdan': 'react',
# 'santa': 'python',
# }

# for name in sorted(favorite_language.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# -- список всех языков, выбранных в опросе, и вас не интересуют 
# имена людей, выбравших каждый язык --

# print("The following languages have been mentioned:")
# for language in favorite_language.values():
#     print(language.title())

# -- список выбранных языков без повторений --

# print("The following languages have been mentioned:")
# for language in set(favorite_language.values()):
#     print(language.title())