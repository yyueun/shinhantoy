from rest_framework import pagination

class OrderLargePagination(pagination.PageNumberPagination): #레스트프레임 워크 밑 페이지네이션 밑에 페이지넘버페이지네이션.
    
    page_size = 10000  
