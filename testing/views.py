from django.shortcuts import render
from django.http import HttpResponse
from testing.models import Typo, Doctor
from api import views
# from rest_framework import viewsets
# from rest_framework import status, permissions
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from testing.serializers import TypoSerializer, DoctorSerializer

# Create your views here.
# class TypoViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Typo.objects.all()
#     serializer_class = TypoSerializer


# class DoctorViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer

#@api_view(['GET', 'POST'])
#@permission_classes((permissions.AllowAny,))
def detail(request, typesofDoctor_name):
  value = Typo.objects.get(pk = typesofDoctor_name)
  #return render(request, 'testing/details.html', {'value': value})
  return views.doctor_list(request, typesofDoctor_name)

def index(request):
    typesofDoctor = Typo.objects.all()
    return render(request, 'testing/index.html', {'typesofDoctor': typesofDoctor})