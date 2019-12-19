rivers = {
    'nile': 'egypt',
    'heilong jiang': 'china',
    'changjiang': 'china'
}

for river, country in rivers.items():
    print(river.title() + " : " + country.title())
    print("The " + river.title() + " run through " + country.title() + ".")
