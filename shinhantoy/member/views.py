from django.shortcuts import render
from .models import Member 
from .serializers import MemberSerializer
from rest_framework import mixins, generics


class RegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = MemberSerializer



    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)