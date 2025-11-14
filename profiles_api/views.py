from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """Reture lsit of apiview featurs"""
        an_apiview =[
            'uses',
            'django view similar',
            'more control'
        ]
        return Response({'message':'hell','an_apiview':an_apiview})
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'mssg':message})
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)