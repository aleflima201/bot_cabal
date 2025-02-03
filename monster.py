class Monster:
    def __init__(self, name, location, image, status=True):
        self.name = name
        self.location = location
        self.image = image

    @property
    def name(self):
        return self.name
    
    @property
    def location(self):
        self.location

    @location.setter
    def location(self, location):
        if self.location == None:
            self.location = location

    @property
    def image(self):
        self.image

    @property
    def status(self):
        self.status

    @status.setter #quando criado o monstro vem com status True=vivo quando morto o status passa a ser False=morto
    def status(self):
        if self.status == True:
            self.status = False