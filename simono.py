from nicegui import ui
import random
import os

# Liste de citations inspirantes
citations = [
    "Les choses sont comme elles doivent être. Accepte-les.",
    "Ce qui ne dépend pas de toi ne mérite pas ton inquiétude.",
    "L’important n’est pas de changer le monde, mais de changer sa façon d’y vivre.",
    "Adapte-toi à ce que tu ne peux pas contrôler. C’est là que commence la paix.",
    "Accepter, c’est le premier pas vers la liberté intérieure.",
    "La sagesse commence par l'acceptation.",
    "Quand tu ne peux plus avancer, repose-toi, mais ne résiste pas."
]

# Page principale
@ui.page('/')
def main_page():
    # Style global du body (dégradé et typographie)
    ui.query('body').style('''
        background: linear-gradient(to bottom right, #f0f4f8, #d9e2ec);
        color: #2f3e46;
        font-family: "Helvetica Neue", Arial, sans-serif;
    ''')

    # Colonne centrée verticalement et horizontalement
    with ui.column().classes('items-center justify-center min-h-screen px-4'):
        # Titre principal
        ui.label('🌿 Réflexion du jour').classes('text-5xl font-extrabold mb-6 text-green-800')
        
        # Citation aléatoire
        citation = random.choice(citations)
        ui.label(f'"{citation}"').classes(
            'italic text-xl text-gray-600 mb-8 max-w-2xl text-center'
        )

        # Zone de saisie
        question = ui.textarea(
            label='✍️ Que veux-tu changer aujourd’hui ?',
            placeholder="Écris ici ta pensée...",
            validation={'required': False}
        ).classes('w-full max-w-2xl mb-4 bg-white rounded-lg shadow-inner')

        # Label vide pour afficher la réponse
        reponse_label = ui.label().classes('text-2xl text-center max-w-2xl mt-4 text-blue-700')

        # Fonction d’analyse de la pensée
        def analyser():
            texte = question.value or ""
            # Mots-clés hors de contrôle
            mots_impossibles = ['le passé', 'les autres', 'la météo', 'mes parents', 'le système']
            if any(mot in texte.lower() for mot in mots_impossibles):
                reponse_label.text = "❌ Tu ne peux pas le changer. Accepte et adapte-toi avec sérénité. 🌌"
            elif texte.strip() == "":
                reponse_label.text = "🕊️ Prends un moment pour écrire, même un mot peut être libérateur."
            else:
                reponse_label.text = "✅ Tu peux probablement agir. Agis avec sagesse et courage ⚡️"

        # Bouton d’analyse
        ui.button(
            "✨ Puis-je le changer ?",
            on_click=analyser
        ).classes('bg-green-600 text-white rounded-2xl px-8 py-3 hover:bg-green-700 shadow-lg')

# Démarrage de l’application
if __name__ == '__main__':
    # Pour déploiement en ligne, on peut définir HOST et PORT via variables d'environnement
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8080))
    ui.run(
        title='Simono - Acceptation et Adaptation',
        host=host,
        port=port,
        reload=False
    )
