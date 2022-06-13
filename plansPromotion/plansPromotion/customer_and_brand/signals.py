from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

from customer_and_brand.models import CustomerGoals, BrandPromotion

@receiver(post_save, sender=CustomerGoals)
def create_customer_goals(sender, instance, created, **kwargs):
    if created:
        plan = instance.plan
        instance.selected_amount = plan.amount
        instance.selected_tenure = plan.tenure_option
        # deposited_amount = 
        instance.benefit_percentage = plan.benefit_percentage
        instance.benefit_type = plan.benefit_type

        brand_promotion = BrandPromotion.objects.get(plan=plan)

        time_period_start = brand_promotion.time_period_start
        past = time_period_start
        time_period_end = brand_promotion.time_period_end
        future = time_period_end
        present = datetime.now().date()

        if brand_promotion.users > 0:
            deposited_amount = int(plan.amount) - ((int(plan.amount)*int(instance.benefit_percentage))/100)
        elif past <= present <= future:
            deposited_amount = int(plan.amount) - ((int(plan.amount)*int(instance.benefit_percentage))/100)
        else:
            deposited_amount = int(plan.amount)

        instance.deposited_amount = deposited_amount

        instance.save()
