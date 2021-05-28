from rest_framework.serializers import ModelSerializer
from .models import car_model, engine_model,department1,employee1


class car_serializer(ModelSerializer):
    class Meta:
        model = car_model
        fields = '__all__'
        depth = 1


class engine_serializer(ModelSerializer):
    class Meta:
        model = engine_model
        fields = '__all__'

#
# class department_serialzer(ModelSerializer):
#     class Meta:
#         model = d_epartment
#         fields = '__all__'
#         depth=1
#
#
# class employee_serializer(ModelSerializer):
#     class Meta:
#         model = e_mployee
#         fields = '__all__'

class department1_serialzer(ModelSerializer):
    class Meta:
        model = department1
        fields = '__all__'
        depth=1


class employee1_serializer(ModelSerializer):
    class Meta:
        model = employee1
        fields = '__all__'

