# app.py

from flask import Flask, render_template, request, flash, send_file
import os
from model import moviesimilarity, df_movie_titles, df_movie_titles_index, create_sparse_matrix, create_movie_sparse

# Inicializando a app flask
app = Flask(__name__)

secret_key = str(os.urandom(16))
print("secret_key" + secret_key)
app.config['SECRET_KEY'] = secret_key

# Renderização HTML
@app.route('/')
def index():
	# Renderização da página html
	return render_template("index.html")

@app.route('/donwloadrecommendation', methods=('GET', 'POST'))
def donwloadrecommendation():
	if request.method =='GET':
		print('teste')
		#recommendations_df = create_recommendations_df()
		#recommendations_df.to_csv(r'recommendations.csv', index=False)
		recommendations_file = (r'recommendations.csv')
		return send_file(recommendations_file, as_attachment=True)

# Renderização HTML
@app.route('/movies', methods=('GET', 'POST'))
def movies():
	#session.clear()
	#session.modified = True

	headings = ('Movie Id', 'Release Year', 'Movie Title')
	
	movie_titles = df_movie_titles()	
	movie_titles = movie_titles.loc[movie_titles['Movie_Id'] < 500]
	
	# Convert datafrae to a numpy array
	movies = movie_titles.to_numpy()

	ratio_disable = False

	if request.method =='POST':
		if request.form.getlist('oneRadio'):
			for id in request.form.getlist('oneRadio'):
				movie_id = int(id)
				
			movie_titles = df_movie_titles_index()
			#movie_titles = movie_titles.set_index('Movie_Id', inplace=True)
			sim_indices = moviesimilarity(movie_id)				
			#print(movie_titles.loc[sim_indices[:10]])
			recommendations = movie_titles.loc[sim_indices[:10]]
			headings = ('Release Year', 'Movie Title')
			movies = recommendations.to_numpy()
			# Flag to unable ratio buttons or other HTML tags
			ratio_disable = True

			# Messages to end user
			train_sparse_matrix = create_sparse_matrix()			
			movie_sparse_matrix = create_movie_sparse(movie_id)
			Movie_Name = "Chosen movie: " + movie_titles.loc[movie_id].values[1]
			Total_User_Ratings = "Total user ratings = " + str(train_sparse_matrix[:,movie_id].getnnz())
			Total_Movies_Similar = "We find " + str(movie_sparse_matrix.getnnz()) + " movies that are similar to this one and listed the most similar ones below."
				
			return render_template('movies.html', movies=movies, headings=headings, ratio_disable=ratio_disable, Movie_Name=Movie_Name, Total_User_Ratings=Total_User_Ratings, Total_Movies_Similar=Total_Movies_Similar)
		
		if not request.form.getlist('oneRadio'):
			flash('You have to check at least one movie to get recommendations!')
			return render_template('movies.html', movies=movies, headings=headings, ratio_disable=ratio_disable)
	
	# Renderização da página html
	return render_template("movies.html", movies=movies, headings=headings, ratio_disable=ratio_disable)

# Função Main
if __name__ == "__main__":
	
	# Decide em que porta executa a app
	port = int(os.environ.get('PORT', 5000))
	
	# Executa a app localmente
	app.run(host='0.0.0.0', port=port)	