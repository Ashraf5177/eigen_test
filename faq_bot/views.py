from django.shortcuts import render
from  rest_framework.views import APIView
from  rest_framework.response import Response
from  rest_framework.decorators import api_view
from django.core.cache import cache
from .serializers import FAQSerializer
import openai
import os


openai_api_key=os.getenv('OPENAI_API_KEY')

class FAQListView(APIView):
    def get(self,request):
        faqs=FAQ.objects.all()
        serializer=FAQSerializer(faqs,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def query_view(request):
    query=request.data.get('query')
    if not query:
        return Response({"error":"Query not provided."},status=400)
    cached_response=cache.get('query')
    if cached_response:
        return Response({"answer":cached_response},status=200)
    faqs=ModelFAQ.objects.all()
    for faq in faqs:
        if query.lower() in faq.question.lower() or any(keyword in faq.keywords):
            cache.set(query,faq_answer)
            return Response({"answer":cached_response},status=200)
    try:
        prompt=f"Answer the following question concinsely:/n{query}"
        llm_response=openain.Completion.create(
            engine='text-divinci-003',
            prompt=prompt,
            max_token=150
            )
        answer=llm.response.choices[0].text.strip()
        cache.set(query,answer)
        return Response({"answer":cached_response},status=200)
    except Exception as e:
        return Response({"error":"The system is temporarily unavailable. Please try again later."},status=500)


