import pywhatkit
import time
from datetime import datetime
import csv
import os

def load_contacts_from_csv(filename):
    contacts = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append({
                    "name": row['First Name'],
                    "number": row['Phone']
                })
        print(f"Successfully loaded {len(contacts)} contacts from CSV")
        return contacts
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return []

# New Year greeting message
message = "Wishing you and your loved ones a joyful New Year in advance! May 2025 bring happiness, good health, and success. Cheers to new beginnings and cherished memories! 🌟🎉 \nThanks Arun!"

def send_whatsapp_message(phone_number, msg):
    try:
        # Get current time
        now = datetime.now()
        
        # Send message
        # Note: Phone number should include country code
        pywhatkit.sendwhatmsg(phone_number, msg, now.hour, now.minute + 1)
        
        # Wait for 20 seconds before sending next message
        time.sleep(10)
        print(f"Message sent successfully to {phone_number}")
        
    except Exception as e:
        print(f"Error sending message to {phone_number}: {str(e)}")

def main():
    # CSV file name
    csv_file = "contacts.csv"
    
    # Load contacts from CSV
    contacts = load_contacts_from_csv(csv_file)
    
    if not contacts:
        print("No contacts loaded. Please check your CSV file.")
        return
    
    print("Starting to send New Year greetings...")
    
    for contact in contacts:
        print(f"Sending message to {contact['name']}...")
        send_whatsapp_message(contact['number'], "Hi " + contact['name'] + ",\n" + message)
        
    print("All messages have been sent!")

if __name__ == "__main__":
    main() 