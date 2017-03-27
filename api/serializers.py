from testing.models import Typo, Doctor
from rest_framework import serializers


class TypoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typo
        fields = ('name')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('ndoc', 'desgn', 'doc_id')