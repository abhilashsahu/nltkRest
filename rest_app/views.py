from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rake_nltk import Rake

class NLTKAPIView(APIView):
    """ Class to handle .../nltk/ endpoint POST requests """

    @staticmethod
    def post(request):
        """ Method to create new project in the DB  """

        rake_nltk_var = Rake()
        text = request.data.get("text", None)

        rake_nltk_var.extract_keywords_from_text(text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()

        response_dict = {"keywords": keyword_extracted}

        return Response(response_dict, status=status.HTTP_200_OK)

