class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return f"The engine of the {self.make} {self.model} is starting."

    def stop_engine(self):
        return f"The engine of the {self.make} {self.model} is stopping."
