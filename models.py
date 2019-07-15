import mongoengine as _db

# Clases de utilidad


class Colaborador(_db.Document):
    primer_nombre = _db.StringField()
    apellidos = _db.StringField()
    autorización = _db.StringField()
    email = _db.EmailField()


class Media(_db.Document):
    nombre = _db.StringField()
    localizacion = _db.StringField()
    descripcion = _db.StringField()


class Tag(_db.Document):
    nombre = _db.StringField()
    descripcion = _db.StringField()


class Edit(_db.Document):
    query = _db.StringField()
    editor = _db.ReferenceField(Colaborador)
    date = _db.DateTimeField()


class Estudio(_db.Documetn):
    nombre: _db.StringField()
    descripcion: _db.StringField()
    fotos: _db.ListField(_db.ReferenceField(Media))
    fundadores: _db.ListField(_db.ReferenceField(Colaborador))
    proyectos: _db.ListField(_db.ReferenceField('Proyecto'))


class menciones(_db.EmbeddedDocument):
    publicacion = _db.StringField()
    url = _db.URLField()
    email = _db.EmailField()


class Proyecto(_db.Document):
    titulo = _db.StringField()
    descripcion = _db.StringField()
    cover = _db.ReferenceField(Media)
    fecha_publicacion = _db.DateField()
    productores_proyecto = _db.ListField(_db.ReferenceField(Estudio))
    colaboradores_proyecto = \
        _db.ListField(_db.ReferenceField(Colaborador))
    rated = _db.StringField()
    menciones = _db.ListField(_db.EmbeddedDocumentField(menciones))
    tags = _db.ListField(_db.ReferenceField(Tag))
    keywords = _db.ListField()
    # allow
    meta = {'allow_inheritance': True}
