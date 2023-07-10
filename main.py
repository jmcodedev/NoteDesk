# IMPORTS

import sys
from PyQt5 import uic
from PyQt5.QtGui import QPalette, QPixmap, QResizeEvent, QMouseEvent
from PyQt5.QtCore import Qt, QPoint, QSize, QDate
from PyQt5.QtWidgets import (QMainWindow,QApplication, QDialog, QVBoxLayout, QWidget, QPushButton, QFrame, QLabel,QToolButton, QHBoxLayout, QStyle, QMessageBox)
from PySide6 import QtCore, QtGui, QtWidgets
from main_design import *
from login_deisgn import *
from register_deisgn import *
from conexionBD import *
import mysql.connector
from datetime import datetime

current_date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
totalData = Data_register()

##############################################################################################################################################################

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('Login.ui', self)
        self.logInBttn.clicked.connect(self.loginfunction)
        self.registerBttn.clicked.connect(self.gotocreate)
        self.cci_Bttn.clicked.connect(self.gotoAppAsGuest)
    # FUNCION PARA COMPROBAR DATOS EN LA BBDD

    def loginfunction(self):
        self.checkUser()

    # FUNCION PARA ABRIR PANTALLA DE REGISTRO

    def gotocreate(self):
        self.close()
        self.registerWindow = CreateAcc()
        self.registerWindow.show()
        
    # FUNCION PARA ABRIR APP

    def gotoApp(self, userId):
        self.close()
        self.appWindow = AppTareas(self.entryUsername.text(), userId)
        self.appWindow.show()
    
    # ABRIR APP COMO INVITADO

    def gotoAppAsGuest(self):
        self.close()
        self.appWindow = AppTareas("Invitado", 22)
        self.appWindow.show()   

    # FUNCION QUE COMPRUEBA LOS DATOS EN LA BBDD

    def checkUser(self):

        resultadoLogIn = totalData.logInUser(self.entryUsername.text(), self.entryPassword.text())
        
        if resultadoLogIn is not False:
           
            self.gotoApp(resultadoLogIn) 
            
        else:

            # MENSAJE DE ERROR EN DATOS
            QMessageBox.critical(self, "Error", "Acceso denegado! Error en los datos.")
            


# VENTANA DE REGISTRO

class CreateAcc(QMainWindow):
    
    def __init__(self):
        super(CreateAcc, self).__init__()
        uic.loadUi('Register.ui', self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.backButton.clicked.connect(self.gotoLogin)
        
    # FUNCION CREAR CUENTA EN LA BBDD

    def gotoLogin(self):
        self.close()
        self.loginWindow = Login()
        self.loginWindow.show()

    # FUNCIÓN PARA CREAR USUARIO Y PASAR LOS DATOS A LA FUNCIÓN QUE SE ENCARGA DE ELLO

    def createaccfunction(self):

        if totalData.createUser(self.registerUsername.text(), self.registerPassword.text()) is False:        
            # MENSAJE ERROR POR NOMBRE DE USUARION EN USO
            QMessageBox.critical(self, "Error", "Nombre de usuario en uso")
        else:
            # MENSAJE DE ÉXITO REGISTRANDO USUARIO
            QMessageBox.information(self,"Éxito", "Usuario creado correctamente! Vuelva a la pantalla de Inicio de Sesión")
            

# VENTANA PRINCIPAL DE LA APP

class AppTareas(QMainWindow):

    def __init__(self, username, userId):

        super(AppTareas, self).__init__() 
        uic.loadUi('Main.ui', self)
        self.btnRestaurar.hide()
        self.username = username
        self.userId = userId
        self.usrBttn.setText(self.username)
        self.tablaResultados.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.stackedWidget.setCurrentWidget(self.p_Ayuda)
        
        # ESCONDER BARRA DE TITULO PARA UTILIZAR LA PERSONALIZADA
        
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # ESCONDER MENU

        self.frame_menu.setFixedWidth(0)

        # SIZE GRIP

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # MOVIMIENTO MENU

        self.frame_superior.mouseMoveEvent = self.mover_ventana
        
        # FILTRADO DE NOTAS

        self.filterButton.clicked.connect(self.filtrarNotas)

        # ABRIR DETALLE NOTAS

        for i in range(1, 24):
            titleButton = f"nt{i}" 
            label = getattr(self, titleButton)
            label.clicked.connect(lambda _, index = i: self.titleClicked(index))

        # ACCION BOTON MENU

        self.btnMenu.clicked.connect(self.move_menu)

        # ACCIONES BOTON VER NOTA

        self.goBackBttn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.p_Inicio))

        # ACCIONES BOTONES MENU

        self.bt_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.p_Inicio))
        self.bt_inicio.clicked.connect(self.writeNotes)
        self.bt_Buscar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.p_Busqueda))
        self.bt_Editar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.p_Edicion))
        self.bt_Borrado.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.p_Borrado))
        self.bt_Ayuda.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.p_Ayuda))

        # ACCIONES BOTONES PANTALLA RESUMEN NOTAS

        self.addBtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.p_AddNote))

        # ACCIONES BOTONES AÑADIR NOTA

        self.cancelBttn_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.p_Inicio))
        self.saveBttn_5.clicked.connect(self.createNote)
        self.saveBttn_5.clicked.connect(self.writeNotes)
        self.dateLabel.setText("La nota será guardada con fecha: " + current_date)

        # ACCIONES BOTONES BARRA DE TITULO

        self.btnMinimizar.clicked.connect(self.control_bt_minimizar)
        self.btnMaximizar.clicked.connect(self.control_bt_maximizar)
        self.btnRestaurar.clicked.connect(self.control_bt_normal)
        self.btnCerrar.clicked.connect(totalData.closeConnection)
        self.btnCerrar.clicked.connect(lambda: self.close())

        # ACCIONES BOTONES EDITAR NOTA

        self.searchButton_edit.clicked.connect(self.buscarNotaEditar)
        self.updateNoteBttn.clicked.connect(self.editarNota)
        self.updateNoteBttn.clicked.connect(self.writeNotes)
        self.updateNoteBttn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.p_Inicio))
        

        # ACCIONES BOTONES BORRAR NOTA

        self.searchButton_delete.clicked.connect(self.buscarNotaBorrar)
        self.deleteNoteBttn.clicked.connect(self.borrarNota)
        self.deleteNoteBttn.clicked.connect(self.writeNotes)
        self.deleteNoteBttn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.p_Inicio))

    # FUNCIONES MINIMIZAR / CERRAR / MAXIMIZAR / NORMALIZAR

    def control_bt_minimizar(self):
        self.showMinimized()
    
    def control_bt_normal(self):
        self.showNormal()
        self.btnRestaurar.hide()
        self.btnMaximizar.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.btnMaximizar.hide()
        self.btnRestaurar.show()
    
    # ABRIR Y CERRAR MENU LATERAL

    def move_menu(self):

        if self.frame_menu.width() == 200:
            self.frame_menu.setFixedWidth(0)
        else:
            self.frame_menu.setFixedWidth(200)


    # MOVIMIENTO DE VENTANA

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    
    def mover_ventana(self, event):
            if self.isMaximized() == False:			
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()

            if event.globalPos().y() <=20:
                self.showMaximized()
            else:
                self.showNormal()
    
    def createNote(self):

        self.tituloNota = self.inpTitulo.text()
        self.contenidoNota = self.inpDesc.toPlainText()
        totalData.createNote(self.tituloNota, self.contenidoNota, self.userId)
        self.stackedWidget.setCurrentWidget(self.p_Inicio)
    
    def buscarNotaEditar(self):

        self.idNote = self.editNoteId.text()
        datosDB = totalData.searchNote(self.idNote, self.userId)

        if datosDB is False:
            QMessageBox.critical(self, "Error", "No se ha encontrado la nota")
        
        else:
            self.inpTitulo_2.setText(datosDB[0])
            self.inpDesc_2.setText(datosDB[1])
            

    def buscarNotaBorrar(self):

        self.idNote = self.deleteNoteId.text()

        datosDB = totalData.searchNote(self.idNote, self.userId)

        if datosDB is False:
            QMessageBox.critical(self, "Error", "No se ha encontrado la nota")
        else:
            self.tituloBorrado.setText(datosDB[0])
            self.contenidoBorrado.setText(datosDB[1])
    
    def borrarNota(self):
        deleteTitle = self.tituloBorrado.text()
        
        totalData.deleteNote(deleteTitle, self.userId)
    
    def editarNota(self):

        idNote = self.editNoteId.text()
        titleToEdit = self.inpTitulo_2.text()
        contenToEdit = self.inpDesc_2.toPlainText()
        totalData.updateNote(idNote, titleToEdit, contenToEdit ,self.userId)
    

    def filtrarNotas(self):

        tituloBusqueda = self.fil_Title.text()
        datosDB = totalData.filterNote(tituloBusqueda, self.userId)
        
        self.tablaResultados.clearContents()
        self.tablaResultados.setRowCount(len(datosDB))
        for i, fila in enumerate(datosDB):
            for j, dato in enumerate(fila):
                if dato is None:
                    item = QtWidgets.QTableWidgetItem("Nunca")
                    self.tablaResultados.setItem(i, j, item)
                else:
                    item = QtWidgets.QTableWidgetItem(str(dato))
                    self.tablaResultados.setItem(i, j, item)
    def writeNotes(self):
            conn = mysql.connector.connect(
                host = 'db4free.net',
                port = 3306,
                username = 'msjoan02',
                password = 'KFRD_MEhAN#fj5T',
                db = 'tfg_jmartinez'
            )
            cursor = conn.cursor()
            query = 'SELECT titulo, fecha_creacion FROM notas WHERE id_usuario =%s ORDER BY fecha_creacion DESC'
            cursor.execute(query, (self.userId,))
            notas = cursor.fetchall()
            nLabel = 23

            for i in range(nLabel):
                if i < len(notas):
                    titulo, fecha = notas[i]
                    label_titulo = getattr(self, f"nt{i+1}")
                    label_titulo.setText(titulo)
                    label_fecha = getattr(self, f"d{i+1}")
                    label_fecha.setText(str(fecha))
                else:
                    label_titulo = getattr(self, f"nt{i+1}")
                    label_titulo.setText("")
                    label_fecha = getattr(self, f"d{i+1}")
                    label_fecha.setText("Creada el:")
            cursor.close()
            conn.close()

    def titleClicked(self, index):
        self.stackedWidget.setCurrentWidget(self.p_NoteDetails)
        titleButton = f"nt{index}"
        titulo = getattr(self, titleButton).text()
        datosDB = totalData.selectNote(titulo, self.userId)
        if datosDB:
            self.viewTitle.setText(datosDB[0])
            self.viewContent.setText(datosDB[1])
            self.viewOriginDate.setText("Creada el: " + str(datosDB[2]))
            
            if datosDB[3] is None:
                self.viewLastEdit.setText("Modificada por última vez: Nunca")
            else:
                self.viewLastEdit.setText("Modificada por última vez: " + str(datosDB[3]))
            
            self.viewCreator.setText("Nota creada por: " + datosDB[4])



##############################################################################################################################################################
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Login()
    widget.show()
    sys.exit(app.exec_())