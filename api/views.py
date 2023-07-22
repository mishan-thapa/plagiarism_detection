from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
result_list = []
@api_view(['GET'])
def getData(request):
    person = {'name':"mishan",'age':22}
    return Response(result_list)



from rest_framework import status
from .models import words
from .serializers import pos_sentenceSerializer
from rest_framework.views import APIView
#from first_app.synset import find_synonyms
from first_app.synset import get_all_synonyms
from django.http import JsonResponse

class create_book(APIView):
    def post(self,request):
        print("abccccccc")
        data = request.data
        print(data)
        print(type(data))

        # Access the value for the "sentence" key
        sentence_value = data['sentence']
        print(sentence_value)
        rdata = get_all_synonyms(sentence_value)
        print(rdata)
        #return Response(status = status.HTTP_200_OK)
        return JsonResponse({'sentence': sentence_value, 'result_list': rdata})
    
        #serializer = pos_sentenceSerializer(data =request.data)
        #if serializer.is_valid():
        #    print("data is valid")
        #    serializer.save()
        #    return Response(serializer.data,status =status.HTTP_201_CREATED)
        #print("data is invalid")
        #return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST )
    def get(self,request):
        obj = words.objects.all()
        serializer = pos_sentenceSerializer(obj,many = True)
        return Response (serializer.data, status = status.HTTP_200_OK)


from first_app.pos_tagging import pos_tagging_function
class pos_tagging(APIView):
    def post(self,request):
        print("ccccc")
        data = request.data
        print(data)
        print(type(data))

        # Access the value for the "sentence" key
        sentence_value = data['sentence']
        print(sentence_value)
        if sentence_value is not None:
            print(sentence_value)
            tagged_words = pos_tagging_function(sentence_value)
            print(tagged_words)
            return JsonResponse({ 'result_list': tagged_words})
            return Response(status=status.HTTP_200_OK)
        else:
            # Handle the case when the "sentence" key is missing
            return Response({"error": "The 'sentence' key is missing in the request data."},status=status.HTTP_400_BAD_REQUEST)
        #rdata = get_all_synonyms(sentence_value)
        #print(rdata)
        return Response(status = status.HTTP_200_OK)
        #return JsonResponse({'sentence': sentence_value, 'result_list': rdata})
