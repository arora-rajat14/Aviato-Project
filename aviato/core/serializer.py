from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            "id",
            "name",
            "age",
            "gender",
            "email",
            "phone_number",
            "created_at",
            "modified_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "modified_at",
        ]
