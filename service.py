import models as md

descripcion_proyecto = 'Uno de los primeros proyectos de comunicación\
                        visual en monterrey en ser reconocido de \
                        manera internacional'

tag1 = md.Tag(nombre='Branding').save()
tag2 = md.Tag(nombre='Arquitectura').save()

mencion

proyect = md.Proyecto(titulo='Theurel & Thomas',
                      descripcion=descripcion_proyecto,
                      keywords=[tag1.id, tag2.id])
