from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai, os
import google.generativeai as genai

openai.api_key = os.getenv("OPENAI_API_KEY")

@api_view(["POST"])
def summarize(request):
    
    try:
        text = request.data.get("text", "")
        if not text:
            return Response({"error": "No text provided"}, status=400)

        '''
            Using Google Gemini API for summarization
        '''
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(f"Summarize this text:\n{text}")
        summary = response.text


        '''
            Using OpenAI API for summarization
        '''

        # completion = openai.chat.completions.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "system", "content": "You are a text summarizer."},
        #         {"role": "user", "content": f"Summarize this text:\n{text}"}
        #     ],
        #     max_tokens=150
        # )

        # summary = completion.choices[0].message.content.strip()
        return Response({"summary": summary})
    
    except Exception as e:
        return Response({"error": str(e)}, status=500)
