from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import UserData
from .serializers import UserDataSerializer
from django.core.mail import send_mail


class UserDataCreateView(CreateModelMixin,
                         ListModelMixin,
                         GenericViewSet):
    queryset = UserData.objects.order_by('-id')
    serializer_class = UserDataSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            print('Sending email to',
                  serializer.data['name'], 'at', serializer.data['email'])
            try:
                send_mail(
                    f'Hey {serializer.data["name"]}',
                    'Thank you for your submission.',
                    'from@userform.com',
                    ['vsreejeet@gmail.com']
                )
                print(f"Email sent")
            except Exception as e:
                print(f"Exception while sending email: ", str(e))
