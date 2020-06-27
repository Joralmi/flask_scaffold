docker build . --tag flask_scaffold
docker run -p 5000:5000 --name flask_scaffold flask_scaffold