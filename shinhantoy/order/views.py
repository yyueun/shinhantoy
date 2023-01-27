from rest_framework import generics, mixins
from rest_framework.views import APIView
from .serializers import OrderSerializer, CommentCreateSerializer, CommentSerializer
from .models import Order,Comment
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    #쿼리셋 세팅
    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    #쿼리셋을 통해 함수 연결 (가져오기)
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

#상세보기 -view를 만들어야하고 하나의 주소와 연결해야함 
# ListModelMixin(리스트만들기)을 넣게 되면 주소에 문제가 생김(만든 뷰는 하나의 주소와 매핑되어야하는데 같은 주소에 여러개가 생김)


class OrderDetailView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin 

):
    serializer_class = OrderSerializer

    def get_queryset(self): #order반환 - 쿼리셋 세팅 : 알아서 get을 해줌 
        return Order.objects.all().order_by('id')

#-------------------list와 retrieve 차이 -----------------
    def get(self,request,*args,**kwargs): #가지고오는 건 retrieve여야함  
        return self.retrieve(request, args, kwargs)


#댓글 리스트  --- 상품리스트와 같음 
class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView, 
): 
    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id') #order_id가져오기
        if order_id: #order id 가져오기 - 있으면 
            #-----------order_id = order_id ------- 앞의 order_id가 변수명인가
            return Comment.objects.filter(order_id=order_id).order_by('-id')
                
        return Comment.objects.none()


    #get으로 띄우기 
    def get(self,request,*args,**kwargs):

        return self.list(request, args, kwargs)

  


#comment 생성
class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

#----------전달 안했을 때 사용하는 것 !------------- 
    permission_classes = [IsAuthenticated] #유저네임 안쓰고 토큰으로 로그인하기 -- 로그인 안한 사용자에 대한 예외 처리가 됨 
    serializer_class = CommentCreateSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request, args, kwargs)



#views를 만들면 -> urls수정

 





