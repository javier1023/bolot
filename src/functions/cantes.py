def sumar_cantes (button,
                  button_tercera1,
                  button_tercera2,
                  button_cincuenta1,
                  button_cincuenta2,
                  button_ciento_cincuenta1,
                  button_ciento_cincuenta2,
                  button_doscientos1,
                  button_doscientos2,
                  button_renuncio1,
                  button_renuncio2,
                  points_input1,
                  points_input2,
                  team1_counters,
                  team2_counters):
    if button.text == 'Borrar':
        points_input1.text = '0'
        points_input2.text = '0'
        team1_counters = {'tercera': 0, 'cincuenta': 0, 'cien': 0, 'ciento_cincuenta': 0, 'doscientos': 0}
        team2_counters = {'tercera': 0, 'cincuenta': 0, 'cien': 0, 'ciento_cincuenta': 0, 'doscientos': 0}
    elif button.text == 'Tercera' and button in (button_tercera1, button_tercera2):
        if button is button_tercera1:
            team1_counters['tercera'] += 1
            points_input1.text = str(int(points_input1.text) + 20)
        else:
            team2_counters['tercera'] += 1
            points_input2.text = str(int(points_input2.text) + 20)
    elif button.text == 'Cincuenta' and button in (button_cincuenta1, button_cincuenta2):
        if button is button_cincuenta1:
            team1_counters['cincuenta'] += 1
            points_input1.text = str(int(points_input1.text) + 50)
        else:
            team2_counters['cincuenta'] += 1
            points_input2.text = str(int(points_input2.text) + 50)
    elif button.text == 'Ciento cincuenta' and button in (
            button_ciento_cincuenta1, button_ciento_cincuenta2):
        if button is button_ciento_cincuenta1:
            team1_counters['ciento_cincuenta'] += 1
            points_input1.text = str(int(points_input1.text) + 150)
        else:
            team2_counters['ciento_cincuenta'] += 1
            points_input2.text = str(int(points_input2.text) + 150)
    elif button.text == 'Doscientos' and button in (button_doscientos1, button_doscientos2):
        if button is button_doscientos1:
            team1_counters['doscientos'] += 1
            points_input1.text = str(int(points_input1.text) + 200)
        else:
            team2_counters['doscientos'] += 1
            points_input2.text = str(int(points_input2.text) + 200)
    elif button.text == 'Renuncio' and button in (button_renuncio1, button_renuncio2):
        if button is button_renuncio1:
            points_input1.text = str(int(points_input1.text) + 0)  # No se incrementa el contador
        else:
            points_input2.text = str(int(points_input2.text) + 0)  # No se incrementa el contador
