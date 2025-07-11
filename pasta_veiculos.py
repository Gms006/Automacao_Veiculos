import os

# Caminho base onde tudo será criado
base_path = r"U:\Automações PYTHON\Veiculos"

folders = [
    "app/pages",
    "app/components",
    "src/estoque",
    "src/tributos",
    "src/utils",
    "src/models",
    "tests",
    "data",
    "docs",
    ".vscode"
]

files = [
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    ".env.example",
    "app/__init__.py",
    "app/main.py",
    "src/__init__.py",
    "tests/__init__.py",
    "tests/test_sample.py",
    "data/README.md",
    "docs/arquitetura.md",
    ".vscode/settings.json"
]

# Criação das pastas
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Criação dos arquivos (vazios)
for file in files:
    file_path = os.path.join(base_path, file)
    # Garante que as pastas intermediárias existem
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "a", encoding="utf-8"):
        pass

print(f"Estrutura criada em {base_path} com sucesso!")
