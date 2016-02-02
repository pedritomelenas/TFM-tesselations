from PIL import Image
from math import floor

class Teselaciones:
    """
    Funciones que generan el grupo cristalografico pedido. Las funciones tienen como nombre
    el nombre del grupo y admite como entrada la imagen y el rango.
    Example:
    >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
    >>> t=Teselaciones(imagen)
    >>> t.p1(2)

    """

    def __init__(self, im):
        self.image = im

    def mini(self):
        """
        Creates a 200x200 pixels thumbnail of the given image, and then squares it
        Example:
        >>> imagen = Image.open("Ejemplos/salamanquesa.jpeg")
        >>> t=Teselaciones(imagen)
        >>> t.mini()
        """
        imag=self.image
        imagaux=imag
        miniatura = (200, 200)
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
        imag=self.image
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
        imag=self.image
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
        imag=self.image
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
        imag=self.image
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
        imag=self.imag
        mp=imag.load()
        imagaux=Image.new("RGB",(imag.size[0],imag.size[1]),"white")
        mpaux=imagaux.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpaux[i,j]=mp[imag.size[0]-i-1,j]
        return(imagaux)


    #------------------------------------------

    def SimH(self):
        imag=self.imag
        mp=imag.load()
        imagaux=Image.new("RGB",(imag.size[0],imag.size[1]),"white")
        mpaux=imagaux.load()
        for i in range(imag.size[0]):
            for j in range(imag.size[1]):
                mpaux[i,j]=mp[i,imag.size[1]-j-1]
        return(imagaux)






    def p1(self,rang):
        """Grupo que contiene dos traslaciones linealmente indepencientes"""
        imag=self.image
        im1=Image.new("RGB",(imag.size[0]*rang,imag.size[1]*rang),"white")
        for i in range(0,rang):
            for j in range(0,rang):
                im1.paste(imag, (i*imag.size[0],j*imag.size[1]))
        return(im1)
