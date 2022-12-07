from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def getTodos(request):
    todos= Todo.objects.all()
    serializer= TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTodo(request, pk):
    todo= Todo.objects.get(id=pk)
    todo.delete()
    return Response("Todo succesfully deleted!")

@api_view(['POST'])
def addTodo(request):
    serializer= TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        emessage=serializer.errors
        print(emessage)
        return Response({
                'status': 'Bad request',
                'message': emessage,
            }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def updateTodo(request, pk):
    todo= Todo.objects.get(id=pk)
    serializer= TodoSerializer(instance= todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        emessage=serializer.errors
        print(emessage)
        return Response({
                'status': 'Bad request',
                'message': emessage,
            }, status=status.HTTP_400_BAD_REQUEST)
