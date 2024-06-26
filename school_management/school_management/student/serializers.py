from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Students


class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200, required=True)
    address = serializers.CharField(max_length=200, required=True)
    roll_number = serializers.IntegerField()
    mobile = serializers.CharField(max_length=10, required=True)
    user = serializers.ReadOnlyField(source='user.username')


    def create(self, validated_data):
        print(validated_data, "-------In Serializer Create function ------------")
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.mobile = validated_data.get('mobile', instance.mobile)

        instance.save()

        return instance


    class Meta:
        model = Students
        fields = ('__all__')



class UserSerializer(serializers.ModelSerializer):
    # Students = serializers.PrimaryKeyRelatedField(many=True, queryset=Students.objects.all())

    class Meta:
        model = User
        fields = ('__all__')

