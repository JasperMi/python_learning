favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

respondents = ['jack', 'lucy', 'edward']
for respondent in respondents:
    if respondent in favorite_languages.keys():
        print("Thank you for taking the poll!")
    else:
        print("Please take the poll!")
