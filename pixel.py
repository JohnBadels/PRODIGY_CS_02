from PIL import Image
import numpy as np

def encrypt_decrypt_image(input_path, output_path, key):
    # Open the image
    img = Image.open(input_path)
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Flatten the array
    flat_array = img_array.flatten()
    
    # Create a key array of the same length as the flattened image
    key_array = np.tile(key, len(flat_array) // len(key) + 1)[:len(flat_array)]
    
    # Perform XOR operation
    encrypted_array = flat_array ^ key_array
    
    # Reshape the array back to the original image shape
    encrypted_img_array = encrypted_array.reshape(img_array.shape)
    
    # Create a new image from the encrypted array
    encrypted_img = Image.fromarray(encrypted_img_array.astype('uint8'), img.mode)
    
    # Save the encrypted/decrypted image
    encrypted_img.save(output_path)
    
    print(f"Image processed and saved as {output_path}")

def main():
    while True:
        operation = input("Enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit: ").lower()
        
        if operation == 'q':
            print("Exiting the program.")
            break
        
        if operation not in ['e', 'd']:
            print("Invalid option. Please try again.")
            continue
        
        input_path = input("Enter the path to the input image: ")
        output_path = input("Enter the path for the output image: ")
        key = input("Enter an encryption/decryption key (a string of numbers): ")
        
        try:
            key = [int(k) for k in key.split()]
        except ValueError:
            print("Invalid key. Please enter a string of numbers separated by spaces.")
            continue
        
        try:
            encrypt_decrypt_image(input_path, output_path, key)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()