from django.shortcuts import render

# Create your views here.
from tokenapp.models import Employee
from tokenapp.serializers import EmployeeSerializer
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import  IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

###costom permission##
from tokenapp.permissions import IsReadOnly,OnlyGETOrPatch,Custom
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.authentication  import JSONWebTokenAuthentication
from tokenapp.authentications import CustomAuthentication



class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes =[CustomAuthentication]
    permission_classes = [IsAuthenticated,]



