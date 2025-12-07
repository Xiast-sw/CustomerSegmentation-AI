from sklearn.cluster import KMeans

def find_optimal_k(data, k_range=range(1, 11)):
    """Elbow method ile optimal K değerini bulur."""
    distortions = []
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        distortions.append(kmeans.inertia_)
    
    return list(k_range), distortions

def build_kmeans_model(n_clusters=5):
    """KMeans modeli oluşturur."""
    return KMeans(n_clusters=n_clusters, random_state=42)

def train_model(model, data):
    """Modeli eğitir ve tahminleri döndürür."""
    predictions = model.fit_predict(data)
    return predictions, model.cluster_centers_
