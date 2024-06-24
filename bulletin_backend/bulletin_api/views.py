from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bulletin
from .serializers import BulletinResponseSerializer, BulletinInputSerializer


@api_view(['GET'])
def list_all_bulletins(request):
    bulletins = Bulletin.objects.all()
    serializer = BulletinResponseSerializer(bulletins, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_bulletin(request):
    serializer = BulletinInputSerializer(data=request.data)
    if serializer.is_valid():
        bulletin = serializer.save()
        return Response(BulletinResponseSerializer(bulletin).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_bulletin(request, bulletin_id):
    try:
        bulletin = Bulletin.objects.get(pk=bulletin_id)
    except Bulletin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BulletinResponseSerializer(bulletin)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BulletinResponseSerializer(bulletin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bulletin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

