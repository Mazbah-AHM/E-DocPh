from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    IC_no = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)

    def __str__(self):
        return self.user

    def __str__(self):
        return self.name 


class m_Product(models.Model):
    name = models.CharField(max_length=200)
    Brand = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=2000)
    tags = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} - {self.quantity} - {self.Brand} - {self.price}'

    def brandchart(self):
        br = self.Brand
        if br == br:
            self.quantity += self.quantity
        return self.quantity

          

 

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Prescription(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    authorize = models.CharField(max_length=200,default="Pending")
    precripImage = models.ImageField(null=True, blank=True)    

    def __str__(self):
         return f'{self.complete} - {self.date_ordered}'

    @property
    def dateo(self):
        
        sec = self.complete
        if sec == True:   
            return self.date_ordered 


    @property
    def prescripImageURL(self):
        try:
            url = self.precripImage.url
        except:
            url = ''
        return url


    @property
    def approve(self):
        appr=self.authorize
        appr = True
        return appr    

    @property
    def disapprove(self):
        appr = self.authorize
        appr = False
        return appr  


    @property
    def nameChange(self):
        complete = self.complete
        if complete == False:
            complete = 'Pending'
        else:
            complete="Delivered"       

        return complete    

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
    	orderitems = self.orderitem_set.all()
    	total = sum([item.get_total for item in orderitems])
    	return total

        

    # @property
    # def get_cart_supertotal(self):
    #     supertotal = self.get_cart_total * 0.18
    #     suptotal=supertotal + self.get_cart_total
    #     return suptotal    

    @property
    def get_cart_items(self):
    	orderitems = self.orderitem_set.all()
    	total = sum([item.quantity for item in orderitems])
    	return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        m_Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(
        Prescription, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
    	total = self.product.price * self.quantity
    	return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order= models.ForeignKey(Prescription, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200,null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    contact_no = models.CharField(max_length=200)

    def __str__(self):
        return self.address