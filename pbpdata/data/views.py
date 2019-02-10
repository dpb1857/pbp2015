
# Find pylint codes at: http://pylint-messages.wikidot.com/all-codes
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=superfluous-parens

from rest_framework import generics

from data.models import Control

from data.serializers import ControlSerializer


# Create your views here.


class ControlList(generics.ListAPIView):
    queryset = Control.objects.all()  # pylint: disable=no-member
    serializer_class = ControlSerializer
