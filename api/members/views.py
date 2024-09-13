from api.members.models import Member
from rest_framework import permissions, viewsets

from api.members.serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Members to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('first_name')
    serializer_class = MemberSerializer
    #permission_classes = [permissions.IsAuthenticated]
