from PIL import Image
from math import sqrt
from math import floor
from sympy import *
class Teselaciones:
    """
    Functions that generate crystallographic group order. Functions have name as
    the name of the group and supported as input image and range .
    Example:
    >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
    >>> t=Teselaciones(imagen)
    >>> t.p1(2)

    """

    def __init__(self, im):
        self.image = im

    def mini(self):
        """
        Creates a 150x150 pixels thumbnail of the given image, and then squares it
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.mini()
        """
        imag=self.image
        imagaux=imag
        miniatura = (150, 150)
        imagaux.thumbnail(miniatura)
        if imagaux.size[0]>=imagaux.size[1]:
            caja=(0,0,imagaux.size[1],imagaux.size[1])
            cuadrado=imagaux.crop(caja)
        else:
            caja=(0,0,imagaux.size[0],imagaux.size[0])
            cuadrado=imagaux.crop(caja)
        return(cuadrado)

    #------------------------------------------


    def SimVertical(self):
        """
        Creates a vertical symmetry of the given image, return image and symmetry image
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.SimVertical()
        """
        imag=self.mini()
        mp=imag.load()
        imagaux=Image.new("RGB",(imag.size[0]*2,imag.size[1]),"white")
        mpaux=imagaux.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpaux[i,j]=mp[i,j]
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpaux[imag.size[0]+i,j]=mpaux[imag.size[0]-i-1,j]
        return(imagaux)


    #------------------------------------------


    def SimHorizontal(self):
        """
        Creates a horizontal symmetry of the given image, return image and symmetry image
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.SimVertical()
        """
        imag=self.mini()
        mp=imag.load()
        imagaux=Image.new("RGB",(imag.size[0],imag.size[1]*2),"white")
        mpaux=imagaux.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpaux[i,j]=mp[i,j]
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpaux[i,imag.size[1]+j]=mpaux[i,imag.size[1]-j-1]
        return(imagaux)




    #------------------------------------------



    def SimHoDesliz(self):
        """
        Creates a horizontal glide reflection of the given image, return image and symmetry image
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.SimHoDesliz()
        """
        imag=self.mini()
        mp=imag.load()
        imagaux=Image.new("RGB",(imag.size[0]*2,imag.size[1]*2),"white")
        mpaux=imagaux.load()
        imsim=Image.new("RGB",(imag.size[0],imag.size[1]),"white")
        mpsim=imsim.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpsim[i,j]=mp[i,imag.size[1]-j-1]
        imagaux.paste(imag, (0,0))
        imagaux.paste(imag, (0,imag.size[1]))
        imagaux.paste(imsim, (imag.size[0],0))
        imagaux.paste(imsim, (imag.size[0],imag.size[1]))
        return(imagaux)



    #------------------------------------------


    def SimVeDesliz(self):
        """
        Creates a horizontal glide reflection of the given image, return image and symmetry image
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.SimVeDesliz()
        """
        imag=self.mini()
        mp=imag.load()
        imagaux=Image.new("RGB",(imag.size[0]*2,imag.size[1]*2),"white")
        mpaux=imagaux.load()
        imsim=Image.new("RGB",(imag.size[0],imag.size[1]),"white")
        mpsim=imsim.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpsim[i,j]=mp[imag.size[0]-i-1,j]
        imagaux.paste(imag, (0,0))
        imagaux.paste(imsim, (0,imag.size[1]))
        imagaux.paste(imag, (imag.size[0],0))
        imagaux.paste(imsim, (imag.size[0],imag.size[1]))
        return(imagaux)


    #------------------------------------------


    def SimV(self):
        """
        Creates a vertical reflection of the given image, symmetry image
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.SimV()
        """
        imag=self.mini()
        mp=imag.load()
        imagaux=Image.new("RGB",(imag.size[0],imag.size[1]),"white")
        mpaux=imagaux.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpaux[i,j]=mp[imag.size[0]-i-1,j]
        return(imagaux)


    #------------------------------------------
    def SimVok(self):
        """
        Creates a vertical reflection of the given image, symmetry image
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.SimV()
        """
        imag=self.image
        mp=imag.load()
        imagaux=Image.new("RGB",(imag.size[0],imag.size[1]),"white")
        mpaux=imagaux.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpaux[i,j]=mp[imag.size[0]-i-1,j]
        return(imagaux)


    #------------------------------------------

    def SimH(self):
        """
        Creates a horizontal reflection of the given image, return symmetry image
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.SimH()
        """
        imag=self.mini()
        mp=imag.load()
        imagaux=Image.new("RGB",(imag.size[0],imag.size[1]),"white")
        mpaux=imagaux.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpaux[i,j]=mp[i,imag.size[1]-j-1]
        return(imagaux)

     #------------------------------------------
        
        #CRISTALOGRAPHIC GROUPS

    #------------------------------------------


    def p1(self,rang):
        """
        p1 Group containing two linearly independent translations
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.p2(2)


        """


        imag=self.mini()
        im1=Image.new("RGB",(imag.size[0]*rang,imag.size[1]*rang),"white")
        for i in range(0,rang):
            for j in range(0,rang):
                im1.paste(imag, (i*imag.size[0],j*imag.size[1]))
        return(im1)
    #------------------------------------------

    def p2(self,rang):
        """
        Group containing two linearly independent translations and rotations of order two.
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.p2(2)


        """

        imag=self.mini()
        im1=Image.new("RGB",(imag.size[0]*rang*2,imag.size[1]*rang*2),"white")
        im2=Image.new("RGB",(imag.size[0],imag.size[1]*2),"white")
        rot = imag.rotate(180)
        im2.paste(imag, (0,0))
        im2.paste(rot, (0,imag.size[1]))
        for i in range(0,rang*2):
            for j in range(0,rang):
                im1.paste(im2, (i*imag.size[0],j*2*imag.size[1]))
        return(im1)
    #------------------------------------------


    def pm(self,rang):
        """
        Group pm
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.pm(2)

        """

        imag=self.mini()
        im1=Image.new("RGB",(imag.size[0]*rang*2,imag.size[1]*rang*2),"white")
        im2=self.SimVertical()
        for i in range(0,rang):
            for j in range(0,rang*2):
                im1.paste(im2, (i*2*imag.size[0],j*imag.size[1]))
        return(im1)

    #------------------------------------------


    def pg(self,rang):
        """
        Group pg
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.pg(2)


        """
        imag=self.mini()
        im1=Image.new("RGB",(imag.size[0]*rang*2,imag.size[1]*rang*2),"white")
        im2=self.SimHoDesliz()
        for i in range(0,rang*2):
            for j in range(0,rang*2):
                im1.paste(im2, (i*2*imag.size[0],j*2*imag.size[1]))
        return(im1)

#------------------------------------------
    def pmm(self,rang):
        """
        Group pmm
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.pmm(2)


        """
        imag=self.mini()
        imagaux=Image.new("RGB",(imag.size[0]*2,imag.size[1]*2),"white")
        im1=Image.new("RGB",(imag.size[0]*2*rang,imag.size[1]*2*rang),"white")
        imsim=self.SimV()
        imsimH=self.SimH()
        rot = imag.rotate(180)
        imagaux.paste(imag, (0,0))
        imagaux.paste(imsimH, (0,imag.size[1]))
        imagaux.paste(imsim, (imag.size[0],0))
        imagaux.paste(rot, (imag.size[0],imag.size[1]))
        for i in range(0,rang*2):
            for j in range(0,rang*2):
                im1.paste(imagaux, (i*2*imag.size[0],j*2*imag.size[1]))
        return(im1)



#------------------------------------------
    def cm(self,rang):
        """
        Group cm
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.cm(2)


        """
        imag=self.mini()
        imagaux=Image.new("RGB",(imag.size[0]*2,imag.size[1]*2),"white")
        im1=Image.new("RGB",(imag.size[0]*2*rang,imag.size[1]*2*rang),"white")
        imsim=self.SimV()
        imsimH=self.SimH()
        rot = imag.rotate(180)
        imagaux.paste(imag, (0,0))
        imagaux.paste(imsimH, (0,imag.size[1]))
        imagaux.paste(rot, (imag.size[0],0))
        imagaux.paste(imsim, (imag.size[0],imag.size[1]))
        for i in range(0,rang*2):
            for j in range(0,rang*2):
                im1.paste(imagaux, (i*2*imag.size[0],j*2*imag.size[1]))
        return(im1)


#------------------------------------------
    def pgg(self,rang):
        """
        Group pgg
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.pgg(2)


        """
        imag=self.mini()
        imagaux=Image.new("RGB",(imag.size[0]*2,imag.size[1]*2),"white")
        im1=Image.new("RGB",(imag.size[0]*2*rang,imag.size[1]*2*rang),"white")
        imsim=self.SimV()
        imsimH=self.SimH()
        rot = imag.rotate(180)
        imagaux.paste(imag, (0,0))
        imagaux.paste(imsim, (0,imag.size[1]))
        imagaux.paste(imsimH, (imag.size[0],0))
        imagaux.paste(rot, (imag.size[0],imag.size[1]))
        for i in range(0,rang*2):
            for j in range(0,rang*2):
                im1.paste(imagaux, (i*2*imag.size[0],j*2*imag.size[1]))
        return(im1)

#------------------------------------------
    def pmg(self,rang):
        """
        Group pmg
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.pmg(2)


        """
        imag=self.mini()
        imagaux=Image.new("RGB",(imag.size[0]*2,imag.size[1]*2),"white")
        im1=Image.new("RGB",(imag.size[0]*2*rang,imag.size[1]*2*rang),"white")
        imsim=self.SimV()
        imsimH=self.SimH()
        rot = imag.rotate(180)
        imagaux.paste(imag, (0,0))
        imagaux.paste(imsimH, (0,imag.size[1]))
        imagaux.paste(rot, (imag.size[0],0))
        imagaux.paste(imsim, (imag.size[0],imag.size[1]))
        for i in range(0,rang*2):
            for j in range(0,rang*2):
                im1.paste(imagaux, (i*2*imag.size[0],j*2*imag.size[1]))
        return(im1)
#------------------------------------------
    def p4(self,rang):
        """
        Group p4
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.p4(2)


        """
        imag=self.mini()
        imagaux=Image.new("RGB",(imag.size[0]*2,imag.size[1]*2),"white")
        im1=Image.new("RGB",(imag.size[0]*2*rang,imag.size[1]*2*rang),"white")
        rot1 = imag.rotate(270)
        rot2 = imag.rotate(180)
        rot3 = rot1.rotate(180)
        imagaux.paste(imag, (0,0))
        imagaux.paste(rot3, (0,imag.size[1]))
        imagaux.paste(rot1, (imag.size[0],0))
        imagaux.paste(rot2, (imag.size[0],imag.size[1]))
        for i in range(0,rang*2):
            for j in range(0,rang*2):
                im1.paste(imagaux, (i*2*imag.size[0],j*2*imag.size[1]))
        return(im1)



#------------------------------------------
    def triangulo(self):
        """
        Creates a triangle of the image.
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.triangulo(2)


        """
        imag=self.image
        mp=imag.load()
        imagaux=Image.new("RGBA",(imag.size[0],imag.size[1]),"white")
        mpaux=imagaux.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                if j>=(-2*imag.size[1]/imag.size[0])*i+imag.size[1] and j>=(2*imag.size[1]/imag.size[0])*i-imag.size[1]:
                    mpaux[i,j]=mp[i,j]
                else:
                    mpaux[i,j]=(255,255,255,0)
        return(imagaux)

#------------------------------------------

    def cmm(self,rang):
        """
        Group cmm
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.cmm(2)


        """
        imag=self.mini()
        mp=imag.load()
        imagaux=self.triangulo()
        mpaux=imagaux.load()
        im1=Image.new("RGBA",(imag.size[0]*2,imag.size[1]*2),"white")
        fin=Image.new("RGB",(imag.size[0]*2*rang,imag.size[1]*2*rang),"white")
        mpf=fin.load()
        mpim1=im1.load()
        imsim=Image.new("RGBA",(imag.size[0],imag.size[1]),"white")
        mpsim=imsim.load()
        s=Image.new("RGBA",(imag.size[0],imag.size[1]),"white")
        mps=s.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpsim[i,j]=mpaux[i,imag.size[1]-j-1]
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mps[i,j]=mpsim[i,imag.size[1]-j-1]
        im1.paste(imagaux, (0,0))
        im1.paste(imsim, (floor(imag.size[0]/2),0), imsim)
        im1.paste(imsim, (0,imag.size[1]))
        im1.paste(s, (floor(imag.size[0]/2),imag.size[1]),s)
        for i in range(-1,rang*2):
            for j in range(0,rang*2):
                fin.paste(im1, (i*imag.size[0],j*2*imag.size[1]),im1)
        return(fin)

    #------------------------------------------

    def divi1(self):
        """
        Divide image in diagonal
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.divi1(2)


        """
        imag=self.mini()
        mp=imag.load()
        imagaux=Image.new("RGBA",(imag.size[0],imag.size[1]),"white")
        mpaux=imagaux.load()
        rot=imag.rotate(90)
        srot=self.SimV()
        rot2=srot.rotate(90)
        mprot2=rot2.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                if j>=(imag.size[1]/imag.size[0])*i:
                    mpaux[i,j]=mp[i,j]
                else:
                    mpaux[i,j]=mprot2[i,j]
        return(imagaux)
#------------------------------------------
    def p4mm(self,rang):
        """
        Group p4mm
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.p4mm(2)


        """

        imag=self.mini()
        aux=self.divi1()
        im1=Teselaciones(aux).p4(rang)
        return(im1)
#------------------------------------------
    def divi2(self):
        """
        Divide image in diagonal
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.divi2(2)


        """
        imag=self.mini()
        mp=imag.load()
        imagaux=Image.new("RGBA",(imag.size[0],imag.size[1]),"white")
        mpaux=imagaux.load()
        rot=imag.rotate(-90)
        srot=self.SimV()
        rot2=srot.rotate(-90)
        mprot2=rot2.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                if j>=(-imag.size[1]/imag.size[0])*i+imag.size[1]:
                    mpaux[i,j]=mp[i,j]
                else:
                    mpaux[i,j]=mprot2[i,j]
        return(imagaux)
#------------------------------------------
    def p4g(self,rang):
        """
        Group p4g
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.p4g(2)


        """
        imag=self.mini()
        aux=self.divi2()
        im1=Teselaciones(aux).p4(rang)
        return(im1)

#------------------------------------------
    def equilatero(self):
        """
        Creates a equilater triangle of the image.
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.triangulo(2)
        """

        imag=self.mini()
        caja = (0, imag.size[1]-floor(sqrt(imag.size[1]**2-(imag.size[1]/2)**2)), imag.size[0], imag.size[1])
        modif = imag.crop(caja)
        tmod=Teselaciones(modif).triangulo()
        return(tmod)




#------------------------------------------
    def p3(self,rang):
        """
        Group p3
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.p3(2)


        """

        imag=self.mini()
        mp=imag.load()
        imagaux=self.equilatero()
        mpaux=imagaux.load()
        im1=Image.new("RGBA",(imagaux.size[0]*3,imagaux.size[1]*3),(255,255,255,0))
        fin=Image.new("RGBA",(imagaux.size[0]*3*rang,imagaux.size[1]*3*rang),(255,255,255,0))
        fin2=Image.new("RGBA",(imagaux.size[0]*3*rang,imagaux.size[1]*3*rang),(255,255,255,0))
        mpf=fin.load()
        mpim1=im1.load()
        imsim=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mpsim=imsim.load()
        s=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mps=s.load()
        s2=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mps2=s2.load()
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mpsim[i,j]=mpaux[i,imagaux.size[1]-j-1]
        rc=imsim.rotate(-120, expand=1)
        caja=(rc.size[0]-imagaux.size[0],rc.size[1]-imagaux.size[1],rc.size[0],rc.size[1])
        rc2=rc.crop(caja)
        mprc2=rc2.load()
        rccc=imagaux.rotate(-120, expand=1)
        caja3=(0,0,imagaux.size[0],imagaux.size[1])
        rccc2=rccc.crop(caja3)
        mprccc2=rccc2.load()
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mps[i,j]=mprc2[i,imagaux.size[1]-j-1]
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mps2[i,j]=mprccc2[i,imagaux.size[1]-j-1]
        im1.paste(imagaux, (0,0))
        im1.paste(s, (floor(imagaux.size[0]/2),imagaux.size[1]),s)
        im1.paste(rccc2, (imagaux.size[0],0),rccc2)
        for i in range(-2,rang*2):
            for j in range(-2,rang*2):
                fin.paste(im1, (i*3*imagaux.size[0]-i,j*2*imagaux.size[1]),im1)
        for i in range(-2,rang*2):
            for j in range(-2,rang*2):
                fin2.paste(im1, (i*3*imagaux.size[0]-imagaux.size[0]-floor((1/2)*imagaux.size[0])-i,j*2*imagaux.size[1]-imagaux.size[1]),im1)
        fin2.paste(fin, fin)
        return(fin2)

#------------------------------------------
    def p31m(self,rang):
        """
        Group p31m
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.p31m(2)


        """

        imagaux=self.equilatero()
        mpaux=imagaux.load()
        im1=Image.new("RGBA",(imagaux.size[0]*3,imagaux.size[1]*3),(255,255,255,0))
        fin=Image.new("RGBA",(imagaux.size[0]*3*rang,imagaux.size[1]*3*rang),(255,255,255,0))
        fin2=Image.new("RGBA",(imagaux.size[0]*3*rang,imagaux.size[1]*3*rang),(255,255,255,0))
        mpf=fin.load()
        mpim1=im1.load()
        imsim=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mpsim=imsim.load()
        s=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mps=s.load()
        s2=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mps2=s2.load()
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mpsim[i,j]=mpaux[i,imagaux.size[1]-j-1]
        rc=imsim.rotate(-120, expand=1)
        caja=(rc.size[0]-imagaux.size[0],rc.size[1]-imagaux.size[1],rc.size[0],rc.size[1])
        rc2=rc.crop(caja)
        mprc2=rc2.load()
        rccc=imagaux.rotate(-120, expand=1)
        caja3=(0,0,imagaux.size[0],imagaux.size[1])
        rccc2=rccc.crop(caja3)
        mprccc2=rccc2.load()
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mps[i,j]=mprc2[i,imagaux.size[1]-j-1]
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mps2[i,j]=mprccc2[i,imagaux.size[1]-j-1]
        im1.paste(imagaux, (0,0))
        im1.paste(rc2, (floor(imagaux.size[0]/2),0),rc2)
        im1.paste(imsim, (0,imagaux.size[1]))
        im1.paste(s, (floor(imagaux.size[0]/2),imagaux.size[1]),s)
        im1.paste(rccc2, (imagaux.size[0]-2,0),rccc2)
        im1.paste(s2,(imagaux.size[0]-2,imagaux.size[1]),s2)
        for i in range(-2,rang*2):
            for j in range(-2,rang*2):
                fin.paste(im1, (i*3*imagaux.size[0]-i,j*2*imagaux.size[1]),im1)
        for i in range(-2,rang*2):
            for j in range(-2,rang*2):
                fin2.paste(im1, (i*3*imagaux.size[0]-imagaux.size[0]-floor((1/2)*imagaux.size[0])-i,j*2*imagaux.size[1]-imagaux.size[1]),im1)
        fin2.paste(fin, fin)
        return(fin2)
#------------------------------------------
    def fundam(self):
        """
        divide a triangle in three same parts, an return one of them.
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.fundam(2)


        """

        im=self.equilatero()
        mp=im.load()
        imaux=Image.new("RGBA",(im.size[0],im.size[1]),"white")
        mpaux=imaux.load()
        for i in range(im.size[0]):
            for j in range(im.size[1]):
                if j<=((-2/3)*im.size[1]/im.size[0])*i+im.size[1] and i<im.size[0]/2:
                    mpaux[i,j]=mp[i,j]
                else:
                    mpaux[i,j]=(255,255,255,0)
        return(imaux)

#------------------------------------------
    def fundam2(self):
        """
        Divide a triangle in three same parts.
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.fundam2(2)


        """
        pp=self.fundam()
        pp2=pp.rotate(-120, expand=1)
        pp3=pp.rotate(120, expand=1)
        ppaux=Image.new("RGBA",(pp3.size[0],pp3.size[1]),"white")
        ppaux.paste(pp, (0,0))
        ppaux.paste(pp2, (0,0),pp2)
        ppaux.paste(pp3, (-floor(pp.size[0]/4)-1,0),pp3)
        aux=self.equilatero()
        caja=(0,0,aux.size[0],aux.size[1])
        ppaux2=ppaux.crop(caja)
        return(ppaux2)
#------------------------------------------
    def p3m1(self,rang):
        """
        Group p3m1
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.p3m1(2)


        """

        imag=self.mini()
        imagaux=self.fundam2()
        mpaux=imagaux.load()
        im1=Image.new("RGBA",(imagaux.size[0]*3,imagaux.size[1]*3),(255,255,255,0))
        fin=Image.new("RGBA",(imagaux.size[0]*3*rang,imagaux.size[1]*3*rang),(255,255,255,0))
        fin2=Image.new("RGBA",(imagaux.size[0]*3*rang,imagaux.size[1]*3*rang),(255,255,255,0))
        mpf=fin.load()
        mpim1=im1.load()
        imsim=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mpsim=imsim.load()
        s=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mps=s.load()
        s2=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mps2=s2.load()
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mpsim[i,j]=mpaux[i,imagaux.size[1]-j-1]
        rc=imsim.rotate(-120, expand=1)
        caja=(rc.size[0]-imagaux.size[0],rc.size[1]-imagaux.size[1],rc.size[0],rc.size[1])
        rc2=rc.crop(caja)
        mprc2=rc2.load()
        rccc=imagaux.rotate(-120, expand=1)
        caja3=(0,0,imagaux.size[0],imagaux.size[1])
        rccc2=rccc.crop(caja3)
        mprccc2=rccc2.load()
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mps[i,j]=mprc2[i,imagaux.size[1]-j-1]
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mps2[i,j]=mprccc2[i,imagaux.size[1]-j-1]
        im1.paste(imagaux, (0,0))
        im1.paste(rc2, (floor(imagaux.size[0]/2)-1,0),rc2)
        im1.paste(rc2, (0,imagaux.size[1]),rc2)
        im1.paste(imagaux, (floor(imagaux.size[0]/2),imagaux.size[1]),imagaux)
        im1.paste(imagaux, (imagaux.size[0],0),imagaux)
        im1.paste(rc2,(imagaux.size[0]-1,imagaux.size[1]),rc2)
        for i in range(-2,rang*2):
            for j in range(-2,rang*2):
                fin.paste(im1, (i*3*imagaux.size[0],j*2*imagaux.size[1]),im1)
        for i in range(-2,rang*2):
            for j in range(-2,rang*2):
                fin2.paste(im1, (i*3*imagaux.size[0]-imagaux.size[0]-floor((1/2)*imagaux.size[0]),j*2*imagaux.size[1]-imagaux.size[1]),im1)
        fin2.paste(fin, fin)
        return(fin2)


#------------------------------------------
    def p6(self,rang):
        """
        Group p6
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.p6(2)


        """

        imag=self.mini()
        imagaux=self.fundam2()
        mpaux=imagaux.load()
        im1=Image.new("RGBA",(imagaux.size[0]*3,imagaux.size[1]*3),(255,255,255,0))
        fin=Image.new("RGBA",(imagaux.size[0]*3*rang,imagaux.size[1]*3*rang),(255,255,255,0))
        fin2=Image.new("RGBA",(imagaux.size[0]*3*rang,imagaux.size[1]*3*rang),(255,255,255,0))
        mpf=fin.load()
        mpim1=im1.load()
        imsim=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mpsim=imsim.load()
        s=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),"white")
        mps=s.load()
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mpsim[i,j]=mpaux[i,imagaux.size[1]-j-1]
        rc=imsim.rotate(-120, expand=1)
        caja=(rc.size[0]-imagaux.size[0],rc.size[1]-imagaux.size[1],rc.size[0],rc.size[1])
        rc2=rc.crop(caja)
        mprc2=rc2.load()
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mps[i,j]=mprc2[imagaux.size[0]-i-1,j]
        im1.paste(imagaux, (0,0))
        im1.paste(s, (floor(imagaux.size[0]/2),0),s)
        im1.paste(s, (0,imagaux.size[1]),s)
        im1.paste(imagaux, (floor(imagaux.size[0]/2),imagaux.size[1]),imagaux)
        im1.paste(imagaux, (imagaux.size[0],0),imagaux)
        im1.paste(s,(imagaux.size[0],imagaux.size[1]),s)
        for i in range(-2,rang*2):
            for j in range(-2,rang*2):
                fin.paste(im1, (i*3*imagaux.size[0],j*2*imagaux.size[1]),im1)
        for i in range(-2,rang*2):
            for j in range(-2,rang*2):
                fin2.paste(im1, (i*3*imagaux.size[0]-imagaux.size[0]-floor((1/2)*imagaux.size[0]),j*2*imagaux.size[1]-imagaux.size[1]),im1)
        fin2.paste(fin, fin)
        return(fin2)

#------------------------------------------
    def fundam3(self):
        """
        divide a triangle in six same parts, an return one of them.
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.fundam3(2)


        """


        im=self.equilatero()
        mp=im.load()
        imaux=Image.new("RGBA",(im.size[0],im.size[1]),"white")
        mpaux=imaux.load()
        for i in range(im.size[0]):
            for j in range(im.size[1]):
                if j<=((-2/3)*im.size[1]/im.size[0])*i+im.size[1] and j<=((2/3)*im.size[1]/im.size[0])*i+im.size[1]/3 and i<im.size[0]/2:
                    mpaux[i,j]=mp[i,j]
                else:
                    mpaux[i,j]=(255,255,255,0)
        return(imaux)
#------------------------------------------
    def fundam4(self):
        """
        divide a triangle in six same parts.
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.fundam3(2)


        """
        im1=self.fundam3()
        mpim1=im1.load()
        im2=im1.rotate(180)
        im3=Teselaciones(im2).SimVok().rotate(-60, expand=1)
        caja=(im3.size[0]-im1.size[0],0,im3.size[0],im1.size[1])
        im4=im3.crop(caja)
        mpim4=im4.load()
        imaux=Image.new("RGBA",(im1.size[0],im1.size[1]),(255,255,255,0))
        mpaux=imaux.load()
        for i in range(im4.size[0]):
            for j in range(im4.size[1]):
                if j<((-2/3)*im4.size[1]/im4.size[0])*i+im4.size[1] and j>=((2/3)*im4.size[1]/im4.size[0])*i+im4.size[1]/3 and i<im4.size[0]/2:
                    mpaux[i,j]=mpim4[i,j]
                else:
                    mpaux[i,j]=mpim1[i,j]
        pp2=imaux.rotate(-120, expand=1)
        pp3=imaux.rotate(120, expand=1)
        ppaux=Image.new("RGBA",(pp3.size[0],pp3.size[1]),(255,255,255,0))
        ppaux.paste(imaux, (0,0))
        ppaux.paste(pp2, (1,0),pp2)
        ppaux.paste(pp3, (-floor(imaux.size[0]/4),0),pp3)
        caja=(0,0,im1.size[0],im1.size[1])
        ppaux2=ppaux.crop(caja)
        fin=Teselaciones(ppaux2).triangulo()
        return(fin)
#------------------------------------------
    def p6m(self,rang):
        """
        Group p6m
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.p6m(2)


        """
        imag=self.mini()
        mp=imag.load()
        imagaux=self.fundam4()
        mpaux=imagaux.load()
        im=Image.new("RGBA",(imagaux.size[0]*3,imagaux.size[1]*3),(255,255,255,0))
        fin=Image.new("RGBA",(imagaux.size[0]*3*rang,imagaux.size[1]*3*rang),(255,255,255,0)) 
        fin2=Image.new("RGBA",(imagaux.size[0]*3*rang,imagaux.size[1]*3*rang),(255,255,255,0)) 
        mpf=fin.load()
        mpim=im.load()
        imsim=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),(255,255,255,0))
        mpsim=imsim.load()
        s=Image.new("RGBA",(imagaux.size[0],imagaux.size[1]),(255,255,255,0))
        mps=s.load()
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mpsim[i,j]=mpaux[i,imagaux.size[1]-j-1]
        rc=imsim.rotate(-120, expand=1)
        caja=(rc.size[0]-imagaux.size[0],rc.size[1]-imagaux.size[1],rc.size[0],rc.size[1])
        rc2=rc.crop(caja)
        mprc2=rc2.load()
        for i in range(imagaux.size[0]):
            for j in range(imagaux.size[1]):
                mps[i,j]=mprc2[imagaux.size[0]-i-1,j]
        im.paste(imagaux, (0,0))
        im.paste(s, (floor(imagaux.size[0]/2)+2,0),s)
        im.paste(s, (2,imagaux.size[1]-1),s)
        im.paste(imagaux, (floor(imagaux.size[0]/2)+1,imagaux.size[1]),imagaux)
        im.paste(imagaux, (imagaux.size[0]+1,0),imagaux)
        im.paste(s,(imagaux.size[0]+2,imagaux.size[1]-1),s)
        for i in range(-2,rang*2):
            for j in range(-2,rang*2):
                fin.paste(im, (i*3*imagaux.size[0],j*2*(imagaux.size[1])),im)
        for i in range(-2,rang*2):
            for j in range(-2,rang*2):
                fin2.paste(im, (i*3*imagaux.size[0]-imagaux.size[0]-floor((1/2)*imagaux.size[0]),j*2*imagaux.size[1]-imagaux.size[1]),im)
        fin2.paste(fin, fin)
        return(fin2)
    



#------------------------------------------
#------------------------------------------

#FRIEZE GROUPS
#------------------------------------------
    def F1(self,rang):
        """
        Group F1
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.F1(2)


        """
        imag=self.mini()
        im1=Image.new("RGB",(imag.size[0]*rang,imag.size[1]),"white")
        for i in range(0,rang):
                im1.paste(imag, (i*imag.size[0],0))
        return(im1)
#------------------------------------------
    def F11(self,rang):
        """
        Group F11
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.F11(2)


        """
        imag=self.mini()
        imag=self.SimHorizontal()
        im1=Image.new("RGB",(imag.size[0]*rang,imag.size[1]),"white")
        for i in range(0,rang):
                im1.paste(imag, (i*imag.size[0],0))
        return(im1)
#------------------------------------------
    def F12(self,rang):
        """
        Group F12
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.F12(2)


        """
        imag=self.mini()
        imag=self.SimVertical()
        im1=Image.new("RGB",(imag.size[0]*rang,imag.size[1]),"white")
        for i in range(0,rang):
                im1.paste(imag, (i*imag.size[0],0))
        return(im1)
#------------------------------------------
    def F13(self,rang):
        """
        Group F13
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.F13(2)


        """
        imag=self.mini()
        imag=self.SimHoDesliz()
        im1=Image.new("RGB",(imag.size[0]*rang,imag.size[1]),"white")
        for i in range(0,rang):
                im1.paste(imag, (i*imag.size[0],0))
        return(im1)
#------------------------------------------
    def F2(self,rang):
        """
        Group F2
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.F2(2)


        """
        imag=self.mini()
        imag=self.equilatero()
        imagr=imag.rotate(180)
        im1=Image.new("RGBA",(imag.size[0]*2,imag.size[1]),(255,255,255,0))
        im1.paste(imag, (0,0))
        im1.paste(imagr, (floor(imag.size[0]/2),0),imagr)
        im2=Image.new("RGBA",(imag.size[0]*rang*2,imag.size[1]),(255,255,255,0))
        for i in range(0,rang):
                im2.paste(im1, (i*imag.size[0],0),im1)
        return(im2)
#------------------------------------------
    def F21(self,rang):
        """
        Group F21
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.F21(2)


        """
        imag=self.mini()
        imag=self.SimHorizontal()
        imagr=imag.rotate(180)
        im1=Image.new("RGB",(imag.size[0]*2,imag.size[1]),"white")
        im1.paste(imag, (0,0))
        im1.paste(imagr, (imag.size[0],0))
        im2=Image.new("RGB",(imag.size[0]*rang*2,imag.size[1]),"white")
        for i in range(0,rang):
                im2.paste(im1, (i*im1.size[0],0))
        return(im2)
#------------------------------------------
    def F22(self,rang):
        """
        Group F22
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.F21(2)


        """
        imag=self.mini()
        imagr=imag.rotate(180)
        imagrs=Teselaciones(imagr).SimV()
        imags=self.SimV()
        im1=Image.new("RGB",(imag.size[0]*2,imag.size[1]*2),"white")
        im1.paste(imag, (0,0))
        im1.paste(imagr, (0,imag.size[1]))
        im1.paste(imags, (imag.size[0],0))
        im1.paste(imagrs,(imag.size[0],imag.size[1]))
        im2=Image.new("RGB",(imag.size[0]*rang*2,imag.size[1]*2),"white")
        for i in range(0,rang):
                im2.paste(im1, (i*im1.size[0],0))
        return(im2)
#------------------------------------------
#------------------------------------------
