from rest_framework import viewsets
from rest_framework.response import Response

from Q_engine.serializers import QuestionSerializer
from Q_engine.views import QuestionAnswer


class QuestionAnswerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = QuestionAnswer.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


