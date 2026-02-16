
productos = {"producto1": {"nombre": "Laptop", "precio":1500, "cantidad": 3},"producto2": {"nombre": "Mouse", "precio":20, "cantidad": 10}, "producto3": {"nombre": "Teclado", "precio":50, "cantidad": 5}}


def valor_total_inventario(dic):
    for producto, detalles in dic.items():
        valor = detalles["precio"] * detalles["cantidad"]
        print(f'{detalles["nombre"]}: ${valor}')

valor_total_inventario(productos)