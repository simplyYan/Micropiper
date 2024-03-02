import os
import requests
import tempfile

def Using(repo_path, func_call):

    user, repo = repo_path.split('/')

    raw_url = f'https://raw.githubusercontent.com/{user}/{repo}/main/main.py'

    response = requests.get(raw_url)

    if response.status_code == 200:

        temp_dir = os.path.join(tempfile.gettempdir(), repo)
        os.makedirs(temp_dir, exist_ok=True)

        temp_file = os.path.join(temp_dir, 'main.py')
        with open(temp_file, 'wb') as f:
            f.write(response.content)

        sys.path.append(temp_dir)

        import main  
        exec(func_call)  
    else:
        print(f'Erro ao baixar o arquivo do repositório {repo_path}')