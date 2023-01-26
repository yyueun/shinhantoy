from rest_framework import generics, mixins
from rest_framework.views import APIView
from .serializers import OrderSerializer, CommentCreateSerializer, CommentSerializer
from .models import Order,Comment
from rest_framework.response import Response

# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

#상세보기 
class OrderDetailView(
    mixins.ListModelMixin,
    generics.GenericAPIView,

):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self,request,*args,**kwargs):
        return self.list(request, args, kwargs)


#댓글 리스트 
class CommentListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView, 
): 
    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        if order_id:
            return Comment.objects.filter(order_id=order_id) \
                    .select_related('member','order') \
                    .order_by('-id')
        
        return Comment.objects.none()


    #post맨에 get으로 띄우기 
    def get(self,request,*args,**kwargs):

        return self.list(request, args, kwargs)

  


#comment 생성
class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentCreateSerializer

    
    def get_queryset(self):
        comments = Comment.objects.all()
        return comments

    def post(self,request,*args,**kwargs):
        return self.create(request, args, kwargs)

 





