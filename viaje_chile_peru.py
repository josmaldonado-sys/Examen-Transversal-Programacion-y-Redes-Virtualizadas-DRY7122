from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="dry7122")

print("=" * 55)
print(" DISTANCIA ENTRE CIUDADES CHILE - PERÚ ")
print("=" * 55)

while True:

    origen = input("\nCiudad de origen (Chile) o S para salir: ")

    if origen.lower() == "s":
        print("\nPrograma finalizado.")
        break

    destino = input("Ciudad de destino (Perú): ")

    if destino.lower() == "s":
        print("\nPrograma finalizado.")
        break

    print("\nMedios de transporte")

    print("1.- Automóvil")
    print("2.- Bus")
    print("3.- Avión")

    opcion = input("Seleccione una opción: ")

    ciudad_origen = geolocator.geocode(origen + ", Chile")
    ciudad_destino = geolocator.geocode(destino + ", Peru")

    if ciudad_origen is None or ciudad_destino is None:
        print("\nNo fue posible encontrar alguna ciudad.")
        continue

    distancia_km = geodesic(
        (ciudad_origen.latitude, ciudad_origen.longitude),
        (ciudad_destino.latitude, ciudad_destino.longitude)
    ).kilometers

    distancia_millas = distancia_km * 0.621371

    if opcion == "1":
        velocidad = 80
        transporte = "Automóvil"

    elif opcion == "2":
        velocidad = 70
        transporte = "Bus"

    elif opcion == "3":
        velocidad = 800
        transporte = "Avión"

    else:
        print("Opción inválida.")
        continue

    horas = distancia_km / velocidad

    print("\n" + "=" * 55)
    print("RESULTADOS")
    print("=" * 55)

    print(f"Origen : {origen}, Chile")
    print(f"Destino: {destino}, Perú")

    print(f"\nDistancia:")
    print(f"{distancia_km:.2f} kilómetros")
    print(f"{distancia_millas:.2f} millas")

    print(f"\nMedio de transporte: {transporte}")
    print(f"Duración aproximada: {horas:.2f} horas")

    print("\nNarrativa del viaje:")
    print(f"El viaje desde {origen}, Chile hasta {destino}, Perú")
    print(f"tiene una distancia aproximada de {distancia_km:.2f} km")
    print(f"({distancia_millas:.2f} millas).")
    print(f"Utilizando {transporte}, el tiempo estimado")
    print(f"de viaje es de {horas:.2f} horas.")
