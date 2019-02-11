
# Find pylint codes at: http://pylint-messages.wikidot.com/all-codes
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=superfluous-parens

from rest_framework import serializers

from data.models import Control, Rider, Timestamp

class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('id', 'location_id', 'name', 'distance', 'inbound')

class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ('plaque', 'startgroup', 'firstname', 'lastname', 'gender', 'country', 'club', 'velo', 'time')

class TimestampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timestamp
        fields = ('plaque', 'control', 'timestamp')
