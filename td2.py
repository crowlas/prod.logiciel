""" création d'une BD à partir de CSV """

import csv


def line1(file):
    """
    charge dans une liste la première ligne d'un fichier CSV (séparateur , )
    """
    # on charge le fichier CSV
    file=open("/hometu/etudiants/b/i/E155722N/2016/s4/prod.logiciel/td2/"+file+".csv","r")
    test=csv.reader(file)
    # on convertit la liste en String afin de faciliter les traitements
    result = ','.join(next(test))
     # on supprime les caractères problématiques
    result = result.replace("'","_")
    result = result.replace(" ","_")

    list=result.split(',')

    return list
    file.close();

def chargerRowCSV(file):
    """
    charge dans une liste de liste les lignes d'un fichier CSV
    """
    line = 0
    file=open("/hometu/etudiants/b/i/E155722N/2016/s4/prod.logiciel/td2/"+file+".csv","r")
    test=csv.reader(file, delimiter= ',')
    tab=[]
    for i in test:
        if (line != 0): # on ne prend pas en compte la ligne d'en tete
            tab.append(i)
            # print (i) # debug
        line+=1

    file.close();
    return tab;



import sqlite3  # on importe la base de données

class BD:
    """Classe définissant une BD caractérisée par :
    - sa connexion
    La bd s'implemente à partir de fichier CSV
    """

    def __init__(self):
        self.conn = sqlite3.connect('ma_base.db')


    def closeBD():
        db.close()


    def createTable(self, table, file):
        """
        create a sqllite table with the first line of the file given
        """

        result=line1(file) # we get the line of the file that contain the name of the columns
        # print("DEBUG : En tête de la table : "%result)

        cursor = self.conn.cursor()

        if (self.existTable(table)==True) : # la table exist-elle
            print ("La table existe déjà. Echec de l'opération de création de table.")
        else :
            for elmt in result :
                print("l'élément à ajouter : %s " %elmt)
                try:
                    cursor.execute("""CREATE TABLE IF NOT EXISTS %s (%s TEXT)""" %(table,elmt))
                    cursor.execute("""alter table %s add column %s TEXT"""%(table,elmt))
                except Exception as e:

                    self.conn.rollback()
                    print ("error %s : %s" %(elmt,e))


    def selectTable(self, table):
        """ display the table choosed """
        if (self.existTable(table)==False) : # la table exist-elle ?
            print ("La table n'existe pas. Echec de l'opération de sélection de table.")
        else :
            cursor = self.conn.cursor()

            sql = "select * from "+table
            cursor.execute(sql)

            return(cursor.fetchall())
            
            
    def selectTableElement(self, table, element):
        """ display the table choosed """
        if (self.existTable(table)==False) : # la table exist-elle ?
            print ("La table n'existe pas. Echec de l'opération de sélection de table.")
        else :
            cursor = self.conn.cursor()

            sql = "select "+element+" from "+table
            cursor.execute(sql)

            return(cursor.fetchall())

    def selectTableRow(self, table, row ):
        """ display the table choosed """
        if (self.existTable(table)==False) : # la table exist-elle ?
            print ("La table n'existe pas. Echec de l'opération de sélection de table.")
        else :
            cursor = self.conn.cursor()
            # La requête SQL
            sql = "select * from "+table
            rows=cursor.execute(sql)
            # Sélection du résultat
            try :
                result = cursor.fetchall()[row]
                return(result)
            except IndexError :
                print ("le tuple sélectionné est innexistant.")



    def existTable(self, table):
        """ check if the given column exist """
        cursor = self.conn.cursor()
        try :
            cursor.execute("""SELECT  * FROM  %s """ %table)
            return (True)
        except Exception as e:
            return (False)


    def deleteTable(self, table):
        """ delete a table"""
        cursor = self.conn.cursor()
        try :
            cursor.execute("DROP TABLE %s " %table)
            print("table %s supprimée." %table)
        except:
            print("table %s introuvable." %table)

        self.conn.commit()



    def addRow(self, table, file):
        """ complete with the right CSV file a table"""
        # on charge les lignes du fichier CSV
        result=chargerRowCSV(file);
        cursor = self.conn.cursor()

        for elmt in result : # on ajoute chaque ligne à la table
            # conversion de la ligne en chaine de caractere pour l'ajout au sql
            elmt2=str(elmt).strip('[]')
            # print ("DEBUG : %s" %elmt2)
            try:
                cursor.execute("INSERT INTO %s VALUES (%s);" %(table,elmt2))

            except:
                print ("error when trying to INSERT the row %s" %elmt2)

        self.conn.commit()