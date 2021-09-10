from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import QuestionSerializer, ChoiceSerializer

from polls.models import Question, Choice


@api_view(["GET","POST"])
def question_list(request):
    if request.method=="GET":
        questions=Question.objects.all()
        serializer=QuestionSerializer(questions,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET","POST"])
def choice_list(request):
    if request.method=="GET":
        choices=Choice.objects.all()
        serializer=QuestionSerializer(choices,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
