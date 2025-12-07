import matplotlib.pyplot as plt
from preprocessing import prepare_data
from model import find_optimal_k, build_kmeans_model, train_model

# 1) Veriyi yükle ve hazırla
print("Loading data...")
df = prepare_data("data/customer-segment.csv")

# 2) Elbow method ile optimal K bul
print("Finding optimal K...")
k_values, distortions = find_optimal_k(df[['income', 'score']])

# Elbow plot
plt.figure(figsize=(10, 6))
plt.plot(k_values, distortions, marker='o')
plt.xlabel('K')
plt.ylabel('Distortion (Inertia)')
plt.title('Elbow Method for Optimal K')
plt.savefig('results/elbow_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# 3) K=5 ile model oluştur ve eğit
print("Training model with K=5...")
model = build_kmeans_model(n_clusters=5)
predictions, centers = train_model(model, df[['income', 'score']])

# Cluster'ları dataframe'e ekle
df['cluster'] = predictions

# 4) Cluster görselleştirme
plt.figure(figsize=(10, 6))

colors = ['green', 'red', 'black', 'orange', 'purple']
for i in range(5):
    cluster_data = df[df.cluster == i]
    plt.scatter(cluster_data['income'], cluster_data['score'], 
                color=colors[i], label=f'Cluster {i}')

plt.scatter(centers[:, 0], centers[:, 1], 
            color='blue', marker='X', s=200, label='Centroids')

plt.xlabel('Income (Normalized)')
plt.ylabel('Spending Score (Normalized)')
plt.title('Customer Segments')
plt.legend()
plt.savefig('results/clusters_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# 5) Sonuçları yazdır
print("\n📊 Cluster Centers:")
print(centers)

print("\n📈 Cluster Distribution:")
print(df['cluster'].value_counts().sort_index())

print("\n✅ Training completed!")
