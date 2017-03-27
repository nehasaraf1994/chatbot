from django.shortcuts import render
from django.http import HttpResponse
from testing.models import Typo, Doctor
from rest_framework import viewsets
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.serializers import TypoSerializer, DoctorSerializer

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

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def doctor_list(request, typesofDoctor_name):

    if request.method == 'GET':
        doctors = Doctor.objects.filter(desgn = typesofDoctor_name)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        data = {
                  'ndoc': request.data['ndoc'],
                  'desgn': request.data['desgn'],
                  'doc_id': request.data['doc_id']
               }
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
