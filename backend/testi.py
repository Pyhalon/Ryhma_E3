
from datetime import datetime
from pyscript import display, window, document

def testifunktio(event):
    tehot = [0, 1.7, 1.8, 1.0, 1.2, 2.6, 0.05, 0.7, 1.1, 5.0, 0.16, 0.15, 0.3, 0.005, 0.08, 1.2, 1.5, 2.0, 1.0, 1.2, 0.6]

    # vastaa input()
    kodinkonevalitsija = int(document.querySelector("#vetovalikko").value)
    tuntihinta = float(document.querySelector("#nykyinenhinta").innerText)
    tunnit = float(document.querySelector("#käyttötunnit").value)
    window.console.log(tunnit)
    minuutit = float(document.querySelector("#käyttöminuutit").value)
    if tunnit < 0 or minuutit < 0:
        window.console.log("Annettu negatiivinen aika")
        return 
    if tunnit > 24 or minuutit > 59:
        window.console.log("Annettu liian iso aika")
        return
    
    # vastaa print()
    window.console.log(kodinkonevalitsija, tuntihinta, tunnit, minuutit, tehot[kodinkonevalitsija])
    hinta = tuntihinta * (tunnit+minuutit/60) * tehot[kodinkonevalitsija]
    document.querySelector("#tulos").innerText = "{:.2f} €".format(hinta / 100)

    window.console.log("nappia painettu!")
   
