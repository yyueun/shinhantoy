from django.shortcuts import render
from .models import Member 
from .serializers import MemberSerializer
from rest_framework import mixins, generics, status
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.permissions import IsAuthenticated


#signup 
class RegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = MemberSerializer
   
    #쿼리셋 생략


    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs) #생성 



class ChangePW(APIView):
    permission_classes = [IsAuthenticated]  #


    def put(self,request,*args,**kwargs):
        password = request.data.get('password')
        change_password = request.data.get('change_password') #변경 비밀번호
        change_password2 = request.data.get('change_password2') #변경 비밀번호 한번 더
    #step1
        if change_password != change_password2 :
            return Response({
                'detail':'Wrong new password'
            },status=status.HTTP_400_BAD_REQUEST)

        member = request.user
    #step4 checkpassword 함수를 사용해서 암호호된 비밀번호와 맞는지 확인하기 
        if  not check_password(password,member.password):  #패스워드랑 멤버의 있는 패스워드랑 같은지 확인하기 -> 일치하지않으면
            return Response({
                'detail': 'Wrong password'
            },status=status.HTTP_400_BAD_REQUEST)
        


    #step5 makepassword를 이용해서  새로운 비밀번호 입력하고 멤버의 비밀번호에 저장하기
        member.password = make_password(change_password)
        member.save()
        return Response(status=status.HTTP_200_OK)
    
#member urls에서   /password경로로 전달하기