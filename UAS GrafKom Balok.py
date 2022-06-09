#Nama   : Rizka Nurul Septiani Hakim
#NIM    : 20051397026
#Kelas  : 2020 B
#Prodi  : D4 Manajemen Informatika
#Tugas UAS Membuat Balok 3D

#memanggil modul pygame
import pygame
from pygame.locals import *
#menggunakan openGL
from OpenGL.GL import *
from OpenGL.GLU import *

#mendefinisikan titik-titik sudutnya
#tinggixlebarxtinggi
vertices = (
(1.5, -3, -5),
(1.5, 3, -5),
(-1.5, 3, -5),
(-1.5, -3, -5),
(1.5, -3, 5),
(1.5, 3, 5),
(-1.5, -3, 5),
(-1.5, 3, 5)
)

#mendefinisikan garis
edges = (
(0,1),
(0,3),
(0,4),
(2,1),
(2,3),
(2,7),
(6,3),
(6,4),
(6,7),
(5,1),
(5,4),
(5,7)
)

#mendefinisikan warna
colors = (
    (1,1,1),
    (1,0,0),
    (1,0,1),
    (1,1,0),
    (0,1,1),
    (0,1,1),
    (1,1,0),
    (1,0,0),
    (1,0,1),
    (1,1,0),
    (1,1,1),
    (1,1,0),
    )

#mendefisikan sisi
surfaces = (
(0,1,2,3),
(3,2,7,6),
(6,7,5,4),
(4,5,1,0),
(1,5,7,2),
(4,0,3,6)
)

#menyatukan vertices, edges, surfaces, color untuk membuat balok
def Balok():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

#membuat tampilan layar untuk menampilkan Balok
def main():
    #inisialisasi pygame
    pygame.init()
    #resolusi display layar
    display = (850,600)
    #mode layar double buffering
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #mengubah perspektif, fov 45*, znear 0.1, zfar 50
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    #memindahkan objek sesuai dengan matriks translasi
    glTranslatef(0.0,0.0, -20)
    #infinite looping
    while True:
        #apabila ditekan tombol x, maka program akan berhenti.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #apabila ada tombol keyboard yang ditekan, 
        #maka akan dilakukan fungsi berikut
        if event.type == pygame.KEYDOWN:
            #bila yang di tekan tombol panah kiri
            #Balok berpindah ke kiri sebanyak 0.5
            if event.key == pygame.K_LEFT:
                glTranslatef(-0.5,0,0)
            #bila yang di tekan tombol panah kanan
            #Balok berpindah ke kanan sebanyak 0.5
            if event.key == pygame.K_RIGHT:
                glTranslatef(0.5,0,0)
            #bila yang di tekan tombol panah atas
            #Balok berpindah ke atas sebanyak 0.1
            if event.key == pygame.K_UP:
                glTranslatef(0,1,0)
            #bila yang di tekan tombol panah bawah
            #Balok berpindah ke bawah sebanyak 0.-1
            if event.key == pygame.K_DOWN:
                glTranslatef(0,-1,0)
        #objek dapat bergerak apabila menggunakan mouse,
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)
                if event.button == 5:
                    glTranslatef(0,0,-1.0)
        #objek bergerak dengan cara berotasi
        glRotatef(1, 3, 1, 1)
        #menghapus semua kanvas/display
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Balok()
        pygame.display.flip()
        #menunggu 10ms sebelum looping lagi
        pygame.time.wait(10) 
main()