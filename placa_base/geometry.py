from pandas import read_csv
from math import ceil

def profile_list():
    profiles_df = read_csv('./placa_base/profiles.csv')
    profile_list_euro = profiles_df['Name'][profiles_df['Type'] == 'Euro'].to_list()
    pprofile_list_american = profiles_df['Name'][profiles_df['Type'] == 'American'].to_list()

    return profile_list_euro, pprofile_list_american

def bolt_list():
    bolt_df = read_csv('./placa_base/bolts.csv')
    bolt_list=bolt_df['bolt_name'].to_list()
    return bolt_list

class Profile():
    def __init__(self, name):
        self.name = name
        
        profiles_df = read_csv('./placa_base/profiles.csv')

        self.h  = profiles_df[profiles_df['Name'] == self.name]['h_(mm)' ].iloc[0]
        self.b  = profiles_df[profiles_df['Name'] == self.name]['b_(mm)' ].iloc[0]
        self.tw = profiles_df[profiles_df['Name'] == self.name]['tw_(mm)'].iloc[0]
        self.tf = profiles_df[profiles_df['Name'] == self.name]['tf_(mm)'].iloc[0]
    
    def profile_shape(self):
        # GEOMETRIA PARA EL DIBUJO EN CANVAS
        x1 = self.b/2
        x2 = self.tw/2
        y1 = self.h/2
        y2 = self.h/2 -self.tf

        # puntos para dibujar silueda del perfil centrados en 0,0
        profile_shape =   [ (-x1,-y1),
                            ( x1,-y1),
                            ( x1,-y2),
                            ( x2,-y2),
                            ( x2, y2),
                            ( x1, y2),
                            ( x1, y1),
                            (-x1, y1),
                            (-x1, y2),
                            (-x2, y2),
                            (-x2,-y2),
                            (-x1,-y2),
                            (-x1,-y1)   ]
        
        return profile_shape
    
    def square_shape(self):
        # minimo cuadrado redondeado a 5 mm, que contiene el perfil 
        xs = ceil(max(self.h,self.b)/5)*5/2 # square shape distance
        min_square = [  (-xs,-xs),
                        ( xs,-xs),
                        ( xs, xs),
                        (-xs, xs),
                        (-xs,-xs)   ]
        
        return min_square
    
    def rectangle_shape(self):
        # minimo rectangulo redondeado a 5 mm, que contiene el perfil 
        half_higth = ceil(self.h/5)*5/2 # square shape distance
        half_width = ceil(self.b/5)*5/2
        min_square = [  (-half_width,-half_higth),
                        ( half_width,-half_higth),
                        ( half_width, half_higth),
                        (-half_width, half_higth),
                        (-half_width,-half_higth)   ]
        
        return min_square

class Bolt():
    
    def __init__ (self, name):
        self.name = name

        bolts_df = read_csv('./placa_base/bolts.csv').set_index('bolt_name')

        self.bolt_diameter   = bolts_df['Diameter, mm.']              .loc[name]
        self.hole_diameter   = bolts_df['Hole Diameter, mm.']         .loc[name]
        self.wash_dimention  = bolts_df['Min. Washer Dimension, mm.'] .loc[name]
        self.wrench_dis      = bolts_df['Socket. mm.']                .loc[name]

    def bolts_shape (self, profile,fit = False, number = 4,x =0, y = 0):
        
        half_higth = ceil(profile.h/5)*5/2
        half_width = ceil(profile.b/5)*5/2
        
        if not(fit):
            half_higth = max(half_higth, half_width)
            half_width = max(half_higth, half_width)
        
        x_dist = ceil((self.wrench_dis + half_width)/2.5)*2.5 + float(x)/2
        y_dist = ceil((self.wrench_dis + half_higth)/2.5)*2.5 + float(y)/2
        
        bolt_cordinates_4= [(-x_dist,-y_dist),
                            (-x_dist, y_dist),
                            ( x_dist,-y_dist),
                            ( x_dist, y_dist)   ]
        
        bolt_cordinates_6= [(-x_dist,-y_dist),
                            (-x_dist, y_dist),
                            ( x_dist,-y_dist),
                            ( x_dist, y_dist),
                            ( 0     , y_dist),
                            ( 0     ,-y_dist)   ]
        
        bolt_cordinates_8= [(-x_dist,-y_dist),
                            (-x_dist, y_dist),
                            ( x_dist,-y_dist),
                            ( x_dist, y_dist),
                            ( 0     ,-y_dist),
                            ( 0     , y_dist),
                            ( x_dist, 0     ),
                            (-x_dist, 0     ),   ]


        if   number == 4:
            return bolt_cordinates_4
        elif number == 6:
            return bolt_cordinates_6
        elif number== 8:
            return bolt_cordinates_8
        else:
            return bolt_cordinates_4
    
class BPlate():
    def __init__ (self):
        pass

    def bp_shape(self,profile, bolt,fit = False, x =0, y = 0):

        half_width = ceil(profile.b/5)*5/2
        half_higth = ceil(profile.h/5)*5/2

        if not(fit):
            half_higth = max(half_higth, half_width)
            half_width = max(half_higth, half_width)
        
        x_dist = ceil((bolt.wrench_dis + half_width)/2.5)*2.5
        y_dist = ceil((bolt.wrench_dis + half_higth)/2.5)*2.5

        x_bp_dis = ceil((x_dist + 1.5 * bolt.bolt_diameter)/2.5)*2.5 + float(x)/2
        y_bp_dis = ceil((y_dist + 1.5 * bolt.bolt_diameter)/2.5)*2.5 + float(y)/2

        bp_sq  = [  (-x_bp_dis,-y_bp_dis),
                    ( x_bp_dis,-y_bp_dis),
                    ( x_bp_dis, y_bp_dis),
                    (-x_bp_dis, y_bp_dis),
                    (-x_bp_dis,-y_bp_dis)]
        
        return bp_sq
    

