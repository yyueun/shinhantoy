from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer
from rest_framework import mixins, generics
from .paginations import OrderLargePagination
# Create your views here.


class OrderView(
    mixins.ListModelMixin,
    generics.GenericAPIView

):
    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination 



    def get_queryset(self):
        return Order.objects.all()


    def get(self,request,*args,**kwargs):
        return self.list(request, args, kwargs)
    