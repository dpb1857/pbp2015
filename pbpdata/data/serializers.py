
# Find pylint codes at: http://pylint-messages.wikidot.com/all-codes
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=superfluous-parens

from rest_framework import serializers

from data.models import Control

class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('id', 'seq', 'name', 'distance', 'inbound')
