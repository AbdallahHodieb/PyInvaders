class Invader_Properties(object):
    def __init__(self,anim_images,exp_images,exp_sound,vectorX=0,vectorY=0,movment_type=0,ANIM_DELAY =2,health =10):
        
        self.anim_images  = anim_images
        self.exp_images   = exp_images        
        
        self.exp_sound    = exp_sound
        
        self.vectorX      = vectorX
        self.vectorY      = vectorY
        self.movment_type = movment_type
        
        self.ANIM_DELAY   = ANIM_DELAY
        self.health       = health
        
class Wepon__Properties(object):
    def __init__(self,anim_images,exp_images,exp_sound,vectorX=0,vectorY=0,movment_type=0,ANIM_DELAY =2,damage =10):

        self.anim_images  = anim_images
        self.exp_images   = exp_images
        
        self.exp_sound    = exp_sound
                
        self.vectorX      = vectorX
        self.vectorY      = vectorY
        self.movment_type = movment_type
        
        self.ANIM_DELAY   = ANIM_DELAY
        self.damage       = damage