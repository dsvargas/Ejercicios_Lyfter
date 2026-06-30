'''Investigue qué usos se le pueden dar a la herencia multiple 
y cree un ejemplo.'''
"Basicamente la herencia multiple se da cuando un objeto hereda de dos clases diferentes o mas "
"ejemplo un hijo con caracteristicas de ambos padres, los ojos verdes de la mama y la piel morena del padre"
""

class ElectronicDevice:
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"🔌 The {self.brand} device has been turned on.")

    def turn_off(self):
        self.is_on = False
        print(f"🔌 The {self.brand} device has been turned off.")


class WiFiConnector:
    def __init__(self):
        self.ip = "0.0.0.0"
        self.is_connected = False

    def connect_to_network(self, network_name):
        self.is_connected = True
        self.ip = "192.168.1.45"
        print(f"🌐 Successfully connected to network: '{network_name}' with IP: {self.ip}")

    def disconnect_from_network(self):
        self.is_connected = False
        print("🌐 Disconnected from the wireless network.")


# CLASE CON HERENCIA MÚLTIPLE
# Hereda la administración de energía Y la administración de red inalámbrica
class SmartTV(ElectronicDevice, WiFiConnector):
    def __init__(self, brand, inches):
        # Inicializamos ambas clases padres para estructurar el objeto correctamente
        ElectronicDevice.__init__(self, brand)
        WiFiConnector.__init__(self)
        self.inches = inches

    def stream_video(self, platform):
        if self.is_on and self.is_connected:
            print(f"Streaming content from {platform} on the {self.inches}-inch screen.")
        elif not self.is_on:
            print("Cannot stream: The TV is turned off.")
        else:
            print("Cannot stream: The TV has no internet connection.")

my_tv = SmartTV(brand="Samsung", inches=55)
my_tv.turn_on()
my_tv.connect_to_network("Home_Internet_5G")
my_tv.stream_video("Netflix")
my_tv.disconnect_from_network()
my_tv.turn_off()