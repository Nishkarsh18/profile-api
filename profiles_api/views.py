from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""

    def get(self,request,format=None):
        """Reture lsit of apiview featurs"""
        an_apiview =[
            'uses',
            'django view similar',
            'more control'
        ]
        return Response({'message':'hell','an_apiview':an_apiview})