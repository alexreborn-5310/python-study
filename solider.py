from gun import gun
class solider:
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun
    def change_gun(self, new_gun):
        self.gun = new_gun
    def add_gun_bullets(self, bullets_num):
        if self.gun is None:
            print(f"{self.name} has no gun to fire")
            return
        self.gun.add_bullets(bullets_num)
      
    def fire(self):
        if self.gun is None:
            print(f"{self.name} has no gun to fire")
            return
        if (self.gun.shoot()):
            print(f"{self.name} fired successfully")
        else:
            print(f"{self.name} failed to fire")
if __name__ == "__main__":
     alex = solider("alex")
     alex.change_gun(gun("AK47", 8))
     alex.fire()
     alex.fire()
     alex.fire()
     alex.fire() 
     alex.add_gun_bullets(5)
     alex.fire()