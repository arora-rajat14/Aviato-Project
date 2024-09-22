from rest_framework import viewsets
from .models import Candidate
from .serializer import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing candidate instances.
    """

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
