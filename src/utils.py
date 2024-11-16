def save_to_file(filename, data):
    """Sauvegarde des données dans un fichier."""
    with open(filename, 'wb') as f:
        f.write(data)

def load_from_file(filename):
    """Charge des données depuis un fichier."""
    with open(filename, 'rb') as f:
        return f.read()
