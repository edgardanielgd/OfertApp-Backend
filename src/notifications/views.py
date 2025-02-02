from .serializers import NotificationSerializer
from .models import Notification
from rest_framework.views import APIView, Response

class NotificationView( APIView ):

    def get( self, request ):

        # Check if user is logged in
        if not request.user.is_authenticated:
            return Response(
                status=200,
                data={
                    "status": "error",
                    "error": "User is not authenticated"
                }
            )

        notifications = Notification.objects.filter( user = request.user )
        serializer = NotificationSerializer( notifications, many = True )
        return Response( serializer.data )
