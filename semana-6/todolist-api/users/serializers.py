from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField
from .models import User
from django.contrib.auth.hashers import make_password

# Para un serializador customizado
class UserLoginSerializer(Serializer):
    email = EmailField(required=True)
    password = CharField(required=True)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    # validated_data es la informacion que el usuario esta enviando
    def create(self, validated_data):
        # si esl password existe entonces hashealo
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data['password'])
        return super().create(validated_data)
