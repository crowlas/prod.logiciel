""" 
création d'objets à partir de la BD du TD2 
la table esuipements possède 182 éléemnts


On utilisera bottle pour passer le python en web ( la géolocalisation est desssus)
"""

import sys
sys.path.append("/hometu/etudiants/b/i/E155722N/2016/s4/prod.logiciel/td2")


import td2

from td2 import BD


class Villes :
    """
    Classe qui donne toutes les villes
    Tire ses données du CSV des activités
    - self.villes : un tableau de villes
    """
    
    def __init__(self):
        bd = BD()
        result = list(bd.selectTableElement("activ","DISTINCT ComLib"))
        self.villes=[]
        for elmt in result :
            print ("Nouvelle ville  : "+elmt[0])
            self.villes.append(elmt)
            
    
    def getVilles(self):
        return self.villes
        

class Activ :
    """
    Classe qui donne toutes les activités
    Tire ses données du CSV des activités
    - self.activites : un tableau de villes
    """
    
    def __init__(self):
        bd = BD()
        result = list(bd.selectTableElement("activ","DISTINCT ActLib"))
        self.activites=[]
        for elmt in result :
            print ("Nouvelle activitée  : "+elmt[0])
            self.activites.append(elmt)
            
    
    def getVilles(self):
        return self.villes
            



class ActivVille:
    """
    Classe qui donne pour une ville toutes les activités disponibles
    Tire ses données du CSV des activités
    - self.ville : un String
    - self.activités : un tableau d'activités
    
    """
   
    def __init__(self, ville):
        bd = BD()
        querySQL="activ where ComLib="+'"'+ville+'"'
        result = list(bd.selectTableElement(querySQL,"DISTINCT ActLib"))
        self.ville=ville
        self.activites=[]
        for elmt in result :
            print ("Nouvelle activité pour la ville "+ville+" : "+elmt[0])
            self.activites.append(elmt[0])
        
        
    def getActivites(self) :
        return self.activites
        

class VillesActiv:
    """
    Classe qui donne pour une activité toutes les villes possibles
    Tire ses données du CSV des activités
    - self.activite : un String
    - self.villes : un tableau de villes
    """
    def __init__(self, activite):
        bd = BD()
        querySQL="activ where ActLib="+'"'+activite+'"'
        result = list(bd.selectTableElement(querySQL,"DISTINCT ComLib"))
        self.activite=activite
        self.villes=[]
        for elmt in result :
            print ("Nouvelle ville pour l'activité "+activite+" : "+elmt[0])
            self.villes.append(elmt[0])
           
    def getVilles(self) :
        return self.villes


class InstallActiv : # JE SUIS ICI !!!
    """
    Classe répertoriant la localisation d'une activité
    Tire ses données du CSV activités ( idEquipement) , du CSV equipement ( EquipementId, InsNumeroInstall) et du CSV installations ( numéro de l'installation)
    - self.activité
    - self.ville
    - self.installations
    """
    
    def __init__(self, ville, activite ):
        bd = BD()
        querySQL="activ where ActLib="+'"'+activite+'"'+"and ComLib="+'"'+ville+'"'
        idEquipement = list(bd.selectTableElement(querySQL,"EquipementId"))
        print ("idEquipement = "+str(idEquipement))
        result=[]
        self.installations=[]
        for elmt in idEquipement :
            #print ("elmt  = "+elmt[0]) # DEBUG
            querySQL="equip where EquipementId="+'"'+elmt[0]+'"'
            numInstall = list(bd.selectTableElement(querySQL,"InsNumeroInstall"))[0][0]
            #print (numInstall) # DEBUG
            if ( numInstall not in result ) :
                result.append(numInstall)
                print ("le result : "+str(result))
        self.activite=activite
        self.ville=ville
        self.installations.append(numInstall)
        
    
    def getInstallations(self):
        return self.installations

    
class Install :
    """
    Classe répertoriant les installations
    Tire ses données du CSV installations 
    - self.nomInstal
    - self.longitude
    - self.latitude
    """
    
    def __init__(self, numInstall ):
        bd = BD()
        querySQL="instal where Numéro_de_l_installation="+'"'+numInstall+'"'
        result = list(bd.selectTableElement(querySQL,"Nom_usuel_de_l_installation, Longitude, Latitude"))
        print ("Nom_usuel_de_l_installation = "+result[0][0])
        print ("Longitude = "+result[0][1])
        print ("Latitude = "+result[0][2])
        
        self.nomInstal=result[0][0]
        self.longitude=result[0][1]
        self.latitude=result[0][2]
        
    def getLongitude(self):
        return self.longitude
    
    def getLatitude(self):
        return self.latitude
        
    def getNomInstal(self):
        return self.latitude
        
    
    
        
        
        
