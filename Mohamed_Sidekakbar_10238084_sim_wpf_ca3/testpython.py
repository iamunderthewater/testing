songs = int(input("Enter the number of songs:"))
price = 0.99 * songs
print("The price is $",price)

album = int(input("Enter your number of album you bought:"))
gana_song = album * 3.90
print("The total is $",gana_song)

school= int(input("Enter your admission:"))
student = school * 1000
print("the total amount is $", student)

age= 25
print("my age is",age,'thank you so much')

google = int(input("how many hours did you work ?"))
payrate = google * 20
print("your salary is $", payrate)

#this is comment section.
#Algorithm 
#step 1 : Get the radius (R) of the circle
#step 2: Calculate area (A) of the circle by using the formula, A= PI * R^2
#step 3: Calculate circumference (c) by using formula, C = 2 * PI *2 
#step 4: Display calculate area and circumference of circle.

#PSEUDOCODE: 
#Declare radius, area, circumference as REAL
#Set PI = 3.14159
#Display "Enter the radius"
#Input radius 
#Compute area= PI * radius^2
#compute circumference = 2 * PI * radius 
#print "the area of the circle is" + area
#print "the circumference of the circle is" + circumference.


hello= int(input("Enter your phone number ?"))
words= ("thank you so much ")
cities = {'GA':'Atlanta','NY':'Albany','CA':'San Diego'}
if 'FL' in cities:
            del cities['FL']
            cities['FL'] = 'Tallahassee'
print(cities)