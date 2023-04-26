from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.files.storage import default_storage
import csv
from io import TextIOWrapper
from django.contrib.auth.models import User
from .models import Customer
from django.db import transaction
from django.core.exceptions import ValidationError
from django.db import IntegrityError


class ReceptionData(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        # Comprueba si se ha enviado un archivo
        if 'file' not in request.FILES:
            return Response({'message': 'No file received'}, status=400)

        # Obtiene el archivo CSV
        csv_file = request.FILES['file']

        # Procesa el archivo CSV
        try:
            # Usa TextIOWrapper para leer el archivo como texto
            wrapper = TextIOWrapper(csv_file.file, encoding='utf-8')
            reader = csv.reader(wrapper)

            # Procesa cada fila del archivo CSV
            repeat=0
            new_users = 0
            row_count = 0
            for row in reader:
                 # Omitir la primera fila, ya que contiene los encabezados
                row_count += 1
                if row_count == 1:
                    continue
                try:
                    # Divide el nombre completo en first_name y last_name
                    full_name, correo, telefono = row
                    name_parts = full_name.split()
                    first_name = name_parts[0]
                    last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''
                    # Crea un usuario y un cliente con los datos de la fila del archivo CSV
                    with transaction.atomic():
                        user = User(username=full_name, first_name=first_name, last_name=last_name)
                        user.save()
                        customer = Customer(user=user, telefono=telefono, correo=correo)
                        customer.save()
                        new_users += 1
                except IntegrityError as e:
                    print("EROROR"*10)
                    # if 'username' in e.message_dict:
                    try:
                        existing_user = User.objects.get(username=full_name)
                        existing_customer = Customer.objects.get(user=existing_user)
                        existing_customer.repeat = True
                        existing_customer.save()
                    except (User.DoesNotExist, Customer.DoesNotExist):
                        pass
                    repeat += 1
                except Exception as e :
                    print(e)
                    repeat += 1

        
        except Exception as e:
            return Response({'message': 'Error processing the CSV file', 'error': str(e)}, status=500)

        return Response({'repeated': repeat, 'new_users': new_users})
