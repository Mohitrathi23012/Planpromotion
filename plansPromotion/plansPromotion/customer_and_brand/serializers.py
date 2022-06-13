from rest_framework import serializers, viewsets

from customer_and_brand.permissions import IsBrandPromoterOrCustomer
from .models import BrandPromotion, CustomerGoals, Plan, User

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','first_name','last_name','user_type','password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsBrandPromoterOrCustomer]

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class BrandPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandPromotion
        fields = (
            'plan',
            'time_period_start',
            'time_period_end',
            'users',
            'url',
        )

class BrandPromotionViewSet(viewsets.ModelViewSet):
    queryset = BrandPromotion.objects.all()
    serializer_class = BrandPromotionSerializer

class CustomerGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGoals
        fields = (
            "plan",
            "user",
            "selected_amount",
            "selected_tenure",
            "started_date",
            "deposited_amount",
            "benefit_percentage",
            "benefit_type",
            "url",
        )

class CustomerGoalsViewSet(viewsets.ModelViewSet):
    queryset = CustomerGoals.objects.all()
    serializer_class = CustomerGoalsSerializer