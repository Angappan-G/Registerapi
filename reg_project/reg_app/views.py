# import imp
# from django.shortcuts import render
# import os
# from django.conf import settings
# from django.template.loader import render_to_string
# from rest_framework_simplejwt.tokens import RefreshToken
# import jwt
# from rest_framework.views import APIView, Response
# from datetime import datetime, timedelta, timezone
# from django.contrib.auth.hashers import make_password
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from .models import Register
# from .serializers import RegisterSerializer

# # from rest_framework_swagger.views import get_swagger_view



# @api_view(['GET'])
# def get(request):
#     reg = Register.objects.all()
#     serializer = RegisterSerializer(reg,many=True)
#     return Response(serializer.data)




# @api_view(['POST'])
# def createuser(request):
#     serialzier =  RegisterSerializer(data=request.data)
#     data = {}
#     if serialzier.is_valid():
#         serialzier.save()

#     else:
#         return Response(serialzier.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def reg(request, pk):
#     reg = reg.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = RegisterSerializer(reg)
#         return Response(serializer.data)

#     if request.methosd == 'PUT':
#         serializer = RegisterSerializer(reg,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         else:
#             return serializer.errors

#     if request.method == 'DELETE':
#         return Response(serializer.data)


from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status    
from .models import Register


class RegisterUser(APIView):
        def get(self,request):
            reg = Register.objects.all()
            serializer = RegisterSerializer(reg,many=True)
            return Response(serializer.data)

class CreateUser(APIView):
    def post(self,request):
        serialzier =  RegisterSerializer(data=request.data)
        data = {}
        if serialzier.is_valid():   
            serialzier.save()

        else:
            return Response(serialzier.errors,status=status.HTTP_400_BAD_REQUEST)

class Users(APIView):
    def get_user_by_pk(self,pk):
        try:
            return Register.objects.get(pk=pk)
        except:
            return Response ({
                'error': 'User does not exist'
            },status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk):
        reg = self.get_user_by_pk(pk)
        serializer = RegisterSerializer(reg)
        return Response(serializer.data)

    def put(self,request,pk):
        reg = self.get_user_by_pk(pk)
        if request.method == 'PUT':
            serializer = RegisterSerializer(reg,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            else:
                return serializer.errors

    def delete(self,request,pk):
            reg = self.get_user_by_pk(pk)
            reg.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)