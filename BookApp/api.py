from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import BookModel
from rest_framework import serializers

from django.contrib.auth import authenticate


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'

    def validate(self, data):
        price = data['price']
        if price < 0:
            raise serializers.ValidationError('Price cannot be negative')
        return data

@api_view(['GET'])
def BookListApi(request):
    if not request.user.is_authenticated:
        return Response({
            'message': 'Please login to view books'
        })
    #fetch from db 
    books = BookModel.objects.all()
    
    serializer = BookModelSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def BookCreateApi(request):
    data = request.data

    serializer = BookModelSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Book created successfully'
        })
    else:
        return Response(serializer.errors)
    


@api_view(['PUT'])
def BookUpdateApi(request, id):
    #with serializer
    data = request.data
    try:
        book = BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        raise NotFound('Book not found')
    serializer = BookModelSerializer(instance = book, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Book updated successfully'
        })
    else:
        return Response(serializer.errors)

    # # get data from request
    # data = request.data
    # name = data.get('name')
    # author = data.get('author')
    # year = data.get('year')
    # price = data.get('price')
    
    # # update in db
    # book = BookModel.objects.get(id=id)
    # book.name = name
    # book.author = author
    # book.year = year
    # book.save()
    # return Response({
    #     'message': 'Book updated successfully'
    # })

@api_view(['DELETE'])
def BookDeleteApi(request, id):
    # check if book exist
    if not BookModel.objects.filter(id=id).exists():
        return Response({
            'message': 'You cannot delete what does not exist'
        })
    else:
        # delete from db
        book = BookModel.objects.get(id=id)
        book.delete()
        
        return Response({
            'message': 'Book deleted successfully'
        })