from rest_framework.response import Response
from rest_framework.decorators import api_view
from  base.models import Item
from .serializer import ItemSerializer


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializedValue = ItemSerializer(items, many=True)
    return Response(serializedValue.data)



@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['GET'])
def getByID(request,id):
   # id = request.query_params
    result = Item.objects.filter(id=id)
    serializedValue = ItemSerializer(result, many=True)
    return Response(serializedValue.data)