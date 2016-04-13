# -*- coding: utf-8 -*-
""" controllo AHP, cioè che dati
        una lista di opz    opzioni m 
        una lista di crit   criteri c
        un vettore di anls  analisi c
        una matrice di g    giudizi m·c
            ottengo il ranking delle opzioni
                lista ordinata e valore                 """
import unittest 
import os
import numpy as np
# import ML
import matplotlib.pyplot as plt

import ahp

a1 = ahp.ahp()
HERE = os.path.dirname(os.path.realpath(__file__))

class LearningCase(unittest.TestCase):

    def setUp(self):
        pass # plt.close('all') # closes all the figure windows

    def tearDown(self):    
        pass # plt.close('all') # closes all the figure windows

    """def test_input_leggi(self):
        # valuto se prende casualmente un numero
        self.assertEqual(a1.input(), ['a', 's'])"""

    def test_giudizio_da_matrice(self):
        """valuto il giudizio è giusto """
        self.assertEqual(a1.giudizio_da_matrice([[1, 1., 1], [1, 1, 1], [1, 1, 1]])[2, 0], 1./3)
        # self.assertEqual(a1.giudizio_da_matrice([[1, 1, 1], [1, 1, 1], [1, 1, 1]])[2, 0], 1./3)
        # errore se input int !!!

    def test_equiparo_lunghezze(self):
        """max(mylist, key=len)"""
        c = ['', '1234', '12']
        # equiparo_lunghezze(self, lista):
        self.assertEqual(len(a1.equiparo_lunghezze(c)[0]), 4)
        self.assertEqual(len(a1.equiparo_lunghezze(c)[2]), 4)

    def test_normalizzazione(self):
        """lineare or Square or Square Root 
            https://www.mathsisfun.com/sets/function-inverse.html 
            values, x_min, x_max, type = "linear")"""
        values = [3, 9, 12]
        self.assertEqual(a1.normalizzazione(values, x_min = 3, x_max=12)[0], 0)
        self.assertAlmostEqual(a1.normalizzazione(values, x_min = 3, x_max=12)[1], .666666666)    
        self.assertEqual(a1.normalizzazione(values, x_min = 3, x_max=12)[2], 1)   
        values = [70.7106781187, 77.45966692418, 94.8683298051, 100]          # `}}
        self.assertAlmostEqual(a1.normalizzazione(values, 0, 100, "Square")[0], 0.5)
        self.assertAlmostEqual(a1.normalizzazione(values, 0, 100, "Square")[1], 0.6)    
        self.assertAlmostEqual(a1.normalizzazione(values, 0, 100, "Square")[2], 0.9)   
        self.assertEqual(a1.normalizzazione(values, 0, 100, "Square")[3], 1)   
        
        values = [25, 36, 81, 100]          # `}}
        self.assertEqual(a1.normalizzazione(values, 0, 100, "Square Root")[0], 0.5)
        self.assertEqual(a1.normalizzazione(values, 0, 100, "Square Root")[1], 0.6)    
        self.assertEqual(a1.normalizzazione(values, 0, 100, "Square Root")[2], 0.9)   
        self.assertEqual(a1.normalizzazione(values, 0, 100, "Square Root")[3], 1)   
        

    def test_read_external_file(self):
        """ Read en external data file """
        # self.assertEqual(a1.giudizio_da_matrice([[1, 1., 1], [1, 1, 1], [1, 1, 1]])[2, 0], 1./3)
        # self.assertEqual(a1.giudizio_da_matrice([[1, 1, 1], [1, 1, 1], [1, 1, 1]])[2, 0], 1./3)
        # a1.esecuzione(  ])

        # parametri  
        dd1 = a1.risultato( opz = ['gato', 'perro', 'pez',],
                             c = ['autonomia', 'economicidad ', 'compañia', 'belleza'], 
                            G = [[10, 7, 7, 9], [5, 5, 10, 7], [10, 9, 2, 5]], 
                            C = [[1,  8,  7, 9], [0.125,  1,  7, 8], [ 0.14,.11,  1, 7], [0.111,.12,.11 , 1]] )
        self.assertEqual(dd1['gato'],  8.531705970502406)

        # read parameters from file 
        opz, c, G , C = a1.inp_from_file("pet.txt")
        dd2 = a1.risultato( opz, c, G, C )
        self.assertEqual(dd2['gato'],  8.531705970502406)

    def test_read_external_file_(self):
        # Read en external data file 
        # read parameters from file 
        opz, c, G , C = a1.inpt_from_file("pets.txt")
        dd2 = a1.risultato( opz, c, G, C )
        self.assertEqual(dd2['gato'],  8.531705970502406)   


    def test_gira_matrice(self):
        # fronm a list of string values e list of float
        self.assertEqual( 86,  sum([sum(i) for i in a1.gira_matrice() ]))   


        pass


def main():
    unittest.main()

# Esecuzione ========================================
if __name__ == "__main__":
    
    print "Hi"
    main()
    print "Text not shown"
