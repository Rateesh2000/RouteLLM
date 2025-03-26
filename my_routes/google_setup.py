import google.genai as genai

client = genai.Client(api_key="AIzaSyCxlO5qac9RsUfe-1Iit6O7aSY8WAqZqBA")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)