#GUICalculator.py
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QFont
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator Project")
        self.setFixedHeight(750)
        self.setFixedWidth(400)

        self.memory = []
        self.currentOperator = ""
        self.xnum = None
        self.ynum = None
        self.answer = None
        self.highlighted_style = f'background-color:white; border-radius: 45px; font-size: 25px; color:#EB984E '
        
        self.createBtn('Clr',0,200,90,90,"LightGray")
        self.createBtn('+/-',100,200,90,90,"LightGray")
        self.createBtn('%',200,200,90,90,"LightGray")
        self.div = self.createBtn('÷',300,200,90,90,"Orange")

        self.createBtn('7',0,300,90,90,"Grey")
        self.createBtn('8',100,300,90,90,"Grey")
        self.createBtn('9',200,300,90,90,"Grey")
        self.mult = self.createBtn('X',300,300,90,90,"Orange")

        self.createBtn('4',0,400,90,90,"Grey")
        self.createBtn('5',100,400,90,90,"Grey")
        self.createBtn('6',200,400,90,90,"Grey")
        self.minus = self.createBtn('-',300,400,90,90,"Orange")
       

        self.createBtn('1',0,500,90,90,"Grey")
        self.createBtn('2',100,500,90,90,"Grey")
        self.createBtn('3',200,500,90,90,"Grey")
        self.plus = QPushButton(self.createBtn('+',300,500,90,90,"Orange"))
        self.createBtn('0',0,600,180,90,"Grey")
        self.createBtn('.',200,600,90,90,"Grey")
        self.eq = self.createBtn('=',300,600,90,90,"Orange")

        self.display = self.createLbl("0")

        
        

        
        
        
    
    
    def createBtn(self,label,x,y,width,height, color):
        btn = QPushButton(label, self)
        btn.setGeometry(x,y,width,height)


       

        def setColor(color):
            if(color== "LightGray"):
                 btn.setStyleSheet('background-color:#D4CCC5; border-radius: 45px; font-size: 25px')
            elif(color == "Orange"):
                 btn.setStyleSheet('background-color:#EB984E; border-radius: 45px; font-size: 25px')
            else:
                 btn.setStyleSheet('background-color:#4D4C4A; border-radius: 45px; font-size: 25px')
        
        setColor(color)
        
        
        
        highlighted_style = f'background-color:white; border-radius: 45px; font-size: 25px; color:#EB984E '
        default_style = f'background-color:#EB984E; border-radius: 45px; font-size: 25px; color:white '

        highlighted_style2 = f'background-color:#A1A09F; border-radius: 45px; font-size: 25px; color:white'
        default_style2 = f'background-color:#4D4C4A; border-radius: 45px; font-size: 25px; color:white '

       

    






       
        if(label == "Clr"):
            btn.clicked.connect(self.Clr)
            
           
        
        if(label in "0123456789"):
            
            btn.clicked.connect(lambda ch, text = label: self.toConsole(text))
            btn.pressed.connect(lambda: btn.setStyleSheet(highlighted_style2))
            btn.released.connect(lambda: btn.setStyleSheet(default_style2))

        
        if(label=="."):
          
           btn.clicked.connect(self.decimal)
           btn.pressed.connect(lambda: btn.setStyleSheet(highlighted_style2))
           btn.released.connect(lambda: btn.setStyleSheet(default_style2))


        if(label=="%"):
           btn.clicked.connect(self.percentage)

        if(label == "+"):
            btn.pressed.connect(lambda: btn.setStyleSheet(highlighted_style))
            btn.released.connect(lambda: btn.setStyleSheet(default_style))
            btn.clicked.connect(self.operation)
            btn.clicked.connect(lambda ch, text = label: self.setOperator(text))

           
          
            
            
            
           
            

        if(label == "÷"):
            btn.pressed.connect(lambda: btn.setStyleSheet(highlighted_style))
            btn.released.connect(lambda: btn.setStyleSheet(default_style))
            btn.clicked.connect(self.operation)
            btn.clicked.connect(lambda ch, text = label: self.setOperator(text))
        if(label == "+/-"):
            
            btn.clicked.connect(self.negative)

           
            
            

            
           
             

        if(label == "X"):
            btn.pressed.connect(lambda: btn.setStyleSheet(highlighted_style))
            btn.released.connect(lambda: btn.setStyleSheet(default_style))
            btn.clicked.connect(self.operation)
            btn.clicked.connect(lambda ch, text = label: self.setOperator(text))
           
           
           
            

        if(label == "-"):
            btn.pressed.connect(lambda: btn.setStyleSheet(highlighted_style))
            btn.released.connect(lambda: btn.setStyleSheet(default_style))
            btn.clicked.connect(self.operation)
            btn.clicked.connect(lambda ch, text = label: self.setOperator(text))
            

            
           
           
            

        if(label == "="):
            btn.pressed.connect(lambda: btn.setStyleSheet(highlighted_style))
            btn.released.connect(lambda: btn.setStyleSheet(default_style))
            btn.clicked.connect(self.operation)
            btn.clicked.connect(lambda ch, text = label: self.setOperator(text))
        
    def Clr(self):
         self.clearConsole()
         self.answer = ""
         self.xnum = ""
         self.ynum = ""
         self.currentOperator = ""
         self.memory =[]
    def negative(self):
        if self.memory == [] or self.memory == ["0"]:
            return None
        if self.memory[0] == "-":
            self.memory.pop(0)
        else:
            self.memory.insert(0, "-")
        self.display.setText("".join(self.memory))
    

            


            

        
            
      
    
    
    def setOperator(self, operator):
            if(operator=="+"):
                self.currentOperator = "+"
                self.plus.setStyleSheet(self.highlighted_style)
            if(operator=="-"):
                self.currentOperator = "-"
            if(operator=="X"):
                self.currentOperator = "X"
            if(operator=="÷"):
                self.currentOperator = "÷"
            if(operator=="="):
                self.currentOperator = "="
    
    def operation(self):
        if(self.memory == [] or self.memory ==["."]):
            return
        
        if(self.currentOperator== ""):
            first_number = ""
            for x in self.memory:
                first_number +=x
            self.xnum = float(first_number)
            self.clearConsole()
            return
        
        if(self.currentOperator == "+" or self.currentOperator=="-" or self.currentOperator=="X" or self.currentOperator=="÷" ):

            second_number = ""
            for x in self.memory:
                second_number +=x
            self.ynum = float(second_number)
            self.clearConsole()
            if(self.currentOperator == "+"):
                self.answer = self.xnum + self.ynum
            if(self.currentOperator == "-"):
                self.answer = self.xnum - self.ynum
            if(self.currentOperator == "X"):
                self.answer = self.xnum * self.ynum
            if(self.currentOperator == "÷"):
                self.answer = self.xnum / self.ynum
            
            ans = str(self.answer)
            self.xnum = self.answer
            self.answer= ""
            self.toConsole(ans)
            return

                

             





                
                
            
           
            


        

        

        

        

       

    
        
        
    def percentage(self):
        if(self.memory == [] or self.memory == ['.']):
            return None
        number = ""
        for x in self.memory:
            number+=x
        num = float(number)/100
        fin_num = str(num)
        self.memory=[]
        self.toConsole(fin_num)
    
    
    

            




        
        

        

        

       
    


       

    def decimal(self):
        if('.' in self.memory):
            return None
        else:
           
            self.toConsole(".")
    
    def ScientificNotation(self, number):
        number = float(number)
        scientific_notation = f"{number:.2e}"
        return scientific_notation
    
    


  


        

            
              
        
                   

        
            
            
            
          

           
           
               
       
    
    def createLbl(self,text):
        lbl = QLabel(self)
        lbl.setText(text)
        lbl.setGeometry(0,0,400,200)
        
        font = QFont("Arial ",80)
        lbl.setFont(font)
        lbl.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        lbl.setStyleSheet("background-color: black; color: white;")
        
        lbl.setWordWrap(True)
        lbl.setScaledContents(True)
        
        
        
        return lbl
 
        
        
    
    def clearConsole(self):
        self.display.setText("")
        self.memory = []
    
    def toConsole(self, number):
        if len(self.memory) == 9:
            return
      
        self.memory.append(number)
        final_number = "".join(self.memory)
        self.display.setText(self.ScientificNotation(final_number) if len(final_number) > 9 else final_number)

      

       
      
        

    

    
       
        
    

app = QApplication([])
window = Window()
window.setStyleSheet("background-color: #000000 ")
window.show()
sys.exit(app.exec())
    
    
