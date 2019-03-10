from rest_framework import serializers
from models import DownVote

class DownVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownVote
        fields = "__all__"
