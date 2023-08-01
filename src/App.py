from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox

from src.functions import cantes

class CalculatorApp(App):

    def build(self):
        self.sm = ScreenManager()

        # Pantalla principal con botones de selección de partida
        main_screen = Screen(name='main')
        main_layout = BoxLayout(orientation='vertical')

        button_1000 = Button(text="Partida a 1000")
        button_1000.bind(on_release=self.calculate_points_1000)
        main_layout.add_widget(button_1000)

        button_1500 = Button(text="Partida a 1500")
        button_1500.bind(on_release=self.calculate_points_1500)
        main_layout.add_widget(button_1500)

        main_screen.add_widget(main_layout)
        self.sm.add_widget(main_screen)

        return self.sm

    def calculate_points_1000(self, instance):
        result = 1000  # Cálculo de puntos para partida a 1000
        if not self.sm.has_screen('score'):
            self.create_score_screen(result)
        self.sm.current = 'score'

    def calculate_points_1500(self, instance):
        result = 1500  # Cálculo de puntos para partida a 1500
        #comprobamos si ya existe una screen con el nombre 'score'
        if not self.sm.has_screen('score'):
            self.create_score_screen(result)
        self.sm.current = 'score'

    def create_score_screen(self, target_points):
        score_screen = Screen(name='score')
        score_layout = BoxLayout(orientation='vertical')

        # Diccionarios para contar la cantidad de veces que se ha pulsado cada botón
        self.team1_counters = {'tercera': 0, 'cincuenta': 0, 'cien': 0, 'ciento_cincuenta': 0, 'doscientos': 0}
        self.team2_counters = {'tercera': 0, 'cincuenta': 0, 'cien': 0, 'ciento_cincuenta': 0, 'doscientos': 0}

        # Puntos de cada pareja
        self.team1_points = 0
        self.team2_points = 0

        # División de la pantalla en dos mitades
        half_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.9))

        # Etiquetas para mostrar el historial de puntos de cada pareja
        self.team1_label = Label(text=f'Pareja 1: {self.team1_points} puntos')
        self.team2_label = Label(text=f'Pareja 2: {self.team2_points} puntos')
        half_layout.add_widget(self.team1_label)
        half_layout.add_widget(self.team2_label)

        score_layout.add_widget(half_layout)

        # Botón "Apuntar ronda" en la parte inferior
        apuntar_button = Button(text="Apuntar ronda", size_hint=(1, 0.1))
        apuntar_button.bind(on_release=lambda x: self.on_apuntar_button_press())
        score_layout.add_widget(apuntar_button)

        finalizar_button = Button(text="Finalizar partida", size_hint=(1, 0.1))
        finalizar_button.bind(on_release=lambda x: self.on_finalizar_button_press())
        score_layout.add_widget(finalizar_button)


        score_screen.add_widget(score_layout)
        self.sm.add_widget(score_screen)


    def on_finalizar_button_press(self):
        self.team1_points = '0'
        self.team2_points = '0'
        self.team1_label.text = f'Pareja 1: {self.team1_points} puntos'
        self.team2_label.text = f'Pareja 2: {self.team2_points} puntos'
        self.sm.current = 'main'

    def on_apuntar_button_press(self):
        #si existe ya una screen con el nombre 'round' no la creamos otra vez
        if not self.sm.has_screen('round'):
            self.create_round_screen()
        self.sm.current = 'round'

    def create_round_screen(self):
        round_screen = Screen(name='round')
        round_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))

        # División de la pantalla en dos secciones
        top_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.8))
        bottom_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        # Parte de top_layout

        # Dividimos top_layout en dos mitades verticales 50%
        half_layout1 = BoxLayout(orientation='vertical', size_hint=(0.5, 1))
        half_layout2 = BoxLayout(orientation='vertical', size_hint=(0.5, 1))

        # Las dos mitades van a ser iguales, van a tener un text_input, una casilla y 5 botones

        # Text_input de la mitad 1
        self.points_input1 = TextInput(multiline=False, text='0')
        half_layout1.add_widget(self.points_input1)

        # Casilla de la mitad 1
        self.checkbox_pareja1 = CheckBox()
        self.checkbox_pareja1.bind(active=lambda instance, value: self.toggle_pareja_principal(1, value))
        half_layout1.add_widget(self.checkbox_pareja1)

        # Botones de la mitad 1
        self.button_tercera1 = Button(text='Tercera', on_release=lambda btn: self.cante(btn))
        self.button_cincuenta1 = Button(text='Cincuenta', on_release=lambda btn: self.cante(btn))
        self.button_ciento_cincuenta1 = Button(text='Ciento cincuenta', on_release=lambda btn: self.cante(btn))
        self.button_doscientos1 = Button(text='Doscientos', on_release=lambda btn: self.cante(btn))
        self.button_renuncio1 = Button(text='Renuncio', on_release=lambda btn: self.cante(btn))
        # Añadimos los botones a la mitad 1 de forma vertical
        half_layout1.add_widget(self.button_tercera1)
        half_layout1.add_widget(self.button_cincuenta1)
        half_layout1.add_widget(self.button_ciento_cincuenta1)
        half_layout1.add_widget(self.button_doscientos1)
        half_layout1.add_widget(self.button_renuncio1)

        # Text_input de la mitad 2
        self.points_input2 = TextInput(multiline=False, text='0')
        half_layout2.add_widget(self.points_input2)

        # Botones de la mitad 2
        self.checkbox_pareja2 = CheckBox()
        self.checkbox_pareja2.bind(active=lambda instance, value: self.toggle_pareja_principal(2, value))
        half_layout2.add_widget(self.checkbox_pareja2)

        # Botones de la mitad 2
        self.button_tercera2 = Button(text='Tercera', on_release=lambda btn: self.cante(btn))
        self.button_cincuenta2 = Button(text='Cincuenta', on_release=lambda btn: self.cante(btn))
        self.button_ciento_cincuenta2 = Button(text='Ciento cincuenta', on_release=lambda btn: self.cante(btn))
        self.button_doscientos2 = Button(text='Doscientos', on_release=lambda btn: self.cante(btn))
        self.button_renuncio2 = Button(text='Renuncio', on_release=lambda btn: self.cante(btn))
        # Añadimos los botones a la mitad 2 de forma vertical
        half_layout2.add_widget(self.button_tercera2)
        half_layout2.add_widget(self.button_cincuenta2)
        half_layout2.add_widget(self.button_ciento_cincuenta2)
        half_layout2.add_widget(self.button_doscientos2)
        half_layout2.add_widget(self.button_renuncio2)

        # Añadimos las dos mitades a top_layout
        top_layout.add_widget(half_layout1)
        top_layout.add_widget(half_layout2)

        # Parte de bottom_layout
        # Se van a crear 2 botones en la parte inferior
        self.button_save = Button(text='Guardar', on_release=lambda btn: self.guardar_ronda(btn))
        self.button_delete = Button(text='Borrar', on_release=lambda btn: self.cante(btn))

        # Añadimos los botones a bottom_layout

        bottom_layout.add_widget(self.button_save)
        bottom_layout.add_widget(self.button_delete)

        # Añadimos top_layout y bottom_layout a round_layout
        round_layout.add_widget(top_layout)
        round_layout.add_widget(bottom_layout)

        # Añadimos round_layout a round_screen
        round_screen.add_widget(round_layout)

        # Añadimos round_screen a self.sm
        self.sm.add_widget(round_screen)

    def toggle_pareja_principal(self, pareja, value):
        if value:
            if pareja == 1:
                self.checkbox_pareja2.active = False
            elif pareja == 2:
                self.checkbox_pareja1.active = False
            print(f"Pareja {pareja} es la pareja principal")
        else:
            print(f"Pareja {pareja} ya no es la pareja principal")

    def cante(self, button):

        cantes.sumar_cantes(button,
                     self.button_tercera1,
                     self.button_tercera2,
                     self.button_cincuenta1,
                     self.button_cincuenta2,
                     self.button_ciento_cincuenta1,
                     self.button_ciento_cincuenta2,
                     self.button_doscientos1,
                     self.button_doscientos2,
                     self.button_renuncio1,
                     self.button_renuncio2,
                     self.points_input1,
                     self.points_input2,
                     self.team1_counters,
                     self.team2_counters)

    def guardar_ronda(self, boton):
        self.sm.current = 'score'
        points_max = 162
        for c, v in self.team1_counters.items():
            if c == 'tercera':
                points_max = points_max + (20 * v)
            elif c == 'cincuenta':
                points_max = points_max + (50 * v)
            elif c == 'ciento_cincuenta':
                points_max = points_max + (150 * v)
            elif c == 'doscientos':
                points_max = points_max + (200 * v)
        for c, v in self.team2_counters.items():
            if c == 'tercera':
                points_max = points_max + (20 * v)
            elif c == 'cincuenta':
                points_max = points_max + (50 * v)
            elif c == 'ciento_cincuenta':
                points_max = points_max + (150 * v)
            elif c == 'doscientos':
                points_max = points_max + (200 * v)

        if not self.checkbox_pareja1.active:
            if int(self.points_input1.text) > int(points_max / 2):
                # Puestada
                self.points_input1.text = str(points_max)
                self.points_input2.text = '0'
            elif int(self.points_input1.text) == int(points_max / 2):
                # Empate
                self.points_input1.text = str(int(points_max / 2))
                self.points_input2.text = str('0')
            else:
                self.points_input2.text = str(int(self.points_input2.text) + points_max - int(self.points_input1.text))

        if not self.checkbox_pareja2.active:
            if int(self.points_input2.text) > int(points_max / 2):
                # Puestada
                self.points_input2.text = str(points_max)
            elif int(self.points_input2.text) == int(points_max / 2):
                # Empate
                self.points_input2.text = str(int(points_max / 2))
                self.points_input1.text = str('0')
            else:
                self.points_input1.text = str(int(self.points_input1.text) + points_max - int(self.points_input2.text))

        # modificar el score de cada pareja
        self.team1_points += int(self.points_input1.text)
        self.team2_points += int(self.points_input2.text)

        #modificar la label de cada pareja
        self.team1_label.text = str(self.team1_points)
        self.team2_label.text = str(self.team2_points)

        self.points_input1.text = '0'
        self.points_input2.text = '0'
        self.team1_counters = {'tercera': 0, 'cincuenta': 0, 'cien': 0, 'ciento_cincuenta': 0, 'doscientos': 0}
        self.team2_counters = {'tercera': 0, 'cincuenta': 0, 'cien': 0, 'ciento_cincuenta': 0, 'doscientos': 0}
        self.checkbox_pareja1.active = False
        self.checkbox_pareja2.active = False
