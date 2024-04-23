import unittest

from db import ver_datos

class test_db(unittest.TestCase):
    database = {
            '1':{
                "nombre1":"Pablo",
                "nombre2":"Diego",
                "apellido1":"Ruiz",
                "apellido2":"Picasso"
            },
            '2':{
                "nombre1":"Elio",
                "apellido1":"Anci"
            },
            '3':{
                "nombre1":"Elias",
                "nombre2":"Marcos",
                "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"
            },
            '4':{
                "nombre":"Sofia",
                "apellido":"Soler"
            },
            '5':{
                "nombre":"Sofia",
                "apellido":"Ramirez"
            }
                }
    
    def test_1(self):
        resultado = ver_datos("Pablo", "Diego","Ruiz","Picasso", **self.database)
        self.assertEqual(resultado, '1')

    def test_3(self):
        resultado = ver_datos("Marcos", "Marcelo","Luciano","Elias","Gonzalez",**self.database)
        self.assertEqual(resultado, '3')

    def test_nohay(self):
        resultado = ver_datos("Marquitos", **self.database)
        self.assertEqual(resultado, 'no hay')

    def test_sofia(self):
        resultado = ver_datos("Sofia", **self.database)
        self.assertEqual(resultado, 'Hay 2 ID con el mismo nombre')

    def test_sofiax2(self):
        resultado = ver_datos("Sofia", "Ramirez", **self.database)
        self.assertEqual(resultado, '5')

    def test_trampa_esta_pero_no_es_ninguno(self):
        resultado = ver_datos("Sofia", "Ramirez", "Soler", **self.database)
        self.assertEqual(resultado, 'no hay')


if __name__ == '__main__':
    unittest.main()
