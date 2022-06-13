from django.db import models
from django.contrib.auth.models import AbstractUser


USER_TYPE = (
    ("BP","Brand Partner"),
    ("EU", "End User")
)

BENEFIT_TYPE = (
    ("CB", "Cashback"),
    ("EV", "Extra Voucher")
)
class User(AbstractUser):
    user_type = models.CharField(verbose_name="Type of user", max_length=2, choices=USER_TYPE, default="EU")

    def __str__(self):
        return self.username

class Plan(models.Model):
    plan_name = models.CharField(max_length=254)
    plan_created_by = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    amount = models.IntegerField(default=0)
    tenure_option = models.IntegerField(verbose_name="For how many months this tenure will be valid")
    benefit_percentage = models.IntegerField(default=0)
    benefit_type = models.CharField(max_length=2, choices=BENEFIT_TYPE)
    timestamp =  models.DateField(auto_now=True)

    def __str__(self):
        return self.plan_name

class BrandPromotion(models.Model):
    plan = models.OneToOneField(Plan, on_delete=models.PROTECT)
    time_period_start = models.DateField(null=True, blank=True)
    time_period_end = models.DateField(null=True, blank=True)
    users = models.IntegerField(verbose_name="For how many users this promotion will be valid", default=0)
    timestamp =  models.DateField(auto_now=True)

    def __str__(self):
        return self.plan.plan_name

class CustomerGoals(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    selected_amount = models.IntegerField(default=0)
    selected_tenure = models.IntegerField(default=0)
    started_date = models.DateField(auto_now=True, null=True, blank=True)
    deposited_amount = models.IntegerField(default=0)
    benefit_percentage = models.IntegerField(default=0)
    benefit_type = models.CharField(max_length=2, choices=BENEFIT_TYPE, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
