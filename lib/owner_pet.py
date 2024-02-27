class Pet:

    PET_TYPES = [
        "dog",
        "cat",
        "rodent",
        "bird",
        "reptile",
        "exotic"
    ]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if not pet_type in Pet.PET_TYPES:
            raise Exception("Not in this list.")
        else:
            self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

class Owner:

    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("The 'pet' argument must be an instance of Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)