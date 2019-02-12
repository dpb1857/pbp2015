
# Find pylint codes at: http://pylint-messages.wikidot.com/all-codes
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=superfluous-parens

from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from data.models import Control, Rider, Timestamp

from data.serializers import ControlSerializer, RiderSerializer, TimestampSerializer


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

    The list is paginated with LimitOffsetPagination, use 'limit' and 'offset'
    parameters to select a portion of list.
    """
    class RiderPagination(LimitOffsetPagination):
        default_limit = 50

    pagination_class = RiderPagination
    serializer_class = RiderSerializer

    def get_queryset(self):
        request = self.request
        queryset = Rider.objects.all() # pylint: disable=no-member
        for key in ["plaque", "startgroup", "lastname", "country", "club"]:
            if key in request.query_params:
                qexpr = None
                for val in request.query_params.getlist(key):
                    if qexpr is None:
                        qexpr = Q(**{key: val})
                    else:
                        qexpr = qexpr | Q(**{key: val})
                queryset = queryset.filter(qexpr)

        return queryset

class RiderDetail(generics.RetrieveAPIView):
    queryset = Rider.objects.all() # pylint: disable=no-member
    serializer_class = RiderSerializer

class TimestampList(generics.ListAPIView):
    """
    The timestamp list can be filtered with the following url parameters:
    * plaque
    * control
    * start     # timestamp >= start
    * end       # timestamp < end

    plaque and control can be repeated to do an OR of all of the values.

    The list is paginated with LimitOffsetPagination, use 'limit' and 'offset'
    parameters to select a portion of list.
    """
    class TimestampPagination(LimitOffsetPagination):
        default_limit = 100

    pagination_class = TimestampPagination
    serializer_class = TimestampSerializer

    def get_queryset(self):
        request = self.request
        queryset = Timestamp.objects.all() # pylint: disable=no-member
        for key in ["plaque", "control"]:
            if key in request.query_params:
                qexpr = None
                for val in request.query_params.getlist(key):
                    if qexpr is None:
                        qexpr = Q(**{key: val})
                    else:
                        qexpr = qexpr | Q(**{key: val})
                queryset = queryset.filter(qexpr)

        if "start" in request.query_params:
            queryset = queryset.filter(timestamp__gte=request.query_params["start"])

        if "end" in request.query_params:
            queryset = queryset.filter(timestamp__lt=request.query_params["end"])

        queryset = queryset.order_by("timestamp")
        return queryset
