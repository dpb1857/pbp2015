
# Find pylint codes at: http://pylint-messages.wikidot.com/all-codes
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=superfluous-parens

from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response

from data.models import Control, Rider

from data.serializers import ControlSerializer, RiderSerializer


# Create your views here.

class ControlList(generics.ListAPIView):
    queryset = Control.objects.all()  # pylint: disable=no-member
    serializer_class = ControlSerializer

class ControlDetail(generics.RetrieveAPIView):
    queryset = Control.objects.all()  # pylint: disable=no-member
    serializer_class = ControlSerializer

class RiderList(generics.ListAPIView):
    """
    The rider list can be filtered with the following url parameters:
    * plaque
    * startgroup
    * lastname
    * country
    * club

    Repeating a parameter multiple times will do an OR of all of the values.

    """
    queryset = Rider.objects.all()  # pylint: disable=no-member
    serializer_class = RiderSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for key in ["plaque", "startgroup", "lastname", "country", "club"]:
            if key in request.query_params:
                qexpr = None
                for val in request.query_params.getlist(key):
                    if qexpr is None:
                        qexpr = Q(**{key: val})
                    else:
                        qexpr = qexpr | Q(**{key: val})
                queryset = queryset.filter(qexpr)

        serializer = RiderSerializer(queryset, many=True)
        return Response(serializer.data)

class RiderDetail(generics.RetrieveAPIView):
    queryset = Rider.objects.all()  # pylint: disable=no-member
    serializer_class = RiderSerializer
