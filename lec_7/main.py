try:
    fileName = input("Enter the name of the file you want to open: ")
    
    file = open(fileName, 'r');    
    print("File Content:");
    print(file.read());
        
    userInput = input("Do you want to write to this file? (yes/no): ");
    if userInput == 'yes':
        file = open(fileName, 'a');        
        text = input("Enter the text you want to add to the file: ");
        file.write(text);
        print("Text successfully added to the file.");
    else:        
        newFileName = input("Enter new file name: ");
        file = open(newFileName, 'w');
        text = input("Enter the text you want to write to the new file: ");
        file.write(text);
        print("Text successfully written to the file ", newFileName, ".");

except FileNotFoundError:
    print("File ", fileName , " not found.");
except ValueError:
    print("Please enter a valid filename.");
except Exception as e:
    print(e);
finally:
    print("File closed.");
