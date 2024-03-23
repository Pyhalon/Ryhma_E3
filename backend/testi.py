
from datetime import datetime
from pyscript import display, window, document

#from pyscript import when, display

#@when("click", "#laske")
def testifunktio(event):

    # vastaa input()
    kodinkonevalitsija = document.querySelector("#vetovalikko").value
    tunnit = document.querySelector("#käyttötunnit").value
    window.console.log(tunnit)
    minuutit = document.querySelector("#käyttöminuutit").value
    # vastaa print()
    document.querySelector("#tulos").innerText = kodinkonevalitsija +  " " + tunnit + " tuntia " + minuutit + " minuuttia  maksaisi"

    window.console.log("nappia painettu!")
    