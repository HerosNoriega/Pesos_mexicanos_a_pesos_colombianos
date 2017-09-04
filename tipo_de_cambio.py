# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
    Mex_to_Col_rate = 145.97

    return Mex_to_Col_rate * ammount

def run():
    print("CALCULADORA DE DIVISAS")
    print("Convierte pesos Mexicanos a pesos Colombianos.")
    print('')
    ammount = float(raw_input("Cantidad $ Mexicanos: "))

    foreign_exchange_calculator(ammount)

    result = foreign_exchange_calculator(ammount)

    print('${} pesos Mexicanos son ${} pesos Colombianos.'.format(ammount, result))
    print('')

if __name__ == '__main__':
    run()
