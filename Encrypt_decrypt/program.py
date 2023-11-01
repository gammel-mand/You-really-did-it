def encrypt_coordinates(latitude, longitude, key):
    encrypted_latitude = ''.join([chr(ord(char) + key) for char in str(latitude)])
    encrypted_longitude = ''.join([chr(ord(char) + key) for char in str(longitude)])
    return encrypted_latitude, encrypted_longitude

def decrypt_coordinates(encrypted_latitude, encrypted_longitude, key):
    decrypted_latitude = ''.join([chr(ord(char) - key) for char in encrypted_latitude])
    decrypted_longitude = ''.join([chr(ord(char) - key) for char in encrypted_longitude])
    return decrypted_latitude, decrypted_longitude

# Example coordinates
latitude = 37.7749
longitude = -122.4194
encryption_key = 5

# Encrypt the coordinates
encrypted_lat, encrypted_lon = encrypt_coordinates(latitude, longitude, encryption_key)

print("Original Coordinates:")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

print("\nEncrypted Coordinates:")
print(f"Latitude: {encrypted_lat}")
print(f"Longitude: {encrypted_lon}")

# Decrypt the coordinates
decrypted_lat, decrypted_lon = decrypt_coordinates(encrypted_lat, encrypted_lon, encryption_key)

print("\nDecrypted Coordinates:")
print(f"Latitude: {decrypted_lat}")
print(f"Longitude: {decrypted_lon}")
