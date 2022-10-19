from django.db import models

# Create your models here.

order_List=(
("Apple Juice",'Apple Juice'),
("Carrot Juice",'Carrot Juice'),
("Cheese Burger",'Cheese Burger'),
("Chicken Roast",'Chicken Roast'),
("Chinese Soup",'Chinese Soup'),
("Cold Coffee",'Cold Coffee'),
("Cold Drink",'Cold Drink'),
("Cupcake",'Cupcake'),
("Doughnut",'Doughnut'),
("Drum Stick",'Drum Stick'),
("Egg Fry",'Egg Fry'),
("Fish Fry",'Fish Fry'),
("Fresh Juice",'Fresh Juice'),
("Hot Dogs",'Hot Dogs'),
("Ice Cream",'Ice Cream'),
("Maggi",'Maggi'),
("Noodles",'Noodles'),
("Pastry",'Pastry'),
("Pizza",'Pizza'),
("Potato Fries",'Potato Fries'),
("Prawns",'Prawns'),
("Champagne",'Champagne'),
("Shawarma",'Shawarma'),
("Soda water",'Soda water'),
("Steam Roast",'Steam Roast'),
("Tea",'Tea'),



)


class login(models.Model):
    FirstName=models.CharField(max_length=200)
    LastName=models.CharField(max_length=200)
    Gender=models.CharField(max_length=50)
    Email=models.CharField(max_length=200)
    PhoneNumber=models.CharField(max_length=300)
    address=models.TextField()
    order=models.CharField(max_length=200,choices =order_List)





class contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()

class blogs(models.Model):
    title=models.CharField(max_length=500)
    des=models.TextField()
    image=models.ImageField(upload_to='photo/')
    poston=models.DateField()