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

# Réponses motivantes
reponses_possibles = [
    "✅ Tu peux probablement agir. Agis avec sagesse et courage ⚡️",
    "🔥 Tu as le pouvoir de changer cela. Une action à la fois 💪",
    "🌱 C’est entre tes mains. Cultive le changement avec patience.",
    "🚀 Lance-toi, tu es plus capable que tu ne le crois.",
    "🛠️ Tu peux façonner ta réalité. Commence doucement, avance sûrement."
]

# Réponses d’acceptation
reponses_acceptation = [
    "❌ Tu ne peux pas le changer. Accepte et adapte-toi avec sérénité. 🌌",
    "🧘 Certaines choses échappent à ton contrôle. Trouve-y la paix.",
    "🌧️ Comme la pluie, certains événements surviennent. Respire, tout passe.",
    "🎈 Lâche prise. C’est dans l’acceptation que tu te libères.",
    "🌊 Sois comme l’eau : contourne ce que tu ne peux traverser."
]

# Page principale
@ui.page('/')
def main_page():
    ui.query('body').style('''
        background: linear-gradient(to bottom right, #f0f4f8, #d9e2ec);
        color: #2f3e46;
        font-family: "Helvetica Neue", Arial, sans-serif;
    ''')

    with ui.column().classes('items-center justify-center min-h-screen px-4'):
        ui.label('🌿 Réflexion du jour').classes('text-5xl font-extrabold mb-6 text-green-800')
        citation = random.choice(citations)
        ui.label(f'"{citation}"').classes('italic text-xl text-gray-600 mb-8 max-w-2xl text-center')

        question = ui.textarea(
            label='✍️ Que veux-tu changer aujourd’hui ?',
            placeholder="Écris ici ta pensée...",
            validation={'required': False}
        ).classes('w-full max-w-2xl mb-4 bg-white rounded-lg shadow-inner')

        reponse_label = ui.label().classes('text-2xl text-center max-w-2xl mt-4 text-blue-700')

        def analyser():
            texte = question.value or ""
            mots_impossibles = ['le passé', 'les autres', 'la météo', 'mes parents', 'le système']
            if any(mot in texte.lower() for mot in mots_impossibles):
                reponse_label.text = random.choice(reponses_acceptation)
            elif texte.strip() == "":
                reponse_label.text = "🕊️ Prends un moment pour écrire, même un mot peut être libérateur."
            else:
                reponse_label.text = random.choice(reponses_possibles)

        ui.button(
            "✨ Puis-je le changer ?",
            on_click=analyser
        ).classes('bg-green-600 text-white rounded-2xl px-8 py-3 hover:bg-green-700 shadow-lg')

# Démarrage
if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8080))
    ui.run(
        title='Simono - Acceptation et Adaptation',
        host=host,
        port=port,
        reload=False
    )
# Fin du code
# Fin du fichier simono.py