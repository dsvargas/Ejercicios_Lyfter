class Head:
    def __init__(self, hair_color, eye_color):
        self.hair_color = hair_color
        self.eye_color = eye_color  
class Torso:
    def __init__(self, chest_size, waist_size):
        self.chest_size = chest_size
        self.waist_size = waist_size
class Arm:
    def __init__(self, length, strength):
        self.length = length
        self.strength = strength
class Hand:
    def __init__(self, size, dexterity):
        self.size = size
        self.dexterity = dexterity
class Leg:
    def __init__(self, length, strength):
        self.length = length
        self.strength = strength
class Feet:
    def __init__(self, size, comfort):
        self.size = size
        self.comfort = comfort

class Human:
    def __init__(self, head, torso, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.torso = torso
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg

    def describe_human(self):
        print(f"Head: Hair Color - {self.head.hair_color}, Eye Color - {self.head.eye_color}")
        print(f"Torso: Chest Size - {self.torso.chest_size}, Waist Size - {self.torso.waist_size}")
        print(f"Left Arm: Length - {self.left_arm.length}, Strength - {self.left_arm.strength}")
        print(f"Right Arm: Length - {self.right_arm.length}, Strength - {self.right_arm.strength}")
        print(f"Left Leg: Length - {self.left_leg.length}, Strength - {self.left_leg.strength}")
        print(f"Right Leg: Length - {self.right_leg.length}, Strength - {self.right_leg.strength}")
human1 = Human(
    head=Head(hair_color="Brown", eye_color="Blue"),
    torso=Torso(chest_size=40, waist_size=32),
    left_arm=Arm(length=20, strength=80),
    right_arm=Arm(length=120, strength=80),
    left_leg=Leg(length=410, strength=90),
    right_leg=Leg(length=410, strength=90)
)
human2 = Human(
    head=Head(hair_color="Brown", eye_color="Blue"),
    torso=Torso(chest_size=40, waist_size=32),
    left_arm=Arm(length=20, strength=80),
    right_arm=Arm(length=120, strength=80),
    left_leg=Leg(length=410, strength=90),
    right_leg=Leg(length=410, strength=90)
)
human3 = Human(
    head=Head(hair_color="Brown", eye_color="Blue"),
    torso=Torso(chest_size=40, waist_size=32),
    left_arm=Arm(length=20, strength=80),
    right_arm=Arm(length=120, strength=80),
    left_leg=Leg(length=410, strength=90),
    right_leg=Leg(length=410, strength=90)
)
human4 = Human(
    head=Head(hair_color="Brown", eye_color="Blue"),
    torso=Torso(chest_size=40, waist_size=32),
    left_arm=Arm(length=20, strength=80),
    right_arm=Arm(length=120, strength=80),
    left_leg=Leg(length=410, strength=90),
    right_leg=Leg(length=410, strength=90)
)
human5 = Human(
    head=Head(hair_color="Brown", eye_color="Blue"),
    torso=Torso(chest_size=40, waist_size=32),
    left_arm=Arm(length=20, strength=80),
    right_arm=Arm(length=120, strength=80),
    left_leg=Leg(length=410, strength=90),
    right_leg=Leg(length=410, strength=90)
)
human6 = Human(
    head=Head(hair_color="Brown", eye_color="Blue"),
    torso=Torso(chest_size=40, waist_size=32),
    left_arm=Arm(length=20, strength=80),
    right_arm=Arm(length=120, strength=80),
    left_leg=Leg(length=410, strength=90),
    right_leg=Leg(length=410, strength=90)
)
human7 = Human(
    head=Head(hair_color="Brown", eye_color="Blue"),
    torso=Torso(chest_size=40, waist_size=32),
    left_arm=Arm(length=20, strength=80),
    right_arm=Arm(length=120, strength=80),
    left_leg=Leg(length=410, strength=90),
    right_leg=Leg(length=410, strength=90)
)

human1.describe_human() 