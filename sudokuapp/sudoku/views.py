from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PuzzleSerializer
from .models import Puzzle


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


@api_view(['GET', 'POST'])
def puzzle_element(request, pk):
    try:
        puzzle = Puzzle.objects.get(pk=pk)
    except Puzzle.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PuzzleSerializer(puzzle)
        return Response(serializer.data)
    elif request.method == 'POST':
        puzzle.set_data(request.POST['data'])
        serializer = PuzzleSerializer(puzzle)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)






