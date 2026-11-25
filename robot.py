def scegli_articolo(parola):
    # Rimuoviamo eventuali spazi e passiamo tutto in minuscolo
    parola = parola.lower().strip()
    
    # 1. Gestiamo le eccezioni speciali con un piccolo dizionario
    eccezioni = {
        "zucchero": "lo",
        "pneumatico": "lo",
        "gnomo": "lo",
        "mano": "la"  # Finisce in 'o' ma è femminile (eccezione)
    }
    
    if parola in eccezioni:
        return eccezioni[parola]
    
    # 2. Regola per "lo" (parole che iniziano con s+consonante, z, x, y, gn, ps)
    gruppi_lo = ('z', 'x', 'y', 'gn', 'ps', 'pn')
    if parola.startswith(gruppi_lo) or (parola.startswith('s') and len(parola) > 1 and not is_vocale(parola[1])):
        return "lo"
        
    # 3. Regola per "la" (generalmente parole che finiscono in 'a')
    elif parola.endswith('a'):
        return "la"
        
    # 4. Regola per "il" (maschili generali)
    else:
        return "il"

def is_vocale(lettera):
    return lettera in 'aeiou'

# Testiamo la nostra funzione
print(scegli_articolo("cane"))      # Output: il
print(scegli_articolo("amica"))     # Output: la
print(scegli_articolo("zaino"))     # Output: lo
print(scegli_articolo("pneumatico"))# Output: lo (preso dalle eccezioni)
