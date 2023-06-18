from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class Category(models.Model):
    category_name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.category_name


class Camera(models.Model):
    camera_name=models.CharField(max_length=200)
    options=(
        ("Canon","Canon"),
        ("Sony","Sony"),
        ("Panasonic","Panasonic"),
        ("Nikon","Nikon"),
        ("Fujifilm","Fujifilm"),
        ("Olympus","Olympus"),
    )
    company_name=models.CharField(choices=options,max_length=300,default="Canon")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    decription=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    
    
    def __str__(self):
        return self.camera_name
    
        
        
class SpecialProduct(models.Model):
    product_name=models.CharField(max_length=200)
    company_name=models.CharField(max_length=300,default="Canon")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    decription=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()
    discount=models.PositiveIntegerField(default=0)
    offerPoint=models.PositiveIntegerField(default=0)
    start_date=models.DateField(default=datetime.date.today)
    end_date=models.DateField(default=datetime.date.today)
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    
    def __str__(self):
        return self.product_name
        
class CameraDetails(models.Model):
    camera=models.ForeignKey(Camera,on_delete=models.CASCADE)
    company=models.CharField(max_length=300)
    categor=models.ForeignKey(Category,on_delete=models.CASCADE)
    decriptio=models.CharField(max_length=200)
    pric=models.PositiveBigIntegerField()
    is_ctive=models.BooleanField(default=True)
    imge=models.ImageField(upload_to="images",null=True,blank=True)

    
    def __str__(self):
        return self.camera
    
  
class Cart(models.Model):
    product=models.ForeignKey(Camera,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    qty=models.PositiveIntegerField(default=1)

class Orders(models.Model):
    product=models.ForeignKey(Camera,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("shipped","shipped"),
        ("order-placed","order-placed"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    curDtae=datetime.date.today()
    expDate=curDtae+datetime.timedelta(days=5)
    expected_deliverydate=models.DateField(default=expDate)
    address=models.CharField(max_length=260,null=True)
    
    
    
class SpecialCart(models.Model):
    product=models.ForeignKey(SpecialProduct,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    qty=models.PositiveIntegerField(default=1)
    
class SpecialOrders(models.Model):
    product=models.ForeignKey(SpecialProduct,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("shipped","shipped"),
        ("order-placed","order-placed"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    curDtae=datetime.date.today()
    expDate=curDtae+datetime.timedelta(days=5)
    expected_deliverydate=models.DateField(default=expDate)
    address=models.CharField(max_length=260,null=True)
    
class Billing(models.Model):
    firstname=models.CharField(max_length=20)
    email=models.EmailField(default=True)
    phone_no=models.CharField(max_length=12)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    