
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

def load_fullcombined_data():
    # Creating the pandas dataframe from the combined file    
    df_netflix = pd.read_csv(r'model/fullcombined_data.csv', sep = ',', names = ['movie', 'user', 'rating', 'date'])
    df_netflix.date = pd.to_datetime(df_netflix.date)
    return df_netflix

def create_sparse_matrix():
    train_sparse_matrix = sparse.load_npz(r'model/train_sparse_matrix.npz')
    #train_sparse_matrix = train_sparse_matrix[:,movie_id]
    return train_sparse_matrix

def create_movie_sparse_old(movie_id):
    movie_sparse_matrix = sparse.load_npz(r"model/movie_sparse_matrix.npz")
    movie_sparse_matrix = movie_sparse_matrix[movie_id]
    return movie_sparse_matrix

def create_movie_sparse(movie_id):
    train_sparse_matrix = create_sparse_matrix()
    movie_sparse_matrix = cosine_similarity(X = train_sparse_matrix.T, dense_output = False)[movie_id]
    return movie_sparse_matrix

def moviesimilarity(movie_id):
    movie_sparse_matrix = create_movie_sparse(movie_id)
    similarities = movie_sparse_matrix.toarray().ravel()
    similar_indices = similarities.argsort()[::-1][1:]
    similarities = similarities[similar_indices]
    sim_indices = similarities.argsort()[::-1][1:]
    return sim_indices


def df_movie_titles_index():

    # Let's load movie titles from the csv file provided by Netflix
    movie_titles = pd.read_csv(r"model/movie_titles.csv", 
                                sep = ',', 
                                header = None,
                                names = ['Movie_Id', 'Release_Year', 'Title'], 
                                verbose = True,
                                index_col = 'Movie_Id',
                                encoding = "ISO-8859-1")
    
    #movie_titles = movie_titles.reset_index(inplace=True)
    return movie_titles

def df_movie_titles():

    # Let's load movie titles from the csv file provided by Netflix
    movie_titles = pd.read_csv(r"model/movie_titles.csv", 
                                sep = ',', 
                                header = None,
                                names = ['Movie_Id', 'Release_Year', 'Title'], 
                                verbose = True,
                                #index_col = 'Movie_Id',
                                encoding = "ISO-8859-1")
    
    #movie_titles = movie_titles.reset_index(inplace=True)
    return movie_titles

def create_recommendations_df(df):
    global recommendations_df
    recommendations_df = df