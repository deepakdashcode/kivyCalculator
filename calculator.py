from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from math import *

class MyCalculator(GridLayout):
    def __init__(self,**kwargs):
        super(MyCalculator,self).__init__(**kwargs)
        self.cols=4

        self.result=TextInput(multiline=False)
        self.add_widget(self.result)

        self.result1=TextInput(multiline=False)
        self.add_widget(self.result1)

        self.result2=TextInput(multiline=False)
        self.add_widget(self.result2)

        self.buttonUndo=Button(
            text='<--',
            font_size=18
        )
        self.add_widget(self.buttonUndo)


        


        self.button7=Button(
            text='7',
            font_size=18
        )
        self.add_widget(self.button7)

        self.button8=Button(
            text='8',
            font_size=18
        )
        self.add_widget(self.button8)

        self.button9=Button(
            text='9',
            font_size=18
        )
        self.add_widget(self.button9)

        self.buttonAdd=Button(
            text='+',
            font_size=18
        )      
        self.add_widget(self.buttonAdd)

        self.button4=Button(
            text='4',
            font_size=18
        )
        self.add_widget(self.button4)

        self.button5=Button(
            text='5',
            font_size=18
        )
        self.add_widget(self.button5)

        self.button6=Button(
            text='6',
            font_size=18
        )
        self.add_widget(self.button6)

        self.buttonDiv=Button(
            text='/',
            font_size=18
        )
        self.add_widget(self.buttonDiv)

        self.button1=Button(
            text='1',
            font_size=18
        )
        self.add_widget(self.button1)

        self.button2=Button(
            text='2',
            font_size=18
        )
        self.add_widget(self.button2)

        self.button3=Button(
            text='3',
            font_size=18
        )
        self.add_widget(self.button3)

        self.buttonMul=Button(
            text='*',
            font_size=18
        )
        self.add_widget(self.buttonMul)

        self.button0=Button(
            text='0',
            font_size=18
        )
        self.add_widget(self.button0)

        self.buttonDot=Button(
            text='.',
            font_size=18
        )
        self.add_widget(self.buttonDot)

        self.buttonEquals=Button(
            text='=',
            font_size=18
        )
        self.add_widget(self.buttonEquals)

        self.buttonSub=Button(
            text='-',
            font_size=18
        )
        self.add_widget(self.buttonSub)
       
       # Binding Buttons

        self.button1.bind(on_press=self.one)
        self.button2.bind(on_press=self.two)
        self.button3.bind(on_press=self.three)
        self.button4.bind(on_press=self.four)
        self.button5.bind(on_press=self.five)
        self.button6.bind(on_press=self.six)
        self.button7.bind(on_press=self.seven)
        self.button8.bind(on_press=self.eight)
        self.button9.bind(on_press=self.nine)
        self.button0.bind(on_press=self.zero)
        self.buttonUndo.bind(on_press=self.undo)
        self.buttonAdd.bind(on_press=self.Add)
        self.buttonSub.bind(on_press=self.Sub)
        self.buttonMul.bind(on_press=self.Mul)
        self.buttonDiv.bind(on_press=self.Div)
        self.buttonEquals.bind(on_press=self.Equals)
        self.buttonDot.bind(on_press=self.Dot)







    def one(self,instance):
        self.result.text=self.result.text+'1'

    def two(self,instance):
        self.result.text=self.result.text+'2'
    
    def three(self,instance):
        self.result.text=self.result.text+'3'

    def four(self,instance):
        self.result.text=self.result.text+'4'

    def five(self,instance):
        self.result.text=self.result.text+'5'

    def six(self,instance):
        self.result.text=self.result.text+'6'

    def seven(self,instance):
        self.result.text=self.result.text+'7'

    def eight(self,instance):
        self.result.text=self.result.text+'8'

    def nine(self,instance):
        self.result.text=self.result.text+'9'

    def zero(self,instance):
        self.result.text=self.result.text+'0'

    def undo(self,instance):
        self.result.text=self.result.text[0:-1]

    def Add(self,instance):
        self.result.text=self.result.text+'+'

    def Sub(self,instance):
        self.result.text=self.result.text+'-'       

    def Mul(self,instance):
        self.result.text=self.result.text+'*'
    
    def Div(self,instance):
        self.result.text=self.result.text+'/'

    def Dot(self,instance):
        self.result.text=self.result.text+'.'

    def Equals(self,instance):
        expression=self.result.text
        answer=eval(expression)
        self.result.text=str(answer)



class CalculatorApp(App):
    def build(self):
        return MyCalculator()

if __name__ == '__main__':
    CalculatorApp().run()

