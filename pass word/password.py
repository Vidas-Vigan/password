import string
def crypteur(Base):
    Caracteres=Base
    Caracteres=str(Caracteres)
    # Minuscules
    Caracteres=string.replace(Caracteres,"a","[m01]")
    Caracteres=string.replace(Caracteres,"b","[m02]")
    Caracteres=string.replace(Caracteres,"c","[m03]")
    Caracteres=string.replace(Caracteres,"d","[m04]")
    Caracteres=string.replace(Caracteres,"e","[m05]")
    Caracteres=string.replace(Caracteres,"f","[m06]")
    Caracteres=string.replace(Caracteres,"g","[m07]")
    Caracteres=string.replace(Caracteres,"h","[m08]")
    Caracteres=string.replace(Caracteres,"i","[m09]")
    Caracteres=string.replace(Caracteres,"j","[m10]")
    Caracteres=string.replace(Caracteres,"k","[m11]")
    Caracteres=string.replace(Caracteres,"l","[m12]")
    Caracteres=string.replace(Caracteres,"m","[m13]")
    Caracteres=string.replace(Caracteres,"n","[m12]")
    Caracteres=string.replace(Caracteres,"o","[m13]")
    Caracteres=string.replace(Caracteres,"p","[m14]")
    Caracteres=string.replace(Caracteres,"q","[m15]")
    Caracteres=string.replace(Caracteres,"r","[m16]")
    Caracteres=string.replace(Caracteres,"s","[m17]")
    Caracteres=string.replace(Caracteres,"t","[m18]")
    Caracteres=string.replace(Caracteres,"u","[m19]")
    Caracteres=string.replace(Caracteres,"v","[m20]")
    Caracteres=string.replace(Caracteres,"w","[m21]")
    Caracteres=string.replace(Caracteres,"x","[m22]")
    Caracteres=string.replace(Caracteres,"y","[m23]")
    Caracteres=string.replace(Caracteres,"z","[m24]")
    # Majuscules
    Caracteres=string.replace(Caracteres,"A","[M01]")
    Caracteres=string.replace(Caracteres,"B","[M02]")
    Caracteres=string.replace(Caracteres,"C","[M03]")
    Caracteres=string.replace(Caracteres,"D","[M04]")
    Caracteres=string.replace(Caracteres,"E","[M05]")
    Caracteres=string.replace(Caracteres,"F","[M06]")
    Caracteres=string.replace(Caracteres,"G","[M07]")
    Caracteres=string.replace(Caracteres,"H","[M08]")
    Caracteres=string.replace(Caracteres,"I","[M09]")
    Caracteres=string.replace(Caracteres,"J","[M10]")
    Caracteres=string.replace(Caracteres,"K","[M11]")
    Caracteres=string.replace(Caracteres,"L","[M12]")
    Caracteres=string.replace(Caracteres,"M","[M13]")
    Caracteres=string.replace(Caracteres,"N","[M12]")
    Caracteres=string.replace(Caracteres,"O","[M13]")
    Caracteres=string.replace(Caracteres,"P","[M14]")
    Caracteres=string.replace(Caracteres,"Q","[M15]")
    Caracteres=string.replace(Caracteres,"R","[M16]")
    Caracteres=string.replace(Caracteres,"S","[M17]")
    Caracteres=string.replace(Caracteres,"T","[M18]")
    Caracteres=string.replace(Caracteres,"U","[M19]")
    Caracteres=string.replace(Caracteres,"V","[M20]")
    Caracteres=string.replace(Caracteres,"W","[M21]")
    Caracteres=string.replace(Caracteres,"X","[M22]")
    Caracteres=string.replace(Caracteres,"Y","[M23]")
    Caracteres=string.replace(Caracteres,"Z","[M24]")
    # Les nombres
    Caracteres=string.replace(Caracteres,"1","[CC1]")
    Caracteres=string.replace(Caracteres,"2","[CC2]")
    Caracteres=string.replace(Caracteres,"3","[CC3]")
    Caracteres=string.replace(Caracteres,"4","[CC4]")
    Caracteres=string.replace(Caracteres,"5","[CC5]")
    Caracteres=string.replace(Caracteres,"6","[CC6]")
    Caracteres=string.replace(Caracteres,"7","[CC7]")
    Caracteres=string.replace(Caracteres,"8","[CC8]")
    Caracteres=string.replace(Caracteres,"9","[CC9]")
    Caracteres=string.replace(Caracteres,"0","[CC0]")
    # Aures caractères
    Caracteres=string.replace(Caracteres," ","[AC01]")
    Caracteres=string.replace(Caracteres,"/","[AC03]")
    Caracteres=string.replace(Caracteres,"*","[AC04]")
    Caracteres=string.replace(Caracteres,"-","[AC05]")
    Caracteres=string.replace(Caracteres,"+","[AC06]")
    Caracteres=string.replace(Caracteres,"-","[AC07]")
    Caracteres=string.replace(Caracteres,"_","[AC08]")
    Caracteres=string.replace(Caracteres,"(","[AC09]")
    Caracteres=string.replace(Caracteres,")","[AC10]")
    Caracteres=string.replace(Caracteres,"[","[AC11]")
    Caracteres=string.replace(Caracteres,"]","[AC12]")
    Caracteres=string.replace(Caracteres,"{","[AC13]")
    Caracteres=string.replace(Caracteres,"}","[AC14]")
    Caracteres=string.replace(Caracteres,"'","[AC16]")
    Caracteres=string.replace(Caracteres,",","[AC17]")
    Caracteres=string.replace(Caracteres,";","[AC18]")
    Caracteres=string.replace(Caracteres,"?","[AC19]")
    Caracteres=string.replace(Caracteres,":","[AC20]")
    Caracteres=string.replace(Caracteres,"!","[AC21]")
    Caracteres=string.replace(Caracteres,"<","[AC22]")
    Caracteres=string.replace(Caracteres,">","[AC23]")
    Caracteres=string.replace(Caracteres,"°","[AC24]")
    Caracteres=string.replace(Caracteres,"@","[AC25]")
    # Caractères spéciaux
    Caracteres=string.replace(Caracteres,"C","[M03]")
    Caracteres=string.replace(Caracteres,"m","[M13]")
    Caracteres=string.replace(Caracteres,"M","[M13]")
    Caracteres=string.replace(Caracteres,"""[""","[AC11]")
    Caracteres=string.replace(Caracteres,"""]""","[AC12]")


password = input("Choisissez un mot de passe : ")

if len(password) >= 8:
    print("Mot de passe enregistré.")
    exit()
else:
    print("Le mot de passe n'est pas assez sécurisé. Il doit comporter au moins une Majuscule et des caractères spéciaux.")


password = input("Choisissez un mot de passe : ")

while len(password) < 8:
    print("Le mot de passe est trop court. Il doit comporter au moins 8 caractères.")
    password = input("Choisissez un nouveau mot de passe : ")

print("Mot de passe enregistré.")

import hashlib

password = input("Entrez votre mot de passe : ")

password = password.enc
hash_object = hashlib.sha256(password)
crypté = hash_object.hexdigest()

print("Cryptage du mot de passe :", crypté)