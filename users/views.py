from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    # Vérifie si la requête est une requête POST (données soumises par le formulaire)
    if request.method == 'POST':
        # Crée une instance du formulaire qui recupere les donnees soumises par l'utilisateur puis  on ...
        form = RegisterForm(request.POST)

        # Vérifie si les données soumises sont valides puis on ...
        if form.is_valid():
            # Sauvegarde le nouvel utilisateur dans la base de données puis on...
            form.save()
            # Récupère le nom d'utilisateur depuis les données nettoyées du formulaire
            username = form.cleaned_data.get('username')
            # Affiche un message de succès pour l'utilisateur
            messages.success(request, f'Welcome {username}, your are currentrly log in')
            # Redirige l'utilisateur vers la page d'accueil des aliments après l'inscription
            return redirect('login')
        # Si le formulaire n'est pas valide, affiche le formulaire avec les erreurs
        else:
            # En option : Ajoute un message d'erreur si le formulaire est invalide
            messages.error(request, 'Please correct the errors below.')

    # Si ce n'est pas une requête POST (donc une requête GET), ou le formulaire est invalide
    else:
        # Crée une nouvelle instance vide du formulaire pour une requête GET
        form = RegisterForm()

    # Rend le template avec le formulaire (qu'il soit vide ou avec des erreurs)
    return render(request, 'users/register.html', {'form': form})



@login_required
def profile_user(request):

    return render(request,"users/profile_user.html",{})


























# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Sauvegarde le nouvel utilisateur
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Welcome {username}, your account is created')
#             return redirect('food:index')
#     else:
#         form = UserCreationForm()  # Initialise le formulaire pour les requêtes GET
#
#     return render(request, 'users/register.html', {'form': form})
#
#
#












#
#
#
# Analyse du Code
# Le code actuel est :
#
# python
# Copy code
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
#
# def register(request):
#     form = UserCreationForm(request.POST)  # Initialisation du formulaire avec POST ici
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()  # Sauvegarde le nouvel utilisateur
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Welcome {username}, your account is created')
#             return redirect('food:index')
#     else:
#         form = UserCreationForm()  # Réinitialisation du formulaire pour les requêtes GET
#
#     return render(request, 'users/register.html', {'form': form})
# Problème
# Initialisation de form avant la condition POST :
#
# form = UserCreationForm(request.POST) est initialisé au début de la vue, ce qui signifie que même pour une requête GET, il essaiera de traiter les données POST, ce qui n'est pas approprié.
# Logique du bloc else :
#
# Si la requête est une POST mais le formulaire est invalide, il est toujours possible que le formulaire ne soit pas réinitialisé correctement pour les requêtes ultérieures, ce qui peut poser problème.
# Correction du Code
# Il est préférable d'initialiser form dans les blocs conditionnels appropriés pour éviter tout traitement incorrect des données POST lorsqu'une requête GET est effectuée. Voici le code corrigé :
#
# python
# Copy code
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
#
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Sauvegarde le nouvel utilisateur
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Welcome {username}, your account is created')
#             return redirect('food:index')
#     else:
#         form = UserCreationForm()  # Initialise le formulaire pour les requêtes GET
#
#     return render(request, 'users/register.html', {'form': form})
# Explication de la Correction
# Initialisation de form dans le Bloc POST :
#
# Lorsqu'une requête POST est reçue, form est initialisé avec UserCreationForm(request.POST). Cela traite correctement les données soumises.
# Initialisation de form dans le Bloc else :
#
# Pour les requêtes GET ou les requêtes POST avec des erreurs de validation, form est réinitialisé à une nouvelle instance de UserCreationForm(). Cela garantit que tu obtiennes un formulaire vide pour les requêtes GET ou pour redistribuer le formulaire après des erreurs.
# Résumé
# Initialise form dans le bloc POST pour les requêtes POST.
# Initialise form dans le bloc else pour les requêtes GET ou lorsque le formulaire est invalide.
# Avec cette approche, tu t'assures que le formulaire est toujours correctement défini et approprié à chaque type de requête.