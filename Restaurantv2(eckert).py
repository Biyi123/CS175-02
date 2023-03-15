#Biyi Abass
#CS175L-02
#restaurant



vegetarian = False
vegan = False
gluten_free = False

response= str(input('Is anyone in your party a vegetarian? '))
if response== 'yes':
     vegetarian = True
if response== 'no':
     vegetarian = False

response = str(input('Is anyone in your party a vegan? '))
if response == 'yes':
    vegan = True
if response == 'no':
    vegan = False

response =str(input('Is anyone in your party gluten-free? '))
if response == 'yes':
    vegan = True
if response == 'no':
    
    vegan = False

print('Here are your restaurant choices. ')

if not vegetarian and not vegan or gluten_free:
    print('Joe\'s Gourment Burgers')
    print('Main Street Pizza Company')
    print('Corner Cafe')
    print('The Chef\'s Kitchen')
    print('Mama\'s Fine Italian')


print("Enter 'yes' if you would like to do another restaurant search(enter'no' to end")

 
