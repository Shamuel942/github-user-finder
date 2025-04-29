import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        print(f"\n👤 Usuario: {user_data['login']}")
        print(f"📝 Nombre: {user_data.get('name', 'No disponible')}")
        print(f"📍 Ubicación: {user_data.get('location', 'No disponible')}")
        print(f"🔗 Perfil: {user_data['html_url']}")
        print(f"📦 Repositorios públicos: {user_data['public_repos']}")
        print(f"👥 Seguidores: {user_data['followers']}")
        print(f"🏢 Empresa: {user_data.get('company', 'No disponible')}")
    else:
        print("\n❌ Usuario no encontrado.")

if __name__ == "__main__":
    print("🔎 Buscador de Usuarios de GitHub 🔎")
    username = input("Introduce el nombre de usuario de GitHub: ")
    get_github_user(username)
