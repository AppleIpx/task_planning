from django.contrib.auth.hashers import make_password
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from users.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from task_plan.models import TaskPlan
from .serializers import (
    CreateTaskPlanSerializers,
    ShowTaskPlanSerializer,
)


# ------start_users--------

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @action(
        methods=["get"],
        detail=False,
        permission_classes=(IsAuthenticatedOrReadOnly,)
    )
    def me(self, request):
        user = get_object_or_404(
            User,
            pk=request.user.id
        )
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def perform_create(self, serializer):
        if "password" in self.request.data:
            password = make_password(self.request.data["password"])
            serializer.save(password=password)
            # thanks_for_sing_up.delay(
            #     serializer.data.get("first_name"),
            #     serializer.data.get("email"),
            # )
        else:
            serializer.save()


# ------end_users----------


# ------start_taks---------


class TasksPlanView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return TaskPlan.objects.all()
        else:
            return TaskPlan.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        method = self.request.method
        if method == "POST" or method == "PATCH":
            return CreateTaskPlanSerializers
        else:
            return ShowTaskPlanSerializer
# ------end_taks-----------
