from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count, Q
from .models import Candidate
from .serializer import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing candidate instances.
    """

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request):
        """
        Custom search API endpoint that searches candidates by their name
        and returns results ordered by relevancy.
        """
        query = request.query_params.get("q", "").strip()

        if not query:
            return Response(
                {"detail": "Please provide a search query."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        search_terms = query.split()

        query_filter = Q()
        for term in search_terms:
            query_filter |= Q(name__icontains=term)

        candidates = Candidate.objects.filter(query_filter).annotate(
            relevancy=Count("name", filter=Q(name__icontains=search_terms[0]))
        )
        candidates = sorted(
            candidates,
            key=lambda candidate: sum(
                1 for term in search_terms if term.lower() in candidate.name.lower()
            ),
            reverse=True,
        )
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
