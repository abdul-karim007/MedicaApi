from rest_framework import serializers
from userdata.models import userData

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = "__all__"