from rest_framework import serializers
from .models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ('email', 'username', 'password', 'password2', 'first_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(_("Passwords must match."))
        return data

    def create(self, validated_data):
        validated_data.pop('password2', None)  # Remove password2 from validated data
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UsersSerializer(serializers.ModelSerializer): 
    image_url = serializers.SerializerMethodField()

    class Meta: 
        model = Account 
        fields = ('id', 'email', 'username', 'first_name', 'image', 'image_url', 'current_step', 'completed_all_steps')
        read_only_fields = ('id', 'current_step', 'completed_all_steps')  # Exemplo de campos somente leitura

    def get_image_url(self, obj):
        return obj.get_image_url()

