from testapp.models import EmployeeModel
from rest_framework.viewsets import ModelViewSet
from testapp.serializers import EmployeeSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class EmployeeCRUD(ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
