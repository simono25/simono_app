from nicegui import ui
import random

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
    ui.query('body').style('background: linear-gradient(to bottom, #fdfbfb, #ebedee); color: #333; font-family: "Helvetica Neue", sans-serif;')

    with ui.column().classes('items-center justify-center min-h-screen'):
        ui.label('🌿 Réflexion du jour').classes('text-4xl font-bold mb-4 text-green-700')
        
        citation = random.choice(citations)
        ui.label(f'"{citation}"').classes('italic text-lg text-gray-600 mb-6 max-w-xl text-center')

        question = ui.textarea(label='✍️ Que veux-tu changer aujourd’hui ?', placeholder="Écris ici ta pensée...").classes('w-full max-w-xl mb-4')

        reponse_label = ui.label().classes('text-xl text-center max-w-xl mt-4 text-blue-700')

        def analyser():
            texte = question.value or ""
            # Analyse simplifiée du type de pensée
            if any(mot in texte.lower() for mot in ['le passé', 'les autres', 'la météo', 'mes parents', 'le système']):
                reponse_label.text = "❌ Tu ne peux pas le changer. Accepte et adapte-toi avec sérénité. 🌌"
            elif texte.strip() == "":
                reponse_label.text = "🕊️ Prends un moment pour écrire, même un mot peut être libérateur."
            else:
                reponse_label.text = "✅ Tu peux probablement agir. Agis avec sagesse et courage. ⚡️"

        ui.button("✨ Puis-je le changer ?", on_click=analyser).classes('bg-green-500 text-white rounded-xl px-6 py-2 hover:bg-green-600 shadow')

# Lance l'application localement
ui.run(title='Simono - Acceptation et Adaptation', reload=False)
