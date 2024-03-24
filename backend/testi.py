
from datetime import datetime
from pyscript import display, window, document

def testifunktio(event):
    tehot = [1.5, 1.8, 1.7, 1.0, 0.16, 1.2]

    # vastaa input()
    kodinkonevalitsija = int(document.querySelector("#vetovalikko").value)
    tuntihinta = float(document.querySelector("#nykyinenhinta").innerText)
    tunnit = float(document.querySelector("#käyttötunnit").value)
    window.console.log(tunnit)
    minuutit = float(document.querySelector("#käyttöminuutit").value)
    
    # vastaa print()
    window.console.log(kodinkonevalitsija, tuntihinta, tunnit, minuutit, tehot[kodinkonevalitsija])
    hinta = tuntihinta * (tunnit+minuutit/60) * tehot[kodinkonevalitsija]
    document.querySelector("#tulos").innerText = "{:.2f} €".format(hinta / 100)

    window.console.log("nappia painettu!")
   