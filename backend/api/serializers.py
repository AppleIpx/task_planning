from django.utils import timezone
from rest_framework import serializers
from users.models import User
from rest_framework.authtoken.models import Token
from task_plan.models import TaskPlan


# -----------start-user-------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )


class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source="key")

    class Meta:
        model = Token
        fields = ("token",)
# ----------end-user-------------

# ---------start-task_plan-------


class CreateTaskPlanSerializers(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True,)

    class Meta:
        model = TaskPlan
        fields = [
            'id',
            'title',
            'text',
            'deadline',
            'created_at',
            'categories',
        ]
        read_only_fields = ('user',)

    def validate(self, data):
        deadline = data.get('deadline')
        if deadline and deadline < timezone.now():
            raise serializers.ValidationError('Выбранное время не может быть прошедшим.')

        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['is_it_ready'] = False
        if 'categories' not in validated_data:
            validated_data['categories'] = None
        return super().create(validated_data)


class ShowTaskPlanSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = TaskPlan
        fields = '__all__'

# ---------end-task_plan--------