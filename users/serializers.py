from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        fields = (
            'first_name',
            'last_name',
            'email',
            'delivery_address',
            'phone_number',
        )
        model = User
