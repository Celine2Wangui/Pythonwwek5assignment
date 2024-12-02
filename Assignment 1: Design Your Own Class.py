class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color 1 

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending '{message}' to {number}...")

    def open_app(self, app_name):
        print(f"Opening {app_name}...")

# Create a smartphone object
my_phone = Smartphone("Apple", "iPhone 15", "256GB", "Midnight")

# Use the methods
my_phone.make_call("+1234567890")
my_phone.send_message("+1234567890", "Hello, world!")
my_phone.open_app("Instagram")
