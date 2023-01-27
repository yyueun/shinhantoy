from rest_framework import serializers
from .models import Order,Comment



class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


#comment를 보여주는 것 
class CommentSerializer(serializers.ModelSerializer): 
    #method필드를 만듦(함수필드) 내가 만든 함수(밑에 함수) 안에서 찾아 쓴다는 것
    member_username = serializers.SerializerMethodField() 
    tstamp = serializers.DateTimeField(  #날짜 타입 설정
        read_only = True, format = '%Y-%m-%d %H:%M:%S' 
    )

    #위의member_username의 method에서 이걸 씀, obj는 쿼리셋 결과의 객체 / 멤버를 가지고 있음 
    #views에서 CommentListView와 같이 사용하고 있기 때문에 여기서는 쿼리셋을 가져오지 않아도 됨 
    #view에서 쿼리셋을 가져오기 때문에 그걸 바탕으로 serializer가 사용함 
    #----------obj---------------------------
    def get_member_username(self,obj): 
        return obj.member.username


    class Meta:
        model = Comment  
        fields = '__all__'

#commentcreateserializer 생성 
class CommentCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField( 
        default=serializers.CurrentUserDefault(),  
        required=False #유효성검증할때 없어도된다는 것, 필수값 x
    )
    #HiddenField를 하면 연결이 끊겨 멤버가 숨겨짐
    #CurrentUserDefault 기본값을 지정해서 세팅(사용자 정보를 바로 넣을 수 있게 됨 )

    class Meta:
        model = Comment 
        fields = '__all__'
   
