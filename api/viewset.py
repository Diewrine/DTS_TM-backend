from rest_framework import viewsets, permissions
from .models import Member
from .serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):    
    permission_classes = [
    permissions.AllowAny
    ]
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)



"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
    permissions.AllowAny
    ]
    serializer_class = UserSerializer
"""