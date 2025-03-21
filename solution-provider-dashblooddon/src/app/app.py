from dash import Dash, html

# initialisation de l'application Dash
app = Dash(__name__)
app.title = "Tableau de bord pour le don de sang: analyse"

# disposition de base
app.layout = html.Div([
	html.H1("Tableau de bord de l'analyse de don de sang", style={"textAlign": "center"}),
	html.P("Prototype de visualisation des campagnes de don de sang.")
])

# lancement de l'application
if __name__ == "__main__":
	app.run_server(debug=True)
