from django.shortcuts import render
from Book.models import Bookinfo

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def addBook(request):
    data = request.data
    try:
        Bookinfo.objects.create(  # ✅ fixed typo here
            book_name=data['book_name'],
            author=data['author'],
            price=data['price'],
            stock=data['stock'],
            category=data['category']
        )
        return Response({"message": "Book Created Successfully"}, status=status.HTTP_201_CREATED)

    except KeyError:
        return Response({"message": "Something Went Wrong"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def getBooks(request):
    obj=Bookinfo.objects.all().values()
    return Response(obj,status=status.HTTP_200_OK)

@api_view(['GET'])
def getById(request,pk):
    try:
        data=Bookinfo.objects.get(pk=pk)
        return Response({
            "book_name":data.book_name,
            "author":data.author,
            "price":data.price,
            "stock":data.stock,
            "category":data.category      

        },status=status.http_200_OK)
    except Bookinfo.DoesNotExist:
        return Response({"message":"Book Not Found"},status=status.HTTP_404_NOT_FOUND)

