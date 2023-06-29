class Peluqueria:
    Citas = ''
    Num_atencion = ''
    Nom_cliente = ''
    Fecha = ''
    Des_atencion = ''
    Costo = ''

    def __init__(self):
        self.Citas = '0'
        self.Num_atencion = 'A-001'
        self.Nom_cliente = '0'
        self.Fecha = '0'
        self.Des_atencion = '0'
        self.Costo = '0'

    def selfNum_atencion(self,num_atencion):
        if num_atencion[0:1].isdigit() and num_atencion[2:4].isalpha():
            self.Num_atencion = num_atencion
            return True
        else:
            print("Numero Atencion Incorrecto")
            return False

    def selfDes_atencion(self,des_atencion):
        if len(des_atencion) >= 5 and len(des_atencion) <= 45:
            self.Des_atencion = des_atencion
            return True
        else:
            print("Largo Incorrecto")
            return False

    def selfCosto(self,costo):
        if len(costo) > 20000 and len(costo) <= 45000:
            self.Costo = costo
            return True
        else:
            print("Costo Incorrecto")
            return False


