# Cluster Basket Points

Cluster Basket Points is a web application that clusters randomly generated geographical points within a bounding box using the Agglomerative Clustering algorithm from scikit-learn. The application is built using Python and FastAPI.
Deployment

The backend is deployed on Render, and the API documentation can be found at https://cluster-basket-points.onrender.com/docs#. The frontend, a simple Leaflet app, is deployed on Vercel and can be accessed at https://cluster-basket-points-fe.vercel.app/.

The resulting GeoJSON file is visualized on the map, with each point's color indicating its cluster.

Both the backend and frontend code are available on GitHub at https://github.com/cemrehancavdar/cluster_basket_points and https://github.com/cemrehancavdar/cluster_basket_points_fe, respectively.
