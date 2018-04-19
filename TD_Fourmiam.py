import math as m 
import random as r
import pants as p
import csv
import networkx as network
import matplotlib.pyplot as pyp

def function(noeuds_x, noeuds_y):
    distance = m.sqrt(pow(noeuds_x[1] - noeuds_y[1],2) + pow(noeuds_x[1] + noeuds_y[1],2))
    return distance

def find_road(graph, debut, fin, road=[]): #Fonction permettant de créer le chemin de noeud en noeud du début à la fin
        road = road + [debut]
        if debut == fin:
            return road
        if not graph.has_key(road):
            return None
        for node in graph[road]:
            if node not in road:
                newroad = find_road(graph, node, fin, road)
                if newroad: return newroad
        return None

Graph = network.Graph()
network.draw(Graph)
pyp.draw() #On dessine le Graph

with open('VOIES_NM.csv') as fichier_csv: #Ici on définit le fichier qui doit être lu
    reader = csv.DictReader(fichier_csv) #Et ici on associe le fichier au reader
    k = 0
    for ligne in reader: #On lit les 100 premières lignes du fichier VOIES_NM.Csv 
        k += 1
        if k < 100:
            Adresse = ligne['COMMUNE'] + '' + ligne['LIBELLE'] #On définit l'adresse
            Tenant = ligne['TENANT'] #On définit le tenant
            Aboutissant = ligne['ABOUTISSANT'] #On définit l'aboutissant
            Statut = ligne['STATUT'] #On définit le statut
            if Tenant != "" and Aboutissant != "": #Ici on regarde si les tenants et aboutissants sont nuls ou non
                if (ligne['BI_MIN'] == ""): #Si BI_MIN est null on lui affecte par défaut la valeur 1
                    ligne['BI_MIN'] = 1
                else:
                    ligne['BI_MIN'] = int(ligne['BI_MIN'])
                if (ligne['BP_MIN'] == ""): #Même chose que pour BI_MIN
                    ligne['BP_MIN'] = 1
                else:
                    ligne['BP_MIN'] = int(ligne['BP_MIN'])
                if (ligne['BI_MAX'] == ""): #Même chose que pour BI_MIN
                    ligne['BI_MAX'] = 1
                else:
                    ligne['BI_MAX'] = int(ligne['BI_MAX']) 
                if (ligne['BP_MAX'] == ""): #Même chose que pour BI_MIN
                    ligne['BP_MAX'] = 1
                else:
                    ligne['BP_MAX'] = int(ligne['BP_MAX'])
                
                Poids = max((ligne['BI_MAX'] - ligne['BI_MIN'])/2, (ligne['BP_MAX'] - ligne['BP_MIN'])/2) #On définit ici le poids
                Graph.add_edge(ligne['TENANT'], ligne['ABOUTISSANT'], weight=Poids, label=ligne['LIBELLE']) #On ajoute les arêtes
                #print(Tenant, Aboutissant)
                #print(Poids)
                pos = network.spring_layout(Graph) #
                #print(network.get_edge_attributes(Graph, 'weight'))
                #print(network.get_edge_attributes(Graph, 'label'))
                tab_poids = network.get_edge_attributes(Graph,'weight') #On récupère le poids des arêtes
                tab_nom = network.get_edge_attributes(Graph,'label') #On récupère les labels des arêtes
                
                for x in tab_nom:
                    print(tab_nom[x],tab_poids[x]) #On affiche le nom et le poids de chaque rue
 
network.draw_networkx_edges(Graph, pos) # On récupère les traits du schéma
network.draw_networkx_labels(Graph, pos)  #On récupère les noms
network.draw_networkx_edge_labels(Graph, pos) #On récupère les noms sur les arêtes
network.draw_networkx_nodes(Graph, pos) #On récupère les points rouge
pyp.show() 

 
noeuds = [] 
choix = r.randint(1,10)
 
for i in range(choix):
    x = r.uniform(0,10)
    y = r.uniform(0,10)
    noeuds.append([x,y])
     
ensemble = p.World(noeuds,function)
solver = p.Solver()
solutions = solver.solutions(ensemble)
 
for solution in solutions:
     print(solution.distance)
 
print(noeuds)


        

