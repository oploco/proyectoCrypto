from django.shortcuts import render

CRYPTOS = ['Bitcoin','Ethereum','Tether','BNB','Solana','XRP','Lido Staked Ether','USDC','Dogecoin','Cardano','Avalanche','Shiba Inu']

def index(request):
    rutas_imagenes = [f"../static/{nombre}.png" for nombre in CRYPTOS]
    #image_paths = ["../static/Bitcoin.png","../static/Ethereum.png"]  # Lista de rutas de las imágenes

    #image_paths = rutas_imagenes  # Lista de rutas de las imágenes
    image_paths = CRYPTOS
    print(request)
    return render(request, 'index.html', {'image_paths': image_paths})

""" def frames_con_imagenes(request):
    return render(request, 'frames_con_imagenes.html') """
