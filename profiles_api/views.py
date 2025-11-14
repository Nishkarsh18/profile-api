from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import models
from profiles_api import serializers
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import viewsets

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
        
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'mssg':"PUT"})        

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'mssg':"DELETE"})        

    def patch(self,request,pk=None):
        """Handle partial update an object"""
        return Response({'mssg':"PATCH"})        
    


class HellowViewSet(viewsets.ViewSet):

    def list(self,request):
        a_viewset = [
            'uses actions (list)',
            'easy to use',
            'simple operations'
        ]

        return Response({"mssg":"viewset","ss":a_viewset})
    def create(self,request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'mssg':message})
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Getting object by id"""
        return Response({"mssg","fetch"})    
    
    def update(self,request,pk=None):
        return Response({"mesage","update"})
    
    def partial_update(self,request,pk=None):
        return Response({"mssg","partial"})
    
    def destroy(self,request,pk=None):
        return Response({"mssg":"delete"})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    