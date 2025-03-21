#################################  C S V  D A T A  F E T C H I N G  #################################
import csv, io
from user.models import User
from user.serializers import UserSerial

# Fetch Data from CSV to add Users
def csv_fetch(text_file):
    csv_reader = csv.reader(text_file)
    header = next(csv_reader)
    normalized_header = [col.lower() for col in header]
    imported = 0
    existing = 0
    error_data = []
    for row in csv_reader:
        email_status = row[normalized_header.index('email')].strip()
        age = row[normalized_header.index('age')].strip() if int(row[normalized_header.index('age')].strip()) > 0 and int(row[normalized_header.index('age')].strip()) < 120 else None
        if email_status and age:
            if not User.objects.filter(email=row[normalized_header.index('email')].strip()).exists():
                user = User.objects.create(
                    first_name=row[normalized_header.index('name')].strip(),
                    email=row[normalized_header.index('email')].strip(),
                    username=row[normalized_header.index('email')].strip(),
                    age=age,
                )
                user.save()
                print(f"User created with email: {user.email}")
                imported += 1
            else:
                existing += 1
        else:
            error_data.append({row[normalized_header.index('name')].strip(): "Email is required"}) if email_status else error_data.append({row[normalized_header.index('name')].strip(): "Age is between 0 and 120"})
    return imported, existing, error_data