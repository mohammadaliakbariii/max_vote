from rest_framework import serializers
from polls.models import Question,Choice



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields="__all__"


class ChoiceSerializer(serializers.ModelSerializer):
    question_text=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="question_list"
    )
    class Meta:
        model= Choice
        fields = "__all__"



