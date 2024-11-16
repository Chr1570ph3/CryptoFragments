from src.share import create_shares, recover_secret
from src.encrypt import encrypt_share
from src.decrypt import decrypt_share

from src.utils import save_to_file, load_from_file

def main():
    seed_phrase = "your secret seed phrase".encode('utf-8')

    # Vérifiez et ajustez la longueur des bytes
    if len(seed_phrase) % 2 != 0:
        seed_phrase += b" "  # Ajoute un byte de remplissage

    total_shares = 5
    threshold = 3

    # Étape 1 : Génération des parts
    shares = create_shares(seed_phrase, total_shares, threshold)
    print("Shares generated.")

    # Étape 2 : Chiffrement des parts et stockage
    encrypted_shares = []
    for i, share in enumerate(shares):
        encrypted_share, key = encrypt_share(share.encode('utf-8'))
        encrypted_shares.append((encrypted_share, key))
        save_to_file(f"share_{i + 1}.enc", encrypted_share)
        save_to_file(f"key_{i + 1}.key", key)
    print("Shares encrypted and saved to files.")

    # Étape 3 : Simulation de récupération
    recovered_shares = []
    for i in range(threshold):
        encrypted_share = load_from_file(f"share_{i + 1}.enc")
        key = load_from_file(f"key_{i + 1}.key")
        decrypted_share = decrypt_share(encrypted_share, key).decode('utf-8')
        recovered_shares.append(decrypted_share)

    # Étape 4 : Reconstitution de la seed phrase
    recovered_seed = recover_secret(recovered_shares)
    print("Recovered Seed Phrase:", recovered_seed)

if __name__ == "__main__":
    main()
