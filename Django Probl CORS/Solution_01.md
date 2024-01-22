from django.http import JsonResponse

def get_csrf_token(request):
    # Votre logique pour récupérer le jeton CSRF
    csrf_token = 'votre_token_csrf'

    # Créez une réponse JSON avec le jeton CSRF et les en-têtes CORS appropriés
    response = JsonResponse({'csrf_token': csrf_token})
    response["Access-Control-Allow-Origin"] = "http://localhost:5173"  # Remplacez par l'URL de votre application Svelte
    response["Access-Control-Allow-Methods"] = "GET"
    response["Access-Control-Allow-Headers"] = "content-type"

    return response