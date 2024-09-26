from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator

STATE_CHOICES = {
    ('DANG','DANG'),
    ('kathamandu','kathamandu'),
    ('lalitpur','lalitpur'),
    ('Bhaktpur','Bhaktpur'),
    ('Tulsipur','Tulsipur'),
    ('Nepaljung','Nepaljung'),
    ('Dharan','Dharan'),
    ('Dhankuta','Dhankuta'),
    ('salyan','salyan'),
    ('Rukum','Rukum'),
    ('Rolpa','Rolpa'),
    ('Puythan','Puythan'),
    ('Bardia','Bardia'),
    ('Lamjung','Lamjung'),
    ('Pokhara','Pokhara'),
    

    

}

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=70)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)



    def __str__(self):
        return str(self.name)
    



category_choice = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('T', 'Top_wear'),
    ('B', 'Bottom_wear'),
)

class Product(models.Model):
    Title = models.CharField(max_length=50)
    selling_price = models.FloatField(default=0)  # Corrected the default value
    Discounted_price = models.FloatField(default=0)  # Corrected the default value
    Description = models.TextField()
    Brand = models.CharField(max_length=50)
    Category = models.CharField(choices=category_choice, max_length=4, default='T')  # Provide a valid default category
    Product_image = models.ImageField(upload_to='Product_image')

    def __str__(self):
        return self.Title

    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.CharField(max_length=50)
    Quantity = models.PositiveBigIntegerField(default=0)


    def __str__(self):
        return str(self.id)
    

Status_check ={
    ('Acceppted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Deivered','Deivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending')
}


class OrderPlaces(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=1)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status_check,max_length=40, default='Pending')



   
    def __str__(self):
        return str(self.Product)
    
