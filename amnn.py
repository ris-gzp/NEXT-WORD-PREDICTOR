from sklearn.metrics.pairwise import linear_kernel

def recommend(movie):
    if movie not in new_df['title'].values:
        print("❌ Movie not found in dataset.")
        return
    
    index = new_df[new_df['title'] == movie].index[0]
    cosine_sim = linear_kernel(vectors[index:index+1], vectors).flatten()
    movies_list = sorted(list(enumerate(cosine_sim)), key=lambda x: x[1], reverse=True)[1:6]

    print(f"\n🎬 Recommended movies for '{movie}':\n")
    for i in movies_list:
        print(f"👉 {new_df.iloc[i[0]].title}")