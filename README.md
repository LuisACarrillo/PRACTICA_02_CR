# PRACTICA_02_CR

# Correr jenkins en docker
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk17

# Obtener clave
docker logs jenkins

# Entrar a Jenkins
http://localhost:8080

- Pegar la clave
- Escoger Install Suggested plugins 
- Agregar usuario admin (opcional, si no agregas uno se inicia con admin)
- 