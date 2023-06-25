from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, AccessToken

# ログイン処理
class LoginSerializer(serializers.Serializer):
    userid = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        userid = data.get('userid')
        password = data.get('password')
        re_userid = User.objects.get(userid=userid)
        re_password = User.objects.get(password=password)
        if userid == re_userid.userid:
            if password == re_password.password:
                return data

            else:
                raise serializers.ValidationError('ログイン失敗')



# ここのUserSerialzerは全てのフィールドを表すシリアルライザー
# このシリアルライザーを使用するとUserモデルの全てのフィールドを表示
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userid', 'name', 'email','introduction']
        extra_kwargs = {'password': {'write_only': True}}



# これは新規登録用のシリアルライザー、新規登録に必要なフィールドだけを記述
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userid','name','email','password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user

# Update用のシリアライザー        
class UserUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, allow_blank=True)
    introduction = serializers.CharField(max_length=100, allow_blank=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.save()
        return instance

# Delete用のシリアルいざー
class CloseAccountSerializer(serializers.Serializer):
    message = serializers.CharField(default="Account and user successfully removed")