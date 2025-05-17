from django.db import models


class Product(models.Model):
    item = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.item} - {self.unit_price}"


class Groups(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Worker(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    gh_card = models.CharField("Ghana Card Number", max_length=20)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    groups = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='workers')
    is_leader = models.BooleanField(default=False)  # New field for leader status

    def __str__(self):
        return f"{self.name} ({self.groups.name}) - {self.gh_card}"
    


class WorkerProduct(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="sown_products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="workers")
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.worker} - {self.product} - {self.quantity} sown"


from django.db import models
from django.utils import timezone

class DailyProduction(models.Model):
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    description = models.CharField(null=True, blank=True, max_length=200)
    date = models.DateField(default=timezone.now)

    @property
    def amount_due(self):
        return self.quantity * self.product.unit_price

    def __str__(self):
        return f"{self.worker.name} - {self.product.item} - {self.quantity} units on {self.date} "
    @property
    def amount_due(self):
        return self._amount_due

    @amount_due.setter
    def amount_due(self, value):
        self._amount_due = value
    
    def save(self, *args, **kwargs):
        self.amount_due = self.quantity * self.product.unit_price
        super().save(*args, **kwargs)










