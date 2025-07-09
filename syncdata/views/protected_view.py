from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Access granted!",
            "user_id": request.user.id,
            "client_id": getattr(request.user, 'client_id', None)
        })
