

def acelerar(auto, velocidad, piloto="carlos"):
    if "tesla" in auto:   # auto.includes("tesla") en JS
        print("auto es electrico")

    print(f"El ṕiloto es {piloto}, acelear auto su velocida inicial es : {velocidad}")
    return "acelear!!!"




salida = acelerar("tesla", "200km/h", "juan")
print(salida)