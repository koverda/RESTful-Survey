from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from surveys.models import Survey
from surveys.permissions import IsOwnerOrReadOnly
from surveys.serializers import SurveySerializer, UserSerializer
from django import forms # needed for radio button


class SurveyViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents surveys.


    The **recommend_company** field asks how strongly they would 
    recommend this company to a friend, from 1 to 10.

    The **what_changes** field asks the user what changes they would
    make to the product, free-form text.

    The **was_researched** field asks the user whether or not they
    researched the product before purchasing, yes or no.

    The **feedback** field asks the user for any additional feedback.
    This field is optional.
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (IsOwnerOrReadOnly, 
                          permissions.IsAuthenticatedOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.

    As you can see, the collection of survey instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
